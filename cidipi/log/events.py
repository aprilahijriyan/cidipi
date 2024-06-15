# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import *

from pydantic import BaseModel, PrivateAttr

from cidipi.log.types import *


class entryAdded(BaseModel):
    """
    Issued when new message was logged.
    """

    __domain__: str = PrivateAttr("Log")
    entry: "LogEntry"
    """
    The entry.
    """
