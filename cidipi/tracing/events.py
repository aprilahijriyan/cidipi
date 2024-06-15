# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import *

from pydantic import BaseModel, PrivateAttr

from cidipi import io
from cidipi.tracing.types import *


class bufferUsage(BaseModel):
    __domain__: str = PrivateAttr("Tracing")
    percentFull: Optional[Union[float, int]]
    """
    A number in range [0..1] that indicates the used size of event buffer as a fraction of its
total size.
    """
    eventCount: Optional[Union[float, int]]
    """
    An approximate number of events in the trace log.
    """
    value: Optional[Union[float, int]]
    """
    A number in range [0..1] that indicates the used size of event buffer as a fraction of its
total size.
    """


class dataCollected(BaseModel):
    """
        Contains a bucket of collected trace events. When tracing is stopped collected events will be
    sent as a sequence of dataCollected events followed by tracingComplete event.
    """

    __domain__: str = PrivateAttr("Tracing")
    value: list


class tracingComplete(BaseModel):
    """
        Signals that tracing is stopped and there is no trace buffers pending flush, all data were
    delivered via dataCollected events.
    """

    __domain__: str = PrivateAttr("Tracing")
    dataLossOccurred: bool
    """
    Indicates whether some trace data is known to have been lost, e.g. because the trace ring
buffer wrapped around.
    """
    stream: Optional[io.StreamHandle]
    """
    A handle of the stream that holds resulting trace data.
    """
    traceFormat: Optional["StreamFormat"]
    """
    Trace data format of returned stream.
    """
    streamCompression: Optional["StreamCompression"]
    """
    Compression format of returned stream.
    """
