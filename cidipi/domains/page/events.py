# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import *

from pydantic import BaseModel, PrivateAttr

from cidipi.domains import dom, network, runtime
from cidipi.domains.page.types import *


class domContentEventFired(BaseModel):
    __domain__: str = PrivateAttr("Page")
    timestamp: network.MonotonicTime


class fileChooserOpened(BaseModel):
    """
    Emitted only when `page.interceptFileChooser` is enabled.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame containing input node.
    """
    mode: Literal["selectSingle", "selectMultiple"]
    """
    Input mode.
    """
    backendNodeId: Optional[dom.BackendNodeId]
    """
    Input node id. Only present for file choosers opened via an `<input type="file">` element.
    """


class frameAttached(BaseModel):
    """
    Fired when frame has been attached to its parent.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame that has been attached.
    """
    parentFrameId: "FrameId"
    """
    Parent frame identifier.
    """
    stack: Optional[runtime.StackTrace]
    """
    JavaScript stack trace of when frame was attached, only set if frame initiated from script.
    """


class frameClearedScheduledNavigation(BaseModel):
    """
    Fired when frame no longer has a scheduled navigation.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame that has cleared its scheduled navigation.
    """


class frameDetached(BaseModel):
    """
    Fired when frame has been detached from its parent.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame that has been detached.
    """
    reason: Literal["remove", "swap"]


class frameNavigated(BaseModel):
    """
    Fired once navigation of the frame has completed. Frame is now associated with the new loader.
    """

    __domain__: str = PrivateAttr("Page")
    frame: "Frame"
    """
    Frame object.
    """
    type: "NavigationType"


class documentOpened(BaseModel):
    """
    Fired when opening document to write to.
    """

    __domain__: str = PrivateAttr("Page")
    frame: "Frame"
    """
    Frame object.
    """


class frameResized(BaseModel):
    __domain__: str = PrivateAttr("Page")


class frameRequestedNavigation(BaseModel):
    """
        Fired when a renderer-initiated navigation is requested.
    Navigation may still be cancelled after the event is issued.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame that is being navigated.
    """
    reason: "ClientNavigationReason"
    """
    The reason for the navigation.
    """
    url: str
    """
    The destination URL for the requested navigation.
    """
    disposition: "ClientNavigationDisposition"
    """
    The disposition for the navigation.
    """


class frameScheduledNavigation(BaseModel):
    """
    Fired when frame schedules a potential navigation.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame that has scheduled a navigation.
    """
    delay: Union[float, int]
    """
    Delay (in seconds) until the navigation is scheduled to begin. The navigation is not
guaranteed to start.
    """
    reason: "ClientNavigationReason"
    """
    The reason for the navigation.
    """
    url: str
    """
    The destination URL for the scheduled navigation.
    """


class frameStartedLoading(BaseModel):
    """
    Fired when frame has started loading.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame that has started loading.
    """


class frameStoppedLoading(BaseModel):
    """
    Fired when frame has stopped loading.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame that has stopped loading.
    """


class downloadWillBegin(BaseModel):
    """
        Fired when page is about to start a download.
    Deprecated. Use Browser.downloadWillBegin instead.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame that caused download to begin.
    """
    guid: str
    """
    Global unique identifier of the download.
    """
    url: str
    """
    URL of the resource being downloaded.
    """
    suggestedFilename: str
    """
    Suggested file name of the resource (the actual name of the file saved on disk may differ).
    """


class downloadProgress(BaseModel):
    """
        Fired when download makes progress. Last call has |done| == true.
    Deprecated. Use Browser.downloadProgress instead.
    """

    __domain__: str = PrivateAttr("Page")
    guid: str
    """
    Global unique identifier of the download.
    """
    totalBytes: Union[float, int]
    """
    Total expected bytes to download.
    """
    receivedBytes: Union[float, int]
    """
    Total bytes received.
    """
    state: Literal["inProgress", "completed", "canceled"]
    """
    Download status.
    """


class interstitialHidden(BaseModel):
    """
    Fired when interstitial page was hidden
    """

    __domain__: str = PrivateAttr("Page")


class interstitialShown(BaseModel):
    """
    Fired when interstitial page was shown
    """

    __domain__: str = PrivateAttr("Page")


class javascriptDialogClosed(BaseModel):
    """
        Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been
    closed.
    """

    __domain__: str = PrivateAttr("Page")
    result: bool
    """
    Whether dialog was confirmed.
    """
    userInput: str
    """
    User input in case of prompt.
    """


class javascriptDialogOpening(BaseModel):
    """
        Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to
    open.
    """

    __domain__: str = PrivateAttr("Page")
    url: str
    """
    Frame url.
    """
    message: str
    """
    Message that will be displayed by the dialog.
    """
    type: "DialogType"
    """
    Dialog type.
    """
    hasBrowserHandler: bool
    """
    True iff browser is capable showing or acting on the given dialog. When browser has no
dialog handler for given target, calling alert while Page domain is engaged will stall
the page execution. Execution can be resumed via calling Page.handleJavaScriptDialog.
    """
    defaultPrompt: Optional[str]
    """
    Default dialog prompt.
    """


class lifecycleEvent(BaseModel):
    """
    Fired for top level page lifecycle events such as navigation, load, paint, etc.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame.
    """
    loaderId: network.LoaderId
    """
    Loader identifier. Empty string if the request is fetched from worker.
    """
    name: str
    timestamp: network.MonotonicTime


class backForwardCacheNotUsed(BaseModel):
    """
        Fired for failed bfcache history navigations if BackForwardCache feature is enabled. Do
    not assume any ordering with the Page.frameNavigated event. This event is fired only for
    main-frame history navigation where the document changes (non-same-document navigations),
    when bfcache navigation fails.
    """

    __domain__: str = PrivateAttr("Page")
    loaderId: network.LoaderId
    """
    The loader id for the associated navigation.
    """
    frameId: "FrameId"
    """
    The frame id of the associated frame.
    """
    notRestoredExplanations: list
    """
    Array of reasons why the page could not be cached. This must not be empty.
    """
    notRestoredExplanationsTree: Optional["BackForwardCacheNotRestoredExplanationTree"]
    """
    Tree structure of reasons why the page could not be cached for each frame.
    """


class loadEventFired(BaseModel):
    __domain__: str = PrivateAttr("Page")
    timestamp: network.MonotonicTime


class navigatedWithinDocument(BaseModel):
    """
    Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation.
    """

    __domain__: str = PrivateAttr("Page")
    frameId: "FrameId"
    """
    Id of the frame.
    """
    url: str
    """
    Frame's new url.
    """


class screencastFrame(BaseModel):
    """
    Compressed image data requested by the `startScreencast`.
    """

    __domain__: str = PrivateAttr("Page")
    data: str
    """
    Base64-encoded compressed image. (Encoded as a base64 string when passed over JSON)
    """
    metadata: "ScreencastFrameMetadata"
    """
    Screencast frame metadata.
    """
    sessionId: Union[float, int]
    """
    Frame number.
    """


class screencastVisibilityChanged(BaseModel):
    """
    Fired when the page with currently enabled screencast was shown or hidden `.
    """

    __domain__: str = PrivateAttr("Page")
    visible: bool
    """
    True if the page is visible.
    """


class windowOpen(BaseModel):
    """
        Fired when a new window is going to be opened, via window.open(), link click, form submission,
    etc.
    """

    __domain__: str = PrivateAttr("Page")
    url: str
    """
    The URL for the new window.
    """
    windowName: str
    """
    Window name.
    """
    windowFeatures: list
    """
    An array of enabled window features.
    """
    userGesture: bool
    """
    Whether or not it was triggered by user gesture.
    """


class compilationCacheProduced(BaseModel):
    """
        Issued for every compilation cache generated. Is only available
    if Page.setGenerateCompilationCache is enabled.
    """

    __domain__: str = PrivateAttr("Page")
    url: str
    data: str
    """
    Base64-encoded data (Encoded as a base64 string when passed over JSON)
    """