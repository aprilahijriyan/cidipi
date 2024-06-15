# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import *

from pydantic import BaseModel, PrivateAttr

from cidipi.console.types import *


class messageAdded(BaseModel):
    """
    Issued when new console message is added.
    """

    __domain__: str = PrivateAttr("Console")
    message: "ConsoleMessage"
    """
    Console message that has been added.
    """
