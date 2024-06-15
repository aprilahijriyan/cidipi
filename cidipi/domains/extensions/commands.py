# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from pydantic import BaseModel, PrivateAttr


class loadUnpacked(BaseModel):
    """
        Installs an unpacked extension from the filesystem similar to
    --load-extension CLI flags. Returns extension ID once the extension
    has been installed.
    """

    __domain__: str = PrivateAttr("Extensions")
    path: str
    """
    Absolute file path.
    """