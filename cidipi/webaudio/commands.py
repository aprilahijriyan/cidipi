# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import *

from pydantic import BaseModel, PrivateAttr

from cidipi.webaudio.types import *


class enable(BaseModel):
    """
    Enables the WebAudio domain and starts sending context lifetime events.
    """

    __domain__: str = PrivateAttr("WebAudio")


class disable(BaseModel):
    """
    Disables the WebAudio domain.
    """

    __domain__: str = PrivateAttr("WebAudio")


class getRealtimeData(BaseModel):
    """
    Fetch the realtime data from the registered contexts.
    """

    __domain__: str = PrivateAttr("WebAudio")
    contextId: "GraphObjectId"
