import logging

from pyee import AsyncIOEventEmitter

logger = logging.getLogger(__name__)
event_emitter = AsyncIOEventEmitter()


@event_emitter.on("event")
async def on_event(message):
    logger.debug(f"on_event: {message}")
    event_name = message["method"]
    event_emitter.emit(event_name, message)


@event_emitter.on("result")
async def on_result(message):
    logger.debug(f"on_result: {message}")
