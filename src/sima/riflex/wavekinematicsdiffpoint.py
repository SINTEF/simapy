# This an autogenerated file
# 
# Generated with WaveKinematicsDiffPoint
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.wavekinematicsdiffpoint import WaveKinematicsDiffPointBlueprint
from sima.riflex.nodereference import NodeReference
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine
    from sima.hydro.diffractedwavefield import DiffractedWaveField

class WaveKinematicsDiffPoint(NodeReference):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
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
    diffractedWaveField : DiffractedWaveField
         Reference to diffracted wave point
    """

    def __init__(self , name:str="", description:str="", _id:str="", segment:int=1, allSegments:bool=False, nodeNumber:int=1, allNodes:bool=False, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__line = None
        self.__segment = segment
        self.__allSegments = allSegments
        self.__nodeNumber = nodeNumber
        self.__allNodes = allNodes
        self.__diffractedWaveField = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WaveKinematicsDiffPointBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

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
    def diffractedWaveField(self) -> DiffractedWaveField:
        """Reference to diffracted wave point"""
        return self.__diffractedWaveField

    @diffractedWaveField.setter
    def diffractedWaveField(self, value: DiffractedWaveField):
        """Set diffractedWaveField"""
        self.__diffractedWaveField = value
