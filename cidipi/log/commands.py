# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from pydantic import BaseModel, PrivateAttr


class clear(BaseModel):
    """
    Clears the log.
    """

    __domain__: str = PrivateAttr("Log")


class disable(BaseModel):
    """
    Disables log domain, prevents further log entries from being reported to the client.
    """

    __domain__: str = PrivateAttr("Log")


class enable(BaseModel):
    """
        Enables log domain, sends the entries collected so far to the client by means of the
    `entryAdded` notification.
    """

    __domain__: str = PrivateAttr("Log")


class startViolationsReport(BaseModel):
    """
    start violation reporting.
    """

    __domain__: str = PrivateAttr("Log")
    config: list
    """
    Configuration for violations.
    """


class stopViolationsReport(BaseModel):
    """
    Stop violation reporting.
    """

    __domain__: str = PrivateAttr("Log")
