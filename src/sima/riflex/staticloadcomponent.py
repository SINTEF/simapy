# This an autogenerated file
# 
# Generated with StaticLoadComponent
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.staticloadcomponent import StaticLoadComponentBlueprint
from typing import Dict
from .segmentreference import SegmentReference
from sima.sima import ScriptableValue
from sima.simo import ReferenceFrameType
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .arline import ARLine

class StaticLoadComponent(SegmentReference):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    line : ARLine
         Line
    segment : int
         Segment on given line(default 1)
    allSegments : bool
         All segments(default False)
    node : int
         Local node number within segment (if global reference system) or element number within segment (if local reference system)(default 0)
    dof : int
         Degree of freedom within the specified node/element (1-6 for nodes, 1-6 for end 1 of an element and 7-12 for end 2 of an element)(default 0)
    magnitude : float
         Magnitude of load component(default 0.0)
    referenceFrame : ReferenceFrameType
         Reference system for application of nodal load components. If GLOBAL the force is applied at the specified node; if LOCAL the force is applied to the specified element.
    specForceIncrement : float
         Force increment on magnitude(default 0.0)
    """

    def __init__(self , description="", segment=1, allSegments=False, node=0, dof=0, magnitude=0.0, referenceFrame=ReferenceFrameType.LOCAL, specForceIncrement=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.line = None
        self.segment = segment
        self.allSegments = allSegments
        self.node = node
        self.dof = dof
        self.magnitude = magnitude
        self.referenceFrame = referenceFrame
        self.specForceIncrement = specForceIncrement
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StaticLoadComponentBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def line(self) -> ARLine:
        """Line"""
        return self.__line

    @line.setter
    def line(self, value: ARLine):
        """Set line"""
        self.__line = value

    @property
    def segment(self) -> int:
        """Segment on given line"""
        return self.__segment

    @segment.setter
    def segment(self, value: int):
        """Set segment"""
        self.__segment = int(value)

    @property
    def allSegments(self) -> bool:
        """All segments"""
        return self.__allSegments

    @allSegments.setter
    def allSegments(self, value: bool):
        """Set allSegments"""
        self.__allSegments = bool(value)

    @property
    def node(self) -> int:
        """Local node number within segment (if global reference system) or element number within segment (if local reference system)"""
        return self.__node

    @node.setter
    def node(self, value: int):
        """Set node"""
        self.__node = int(value)

    @property
    def dof(self) -> int:
        """Degree of freedom within the specified node/element (1-6 for nodes, 1-6 for end 1 of an element and 7-12 for end 2 of an element)"""
        return self.__dof

    @dof.setter
    def dof(self, value: int):
        """Set dof"""
        self.__dof = int(value)

    @property
    def magnitude(self) -> float:
        """Magnitude of load component"""
        return self.__magnitude

    @magnitude.setter
    def magnitude(self, value: float):
        """Set magnitude"""
        self.__magnitude = float(value)

    @property
    def referenceFrame(self) -> ReferenceFrameType:
        """Reference system for application of nodal load components. If GLOBAL the force is applied at the specified node; if LOCAL the force is applied to the specified element."""
        return self.__referenceFrame

    @referenceFrame.setter
    def referenceFrame(self, value: ReferenceFrameType):
        """Set referenceFrame"""
        self.__referenceFrame = value

    @property
    def specForceIncrement(self) -> float:
        """Force increment on magnitude"""
        return self.__specForceIncrement

    @specForceIncrement.setter
    def specForceIncrement(self, value: float):
        """Set specForceIncrement"""
        self.__specForceIncrement = float(value)
