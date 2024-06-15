# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import *

from pydantic import BaseModel, PrivateAttr

from cidipi.dom.types import *


class attributeModified(BaseModel):
    """
    Fired when `Element`'s attribute is modified.
    """

    __domain__: str = PrivateAttr("DOM")
    nodeId: "NodeId"
    """
    Id of the node that has changed.
    """
    name: str
    """
    Attribute name.
    """
    value: str
    """
    Attribute value.
    """


class attributeRemoved(BaseModel):
    """
    Fired when `Element`'s attribute is removed.
    """

    __domain__: str = PrivateAttr("DOM")
    nodeId: "NodeId"
    """
    Id of the node that has changed.
    """
    name: str
    """
    A ttribute name.
    """


class characterDataModified(BaseModel):
    """
    Mirrors `DOMCharacterDataModified` event.
    """

    __domain__: str = PrivateAttr("DOM")
    nodeId: "NodeId"
    """
    Id of the node that has changed.
    """
    characterData: str
    """
    New text value.
    """


class childNodeCountUpdated(BaseModel):
    """
    Fired when `Container`'s child node count has changed.
    """

    __domain__: str = PrivateAttr("DOM")
    nodeId: "NodeId"
    """
    Id of the node that has changed.
    """
    childNodeCount: Union[float, int]
    """
    New node count.
    """


class childNodeInserted(BaseModel):
    """
    Mirrors `DOMNodeInserted` event.
    """

    __domain__: str = PrivateAttr("DOM")
    parentNodeId: "NodeId"
    """
    Id of the node that has changed.
    """
    previousNodeId: "NodeId"
    """
    Id of the previous sibling.
    """
    node: "Node"
    """
    Inserted node data.
    """


class childNodeRemoved(BaseModel):
    """
    Mirrors `DOMNodeRemoved` event.
    """

    __domain__: str = PrivateAttr("DOM")
    parentNodeId: "NodeId"
    """
    Parent id.
    """
    nodeId: "NodeId"
    """
    Id of the node that has been removed.
    """


class distributedNodesUpdated(BaseModel):
    """
    Called when distribution is changed.
    """

    __domain__: str = PrivateAttr("DOM")
    insertionPointId: "NodeId"
    """
    Insertion point where distributed nodes were updated.
    """
    distributedNodes: list
    """
    Distributed nodes for given insertion point.
    """


class documentUpdated(BaseModel):
    """
    Fired when `Document` has been totally updated. Node ids are no longer valid.
    """

    __domain__: str = PrivateAttr("DOM")


class inlineStyleInvalidated(BaseModel):
    """
    Fired when `Element`'s inline style is modified via a CSS property modification.
    """

    __domain__: str = PrivateAttr("DOM")
    nodeIds: list
    """
    Ids of the nodes for which the inline styles have been invalidated.
    """


class pseudoElementAdded(BaseModel):
    """
    Called when a pseudo element is added to an element.
    """

    __domain__: str = PrivateAttr("DOM")
    parentId: "NodeId"
    """
    Pseudo element's parent element id.
    """
    pseudoElement: "Node"
    """
    The added pseudo element.
    """


class topLayerElementsUpdated(BaseModel):
    """
    Called when top layer elements are changed.
    """

    __domain__: str = PrivateAttr("DOM")


class pseudoElementRemoved(BaseModel):
    """
    Called when a pseudo element is removed from an element.
    """

    __domain__: str = PrivateAttr("DOM")
    parentId: "NodeId"
    """
    Pseudo element's parent element id.
    """
    pseudoElementId: "NodeId"
    """
    The removed pseudo element id.
    """


class setChildNodes(BaseModel):
    """
        Fired when backend wants to provide client with the missing DOM structure. This happens upon
    most of the calls requesting node ids.
    """

    __domain__: str = PrivateAttr("DOM")
    parentId: "NodeId"
    """
    Parent node id to populate with children.
    """
    nodes: list
    """
    Child nodes array.
    """


class shadowRootPopped(BaseModel):
    """
    Called when shadow root is popped from the element.
    """

    __domain__: str = PrivateAttr("DOM")
    hostId: "NodeId"
    """
    Host element id.
    """
    rootId: "NodeId"
    """
    Shadow root id.
    """


class shadowRootPushed(BaseModel):
    """
    Called when shadow root is pushed into the element.
    """

    __domain__: str = PrivateAttr("DOM")
    hostId: "NodeId"
    """
    Host element id.
    """
    root: "Node"
    """
    Shadow root.
    """
