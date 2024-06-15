# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from enum import Enum
from typing import Optional, TypeVar, Union

from pydantic import BaseModel

GraphObjectId = TypeVar("GraphObjectId", bound=str)
"""
An unique ID for a graph object (AudioContext, AudioNode, AudioParam) in Web Audio API
"""


class ContextType(str, Enum):
    """
    Enum of BaseAudioContext types
    """

    realtime = "realtime"
    offline = "offline"


class ContextState(str, Enum):
    """
    Enum of AudioContextState from the spec
    """

    suspended = "suspended"
    running = "running"
    closed = "closed"


NodeType = TypeVar("NodeType", bound=str)
"""
Enum of AudioNode types
"""


class ChannelCountMode(str, Enum):
    """
    Enum of AudioNode::ChannelCountMode from the spec
    """

    clamped_max = "clamped-max"
    explicit = "explicit"
    max = "max"


class ChannelInterpretation(str, Enum):
    """
    Enum of AudioNode::ChannelInterpretation from the spec
    """

    discrete = "discrete"
    speakers = "speakers"


ParamType = TypeVar("ParamType", bound=str)
"""
Enum of AudioParam types
"""


class AutomationRate(str, Enum):
    """
    Enum of AudioParam::AutomationRate from the spec
    """

    a_rate = "a-rate"
    k_rate = "k-rate"


class ContextRealtimeData(BaseModel):
    """
    Fields in AudioContext that change in real-time.
    """

    currentTime: Union[float, int]
    """
    The current context time in second in BaseAudioContext.
    """
    renderCapacity: Union[float, int]
    """
    The time spent on rendering graph divided by render quantum duration,
and multiplied by 100. 100 means the audio renderer reached the full
capacity and glitch may occur.
    """
    callbackIntervalMean: Union[float, int]
    """
    A running mean of callback interval.
    """
    callbackIntervalVariance: Union[float, int]
    """
    A running variance of callback interval.
    """


class BaseAudioContext(BaseModel):
    """
    Protocol object for BaseAudioContext
    """

    contextId: "GraphObjectId"
    contextType: "ContextType"
    contextState: "ContextState"
    realtimeData: Optional["ContextRealtimeData"]
    callbackBufferSize: Union[float, int]
    """
    Platform-dependent callback buffer size.
    """
    maxOutputChannelCount: Union[float, int]
    """
    Number of output channels supported by audio hardware in use.
    """
    sampleRate: Union[float, int]
    """
    Context sample rate.
    """


class AudioListener(BaseModel):
    """
    Protocol object for AudioListener
    """

    listenerId: "GraphObjectId"
    contextId: "GraphObjectId"


class AudioNode(BaseModel):
    """
    Protocol object for AudioNode
    """

    nodeId: "GraphObjectId"
    contextId: "GraphObjectId"
    nodeType: "NodeType"
    numberOfInputs: Union[float, int]
    numberOfOutputs: Union[float, int]
    channelCount: Union[float, int]
    channelCountMode: "ChannelCountMode"
    channelInterpretation: "ChannelInterpretation"


class AudioParam(BaseModel):
    """
    Protocol object for AudioParam
    """

    paramId: "GraphObjectId"
    nodeId: "GraphObjectId"
    contextId: "GraphObjectId"
    paramType: "ParamType"
    rate: "AutomationRate"
    defaultValue: Union[float, int]
    minValue: Union[float, int]
    maxValue: Union[float, int]