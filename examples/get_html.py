import asyncio
import logging

from cidipi.client import Browser
from cidipi.protocols import commands

logging.basicConfig(
    level=logging.DEBUG, format="[%(levelname)s] [%(name)s] %(message)s"
)
logging.getLogger("websockets.client").disabled = True


async def main():
    async with Browser(headless=True, remote_port=0) as browser:

        async def run(url: str):
            async with browser.new_tab() as tab:
                await tab.execute(commands.Page.enable())
                await tab.execute(commands.DOM.enable())
                await tab.execute(commands.Page.navigate(url=url))
                await asyncio.sleep(3)
                result = await tab.execute(
                    commands.Runtime.evaluate(
                        expression="document.documentElement.outerHTML"
                    )
                )
                logging.info(result)

        await run("https://www.google.com")


if __name__ == "__main__":
    asyncio.run(main())
