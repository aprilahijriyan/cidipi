# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from pydantic import BaseModel, PrivateAttr

from cidipi import dom, page


class inspectNodeRequested(BaseModel):
    """
        Fired when the node should be inspected. This happens after call to `setInspectMode` or when
    user manually inspects an element.
    """

    __domain__: str = PrivateAttr("Overlay")
    backendNodeId: dom.BackendNodeId
    """
    Id of the node to inspect.
    """


class nodeHighlightRequested(BaseModel):
    """
    Fired when the node should be highlighted. This happens after call to `setInspectMode`.
    """

    __domain__: str = PrivateAttr("Overlay")
    nodeId: dom.NodeId


class screenshotRequested(BaseModel):
    """
    Fired when user asks to capture screenshot of some area on the page.
    """

    __domain__: str = PrivateAttr("Overlay")
    viewport: page.Viewport
    """
    Viewport to capture, in device independent pixels (dip).
    """


class inspectModeCanceled(BaseModel):
    """
    Fired when user cancels the inspect mode.
    """

    __domain__: str = PrivateAttr("Overlay")
