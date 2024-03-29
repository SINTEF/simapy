# This an autogenerated file
# 
# Generated with MeasurementNode
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.measurementnode import MeasurementNodeBlueprint
from typing import Dict
from ..sima import ScriptableValue
from .nodereference import NodeReference
from .nodesystem import NodeSystem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .arline import ARLine

class MeasurementNode(NodeReference):
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
    nodeNumber : int
         Local node number on actual segment(default 1)
    allNodes : bool
         All nodes(default False)
    system : NodeSystem
    """

    def __init__(self , description="", segment=1, allSegments=False, nodeNumber=1, allNodes=False, system=NodeSystem.GLOBAL, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.line = None
        self.segment = segment
        self.allSegments = allSegments
        self.nodeNumber = nodeNumber
        self.allNodes = allNodes
        self.system = system
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MeasurementNodeBlueprint()


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
    def nodeNumber(self) -> int:
        """Local node number on actual segment"""
        return self.__nodeNumber

    @nodeNumber.setter
    def nodeNumber(self, value: int):
        """Set nodeNumber"""
        self.__nodeNumber = int(value)

    @property
    def allNodes(self) -> bool:
        """All nodes"""
        return self.__allNodes

    @allNodes.setter
    def allNodes(self, value: bool):
        """Set allNodes"""
        self.__allNodes = bool(value)

    @property
    def system(self) -> NodeSystem:
        """"""
        return self.__system

    @system.setter
    def system(self, value: NodeSystem):
        """Set system"""
        self.__system = value
