# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from enum import Enum
from typing import Literal, Optional, TypeVar, Union

from pydantic import BaseModel

from cidipi import runtime

BreakpointId = TypeVar("BreakpointId", bound=str)
"""
Breakpoint identifier.
"""

CallFrameId = TypeVar("CallFrameId", bound=str)
"""
Call frame identifier.
"""


class Location(BaseModel):
    """
    Location in the source code.
    """

    scriptId: runtime.ScriptId
    """
    Script identifier as reported in the `Debugger.scriptParsed`.
    """
    lineNumber: Union[float, int]
    """
    Line number in the script (0-based).
    """
    columnNumber: Optional[Union[float, int]]
    """
    Column number in the script (0-based).
    """


class ScriptPosition(BaseModel):
    """
    Location in the source code.
    """

    lineNumber: Union[float, int]
    columnNumber: Union[float, int]


class LocationRange(BaseModel):
    """
    Location range within one script.
    """

    scriptId: runtime.ScriptId
    start: "ScriptPosition"
    end: "ScriptPosition"


class CallFrame(BaseModel):
    """
    JavaScript call frame. Array of call frames form the call stack.
    """

    callFrameId: "CallFrameId"
    """
    Call frame identifier. This identifier is only valid while the virtual machine is paused.
    """
    functionName: str
    """
    Name of the JavaScript function called on this call frame.
    """
    functionLocation: Optional["Location"]
    """
    Location in the source code.
    """
    location: "Location"
    """
    Location in the source code.
    """
    url: str
    """
    JavaScript script name or url.
Deprecated in favor of using the `location.scriptId` to resolve the URL via a previously
sent `Debugger.scriptParsed` event.
    """
    scopeChain: list
    """
    Scope chain for this call frame.
    """
    this: runtime.RemoteObject
    """
    `this` object for this call frame.
    """
    returnValue: Optional[runtime.RemoteObject]
    """
    The value being returned, if the function is at return point.
    """
    canBeRestarted: Optional[bool]
    """
    Valid only while the VM is paused and indicates whether this frame
can be restarted or not. Note that a `true` value here does not
guarantee that Debugger#restartFrame with this CallFrameId will be
successful, but it is very likely.
    """


class Scope(BaseModel):
    """
    Scope description.
    """

    type: Literal[
        "global",
        "local",
        "with",
        "closure",
        "catch",
        "block",
        "script",
        "eval",
        "module",
        "wasm-expression-stack",
    ]
    """
    Scope type.
    """
    object: runtime.RemoteObject
    """
    Object representing the scope. For `global` and `with` scopes it represents the actual
object; for the rest of the scopes, it is artificial transient object enumerating scope
variables as its properties.
    """
    name: Optional[str]
    startLocation: Optional["Location"]
    """
    Location in the source code where scope starts
    """
    endLocation: Optional["Location"]
    """
    Location in the source code where scope ends
    """


class SearchMatch(BaseModel):
    """
    Search match for resource.
    """

    lineNumber: Union[float, int]
    """
    Line number in resource content.
    """
    lineContent: str
    """
    Line with match content.
    """


class BreakLocation(BaseModel):
    scriptId: runtime.ScriptId
    """
    Script identifier as reported in the `Debugger.scriptParsed`.
    """
    lineNumber: Union[float, int]
    """
    Line number in the script (0-based).
    """
    columnNumber: Optional[Union[float, int]]
    """
    Column number in the script (0-based).
    """
    type: Optional[Literal["debuggerStatement", "call", "return"]]


class WasmDisassemblyChunk(BaseModel):
    lines: list
    """
    The next chunk of disassembled lines.
    """
    bytecodeOffsets: list
    """
    The bytecode offsets describing the start of each line.
    """


class ScriptLanguage(str, Enum):
    """
    Enum of possible script languages.
    """

    JavaScript = "JavaScript"
    WebAssembly = "WebAssembly"


class DebugSymbols(BaseModel):
    """
    Debug symbols available for a wasm script.
    """

    type: Literal["None", "SourceMap", "EmbeddedDWARF", "ExternalDWARF"]
    """
    Type of the debug symbols.
    """
    externalURL: Optional[str]
    """
    URL of the external symbol source.
    """
