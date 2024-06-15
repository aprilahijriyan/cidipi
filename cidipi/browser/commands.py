# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import *

from pydantic import BaseModel, PrivateAttr

from cidipi import target
from cidipi.browser.types import *


class setPermission(BaseModel):
    """
    Set permission settings for given origin.
    """

    __domain__: str = PrivateAttr("Browser")
    permission: "PermissionDescriptor"
    """
    Descriptor of permission to override.
    """
    setting: "PermissionSetting"
    """
    Setting of the permission.
    """
    origin: Optional[str]
    """
    Origin the permission applies to, all origins if not specified.
    """
    browserContextId: Optional["BrowserContextID"]
    """
    Context to override. When omitted, default browser context is used.
    """


class grantPermissions(BaseModel):
    """
    Grant specific permissions to the given origin and reject all others.
    """

    __domain__: str = PrivateAttr("Browser")
    permissions: list
    origin: Optional[str]
    """
    Origin the permission applies to, all origins if not specified.
    """
    browserContextId: Optional["BrowserContextID"]
    """
    BrowserContext to override permissions. When omitted, default browser context is used.
    """


class resetPermissions(BaseModel):
    """
    Reset all permission management for all origins.
    """

    __domain__: str = PrivateAttr("Browser")
    browserContextId: Optional["BrowserContextID"]
    """
    BrowserContext to reset permissions. When omitted, default browser context is used.
    """


class setDownloadBehavior(BaseModel):
    """
    Set the behavior when downloading a file.
    """

    __domain__: str = PrivateAttr("Browser")
    behavior: Literal["deny", "allow", "allowAndName", "default"]
    """
    Whether to allow all or deny all download requests, or use default Chrome behavior if
available (otherwise deny). |allowAndName| allows download and names files according to
their download guids.
    """
    browserContextId: Optional["BrowserContextID"]
    """
    BrowserContext to set download behavior. When omitted, default browser context is used.
    """
    downloadPath: Optional[str]
    """
    The default path to save downloaded files to. This is required if behavior is set to 'allow'
or 'allowAndName'.
    """
    eventsEnabled: Optional[bool]
    """
    Whether to emit download events (defaults to false).
    """


class cancelDownload(BaseModel):
    """
    Cancel a download if in progress
    """

    __domain__: str = PrivateAttr("Browser")
    guid: str
    """
    Global unique identifier of the download.
    """
    browserContextId: Optional["BrowserContextID"]
    """
    BrowserContext to perform the action in. When omitted, default browser context is used.
    """


class close(BaseModel):
    """
    Close browser gracefully.
    """

    __domain__: str = PrivateAttr("Browser")


class crash(BaseModel):
    """
    Crashes browser on the main thread.
    """

    __domain__: str = PrivateAttr("Browser")


class crashGpuProcess(BaseModel):
    """
    Crashes GPU process.
    """

    __domain__: str = PrivateAttr("Browser")


class getVersion(BaseModel):
    """
    Returns version information.
    """

    __domain__: str = PrivateAttr("Browser")


class getBrowserCommandLine(BaseModel):
    """
        Returns the command line switches for the browser process if, and only if
    --enable-automation is on the commandline.
    """

    __domain__: str = PrivateAttr("Browser")


class getHistograms(BaseModel):
    """
    Get Chrome histograms.
    """

    __domain__: str = PrivateAttr("Browser")
    query: Optional[str]
    """
    Requested substring in name. Only histograms which have query as a
substring in their name are extracted. An empty or absent query returns
all histograms.
    """
    delta: Optional[bool]
    """
    If true, retrieve delta since last delta call.
    """


class getHistogram(BaseModel):
    """
    Get a Chrome histogram by name.
    """

    __domain__: str = PrivateAttr("Browser")
    name: str
    """
    Requested histogram name.
    """
    delta: Optional[bool]
    """
    If true, retrieve delta since last delta call.
    """


class getWindowBounds(BaseModel):
    """
    Get position and size of the browser window.
    """

    __domain__: str = PrivateAttr("Browser")
    windowId: "WindowID"
    """
    Browser window id.
    """


class getWindowForTarget(BaseModel):
    """
    Get the browser window that contains the devtools target.
    """

    __domain__: str = PrivateAttr("Browser")
    targetId: Optional[target.TargetID]
    """
    Devtools agent host id. If called as a part of the session, associated targetId is used.
    """


class setWindowBounds(BaseModel):
    """
    Set position and/or size of the browser window.
    """

    __domain__: str = PrivateAttr("Browser")
    windowId: "WindowID"
    """
    Browser window id.
    """
    bounds: "Bounds"
    """
    New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined
with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
    """


class setDockTile(BaseModel):
    """
    Set dock tile details, platform-specific.
    """

    __domain__: str = PrivateAttr("Browser")
    badgeLabel: Optional[str]
    image: Optional[str]
    """
    Png encoded image. (Encoded as a base64 string when passed over JSON)
    """


class executeBrowserCommand(BaseModel):
    """
    Invoke custom browser commands used by telemetry.
    """

    __domain__: str = PrivateAttr("Browser")
    commandId: "BrowserCommandId"


class addPrivacySandboxEnrollmentOverride(BaseModel):
    """
        Allows a site to use privacy sandbox features that require enrollment
    without the site actually being enrolled. Only supported on page targets.
    """

    __domain__: str = PrivateAttr("Browser")
    url: str
