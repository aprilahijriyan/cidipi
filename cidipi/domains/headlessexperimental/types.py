# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import Literal, Optional, Union

from pydantic import BaseModel


class ScreenshotParams(BaseModel):
    """
    Encoding options for a screenshot.
    """

    format: Optional[Literal["jpeg", "png", "webp"]]
    """
    Image compression format (defaults to png).
    """
    quality: Optional[Union[float, int]]
    """
    Compression quality from range [0..100] (jpeg and webp only).
    """
    optimizeForSpeed: Optional[bool]
    """
    Optimize image encoding for speed, not for resulting size (defaults to false)
    """