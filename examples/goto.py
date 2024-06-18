import asyncio
import logging

from cidipi.client import Browser
from cidipi.event import event_emitter
from cidipi.protocols import commands, events

logging.basicConfig(
    level=logging.DEBUG, format="[%(levelname)s] [%(name)s] %(message)s"
)


async def wait_for(event: str):
    done = asyncio.Event()
    cdp_event_klass = events.Page.lifecycleEvent
    cdp_event_name = cdp_event_klass.get_method_name()

    async def on_lifecycle_event(message: dict):
        method = message["method"]
        if method == cdp_event_name:
            obj = cdp_event_klass(**message["params"])
            if obj.name == event:
                event_emitter.remove_listener(cdp_event_name, on_lifecycle_event)
                done.set()

    event_emitter.on(cdp_event_name, on_lifecycle_event)
    await done.wait()


async def main():
    async with Browser(headless=False, remote_port=0) as browser:
        async with browser.new_tab() as tab:
            await tab.execute(commands.Page.enable())
            await tab.execute(commands.Page.setLifecycleEventsEnabled(enabled=True))
            await tab.execute(commands.Page.navigate(url="https://www.python.org"))
            await wait_for("networkIdle")
            input("Press Enter to continue...")


if __name__ == "__main__":
    asyncio.run(main())
