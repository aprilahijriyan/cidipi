from __future__ import annotations

import asyncio
import json
import logging
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Literal,
    Optional,
    Union,
)

import async_timeout
import websockets
from curl_cffi import requests
from pydantic import BaseModel, Field, PrivateAttr, TypeAdapter
from typing_extensions import TypedDict

from cidipi.interface import ICommand
from cidipi.utils import AtomicInteger

if TYPE_CHECKING:
    from cidipi.client import Browser

logger = logging.getLogger(__name__)


async def wait_for_result(data: "Payload", future: asyncio.Future):
    if data.kind == "result":
        future.set_result(data.data)


class Tab(BaseModel):
    _browser: Optional["Browser"] = PrivateAttr(None)
    _ws: Optional[websockets.WebSocketClientProtocol] = PrivateAttr(None)
    _auto_close: bool = PrivateAttr(True)
    _current_id: AtomicInteger = PrivateAttr(default_factory=AtomicInteger)

    description: str
    devtoolsFrontendUrl: str
    id: str
    title: str
    type: str
    url: str
    webSocketDebuggerUrl: str

    def _browser_required(self):
        if self._browser is None:
            raise RuntimeError("Tab is not attached to a browser")

    def set_auto_close(self, value: bool):
        self._auto_close = value

    def close(self):
        self._browser_required()
        url = self._browser.http_uri + "/json/close/%s" % self.id
        resp = requests.get(url)
        return resp.text == "Target is closing"

    def activate(self):
        self._browser_required()
        url = self._browser.http_uri + "/json/activate/%s" % self.id
        resp = requests.get(url)
        return resp.text == "Target activated"

    async def __aenter__(self):
        if self.activate():
            self._ws = await websockets.connect(self.webSocketDebuggerUrl).__aenter__()
            return self
        else:
            raise RuntimeError("Failed to activate tab")

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._ws.close()
        self._ws = None
        if self._auto_close:
            self.close()

    async def execute(
        self,
        method: ICommand,
        callback: Optional[
            Callable[["Payload", asyncio.Future], Awaitable[None]]
        ] = wait_for_result,
        timeout: Optional[float] = 30,
    ):
        cid = await self._current_id.increment()
        cmd = {"id": cid, **method.to_cdp()}
        body = json.dumps(cmd)
        method_name = method.get_method_name()
        logger.debug(f"[{method_name}] [{cid}] SEND >>> {cmd}")
        await self._ws.send(body)
        result = asyncio.Future()

        async def fn():
            async for msg in self._ws:
                data = Payload(json.loads(msg))
                logger.debug(f"[{method_name}] [{cid}] RECV <<< {data.data}")
                if callable(callback):
                    await callback(data, result)
                if result.done():
                    break

        task = asyncio.create_task(fn())
        try:
            async with async_timeout.timeout(timeout):
                return await result
        finally:
            task.cancel()


class Payload:
    def __init__(self, data: Union["CommandResponse", "EventResponse"]):
        self.data = data
        self.kind: Literal["result", "event"] = "result" if "id" in data else "event"


class CommandResponse(TypedDict):
    id: int
    result: dict[str, Any]


class EventResponse(TypedDict):
    method: str
    params: dict[str, Any]


ListTabAdapter = TypeAdapter(list[Tab])


class BrowserMetadata(BaseModel):
    Browser: str
    Protocol_Version: str = Field(..., alias="Protocol-Version")
    User_Agent: str = Field(..., alias="User-Agent")
    V8_Version: str = Field(..., alias="V8-Version")
    WebKit_Version: str = Field(..., alias="WebKit-Version")
    webSocketDebuggerUrl: str
