# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import Union

from pydantic import BaseModel, PrivateAttr


class accepted(BaseModel):
    """
    Informs that port was successfully bound and got a specified connection id.
    """

    __domain__: str = PrivateAttr("Tethering")
    port: Union[float, int]
    """
    Port number that was successfully bound.
    """
    connectionId: str
    """
    Connection id to be used.
    """