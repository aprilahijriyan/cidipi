# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import Optional, TypeVar

from pydantic import BaseModel

SerializedStorageKey = TypeVar("SerializedStorageKey", bound=str)


class StorageId(BaseModel):
    """
    DOM Storage identifier.
    """

    securityOrigin: Optional[str]
    """
    Security origin for the storage.
    """
    storageKey: Optional["SerializedStorageKey"]
    """
    Represents a key by which DOM Storage keys its CachedStorageAreas
    """
    isLocalStorage: bool
    """
    Whether the storage is local storage (not session storage).
    """


Item = TypeVar("Item", bound=list)
"""
DOM Storage item.
"""
