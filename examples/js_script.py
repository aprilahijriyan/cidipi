import asyncio
import logging
from typing import cast

from cidipi.client import Browser
from cidipi.models import CommandResponse
from cidipi.protocols import commands

logging.basicConfig(
    level=logging.DEBUG, format="[%(levelname)s] [%(name)s] %(message)s"
)
logging.getLogger("websockets.client").disabled = True


async def main():
    async with Browser(headless=False, remote_port=0) as browser:

        async def run(url: str):
            async with browser.new_tab() as tab:
                await tab.execute(commands.Page.enable())
                await tab.execute(commands.Page.setLifecycleEventsEnabled(enabled=True))
                script_info = await tab.execute(
                    commands.Page.addScriptToEvaluateOnNewDocument(
                        source="window.__INJECTED__ = 1;"
                    )
                )
                print("script_info:", script_info)
                await tab.execute(commands.Page.navigate(url=url))
                result = await tab.execute(
                    commands.Runtime.evaluate(expression="window.__INJECTED__")
                )
                cmd_resp = cast(CommandResponse, result)
                if cmd_resp["result"]["result"]["value"] == 1:
                    print("Matched!")
                else:
                    print("Something went wrong...")

        await run("https://www.google.com")


if __name__ == "__main__":
    asyncio.run(main())
