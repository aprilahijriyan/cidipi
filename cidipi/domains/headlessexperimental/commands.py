# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import *

from pydantic import BaseModel, PrivateAttr

from cidipi.domains.headlessexperimental.types import *


class beginFrame(BaseModel):
    """
        Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a
    screenshot from the resulting frame. Requires that the target was created with enabled
    BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also
    https://goo.gle/chrome-headless-rendering for more background.
    """

    __domain__: str = PrivateAttr("HeadlessExperimental")
    frameTimeTicks: Optional[Union[float, int]]
    """
    Timestamp of this BeginFrame in Renderer TimeTicks (milliseconds of uptime). If not set,
the current time will be used.
    """
    interval: Optional[Union[float, int]]
    """
    The interval between BeginFrames that is reported to the compositor, in milliseconds.
Defaults to a 60 frames/second interval, i.e. about 16.666 milliseconds.
    """
    noDisplayUpdates: Optional[bool]
    """
    Whether updates should not be committed and drawn onto the display. False by default. If
true, only side effects of the BeginFrame will be run, such as layout and animations, but
any visual updates may not be visible on the display or in screenshots.
    """
    screenshot: Optional["ScreenshotParams"]
    """
    If set, a screenshot of the frame will be captured and returned in the response. Otherwise,
no screenshot will be captured. Note that capturing a screenshot can fail, for example,
during renderer initialization. In such a case, no screenshot data will be returned.
    """


class disable(BaseModel):
    """
    Disables headless events for the target.
    """

    __domain__: str = PrivateAttr("HeadlessExperimental")


class enable(BaseModel):
    """
    Enables headless events for the target.
    """

    __domain__: str = PrivateAttr("HeadlessExperimental")