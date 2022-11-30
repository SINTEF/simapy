# This an autogenerated file
# 
# Generated with DynamicNodalForceItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dynamicnodalforceitem import DynamicNodalForceItemBlueprint
from typing import Dict
from sima.riflex.coordinatesystem import CoordinateSystem
from sima.riflex.forcecomponenttype import ForceComponentType
from sima.riflex.segmentreference import SegmentReference
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine

class DynamicNodalForceItem(SegmentReference):
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
         Local node/element number within segment(default 0)
    dof : int
         Degree of freedom within the specified node/element (1-6 at node on end 1, 7-12 at node on end 2)(default 0)
    coordinateSystem : CoordinateSystem
         Coordinate system code
    forceType : ForceComponentType
         Force component type
    timeOn : float
         Time for switching component on(default 0.0)
    timeOff : float
         Time for switching component off(default 0.0)
    p1 : float
         Force component parameter 1(default 0.0)
    p2 : float
         Force component parameter 2(default 0.0)
    p3 : float
         Force component parameter 3(default 0.0)
    """

    def __init__(self , description="", segment=1, allSegments=False, node=0, dof=0, coordinateSystem=CoordinateSystem.LOCAL, forceType=ForceComponentType.CONSTANT, timeOn=0.0, timeOff=0.0, p1=0.0, p2=0.0, p3=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.line = None
        self.segment = segment
        self.allSegments = allSegments
        self.node = node
        self.dof = dof
        self.coordinateSystem = coordinateSystem
        self.forceType = forceType
        self.timeOn = timeOn
        self.timeOff = timeOff
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DynamicNodalForceItemBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
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
        """Local node/element number within segment"""
        return self.__node

    @node.setter
    def node(self, value: int):
        """Set node"""
        self.__node = int(value)

    @property
    def dof(self) -> int:
        """Degree of freedom within the specified node/element (1-6 at node on end 1, 7-12 at node on end 2)"""
        return self.__dof

    @dof.setter
    def dof(self, value: int):
        """Set dof"""
        self.__dof = int(value)

    @property
    def coordinateSystem(self) -> CoordinateSystem:
        """Coordinate system code"""
        return self.__coordinateSystem

    @coordinateSystem.setter
    def coordinateSystem(self, value: CoordinateSystem):
        """Set coordinateSystem"""
        self.__coordinateSystem = value

    @property
    def forceType(self) -> ForceComponentType:
        """Force component type"""
        return self.__forceType

    @forceType.setter
    def forceType(self, value: ForceComponentType):
        """Set forceType"""
        self.__forceType = value

    @property
    def timeOn(self) -> float:
        """Time for switching component on"""
        return self.__timeOn

    @timeOn.setter
    def timeOn(self, value: float):
        """Set timeOn"""
        self.__timeOn = float(value)

    @property
    def timeOff(self) -> float:
        """Time for switching component off"""
        return self.__timeOff

    @timeOff.setter
    def timeOff(self, value: float):
        """Set timeOff"""
        self.__timeOff = float(value)

    @property
    def p1(self) -> float:
        """Force component parameter 1"""
        return self.__p1

    @p1.setter
    def p1(self, value: float):
        """Set p1"""
        self.__p1 = float(value)

    @property
    def p2(self) -> float:
        """Force component parameter 2"""
        return self.__p2

    @p2.setter
    def p2(self, value: float):
        """Set p2"""
        self.__p2 = float(value)

    @property
    def p3(self) -> float:
        """Force component parameter 3"""
        return self.__p3

    @p3.setter
    def p3(self, value: float):
        """Set p3"""
        self.__p3 = float(value)
