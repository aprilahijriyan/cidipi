from typing import Any, ClassVar

from pydantic import BaseModel
from pydantic.fields import ModelPrivateAttr
from typing_extensions import TypedDict


class CDPRequest(TypedDict):
    method: str
    params: dict[str, Any]


class CDP(BaseModel):
    _domain: ClassVar[ModelPrivateAttr]

    @classmethod
    def get_method_name(cls) -> str:
        return f"{cls._domain.get_default()}.{cls.__name__}"


class ICommand(CDP):
    def to_cdp(self) -> CDPRequest:
        params = self.model_dump(exclude_none=True)
        return {"method": self.get_method_name(), "params": params}


class IEvent(CDP):
    pass
