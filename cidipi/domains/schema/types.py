# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from pydantic import BaseModel


class Domain(BaseModel):
    """
    Description of the protocol domain.
    """

    name: str
    """
    Domain name.
    """
    version: str
    """
    Domain version.
    """