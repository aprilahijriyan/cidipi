import asyncio
import logging
from typing import cast

from cidipi.client import Browser
from cidipi.models import EventResponse, Payload, Tab
from cidipi.protocols import commands, events

logging.basicConfig(
    level=logging.DEBUG, format="[%(levelname)s] [%(name)s] %(message)s"
)
logging.getLogger("websockets.client").disabled = True


async def navigate(tab: Tab, *, url: str, wait_until: str):
    async def wait_for(data: Payload, result: asyncio.Future):
        if data.kind == "result":
            return

        cdp_event_klass = events.Page.lifecycleEvent
        cdp_event_name = cdp_event_klass.get_method_name()
        resp_data = cast(EventResponse, data.data)
        if resp_data["method"] == cdp_event_name:
            obj = cdp_event_klass(**resp_data["params"])
            if obj.name == wait_until:
                result.set_result(None)

    return await tab.execute(
        commands.Page.navigate(url=url), callback=wait_for, timeout=30
    )


async def main():
    async with Browser(headless=False, remote_port=0) as browser:

        async def run(url: str):
            async with browser.new_tab() as tab:
                await tab.execute(commands.Page.enable())
                await tab.execute(commands.Page.setLifecycleEventsEnabled(enabled=True))
                await navigate(tab, url=url, wait_until="load")

        await run("https://www.google.com")


if __name__ == "__main__":
    asyncio.run(main())
