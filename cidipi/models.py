from __future__ import annotations

import asyncio
import json
import logging
from typing import TYPE_CHECKING, Optional

import websockets
from curl_cffi import requests
from pydantic import BaseModel, Field, PrivateAttr, TypeAdapter

from cidipi.event import event_emitter
from cidipi.interface import ICommand
from cidipi.utils import AtomicInteger

if TYPE_CHECKING:
    from cidipi.client import Browser

logger = logging.getLogger(__name__)


class Tab(BaseModel):
    _browser: Optional["Browser"] = PrivateAttr(None)
    _ws: Optional[websockets.WebSocketClientProtocol] = PrivateAttr(None)
    _auto_close: bool = PrivateAttr(True)
    _stop_listening: Optional[asyncio.Event] = PrivateAttr(None)
    _futures: dict[int, asyncio.Future] = PrivateAttr({})
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
            await self.listen()
            return self
        else:
            raise RuntimeError("Failed to activate tab")

    async def listen(self):
        if self._ws is None:
            raise RuntimeError("Tab is not attached to a browser")

        self._stop_listening = asyncio.Event()
        is_running = asyncio.Event()

        async def fn():
            is_running.set()
            async for msg in self._ws:
                data = json.loads(msg)
                await self.on_message(data)
                if self._stop_listening.is_set():
                    break

        asyncio.create_task(fn())
        await is_running.wait()

    async def on_message(self, msg):
        if "id" in msg:
            # command result
            if msg["id"] in self._futures:
                fut = self._futures.pop(msg["id"])
                fut.set_result(msg)

            event_emitter.emit("result", msg)
        else:
            # event result
            event_emitter.emit("event", msg)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._stop_listening.set()
        await self._ws.close()
        self._ws = None
        if self._auto_close:
            self.close()

    async def execute(self, method: ICommand):
        cid = await self._current_id.increment()
        cmd = {"id": cid, **method.to_cdp()}
        body = json.dumps(cmd)
        logger.debug(f"[{method.get_method_name()}] [{cid}] SEND >>> {body}")
        fut = asyncio.Future()
        self._futures[cid] = fut
        await self._ws.send(body)
        return await fut


ListTabAdapter = TypeAdapter(list[Tab])


class BrowserMetadata(BaseModel):
    Browser: str
    Protocol_Version: str = Field(..., alias="Protocol-Version")
    User_Agent: str = Field(..., alias="User-Agent")
    V8_Version: str = Field(..., alias="V8-Version")
    WebKit_Version: str = Field(..., alias="WebKit-Version")
    webSocketDebuggerUrl: str
