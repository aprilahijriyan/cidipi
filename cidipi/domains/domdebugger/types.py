# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel

from cidipi.domains import dom, runtime


class DOMBreakpointType(str, Enum):
    """
    DOM breakpoint type.
    """

    subtree_modified = "subtree-modified"
    attribute_modified = "attribute-modified"
    node_removed = "node-removed"


class CSPViolationType(str, Enum):
    """
    CSP Violation type.
    """

    trustedtype_sink_violation = "trustedtype-sink-violation"
    trustedtype_policy_violation = "trustedtype-policy-violation"


class EventListener(BaseModel):
    """
    Object event listener.
    """

    type: str
    """
    `EventListener`'s type.
    """
    useCapture: bool
    """
    `EventListener`'s useCapture.
    """
    passive: bool
    """
    `EventListener`'s passive flag.
    """
    once: bool
    """
    `EventListener`'s once flag.
    """
    scriptId: runtime.ScriptId
    """
    Script id of the handler code.
    """
    lineNumber: Union[float, int]
    """
    Line number in the script (0-based).
    """
    columnNumber: Union[float, int]
    """
    Column number in the script (0-based).
    """
    handler: Optional[runtime.RemoteObject]
    """
    Event handler function value.
    """
    originalHandler: Optional[runtime.RemoteObject]
    """
    Event original handler function value.
    """
    backendNodeId: Optional[dom.BackendNodeId]
    """
    Node the listener is added to (if any).
    """