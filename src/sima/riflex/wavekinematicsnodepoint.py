# This an autogenerated file
# 
# Generated with WaveKinematicsNodePoint
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wavekinematicsnodepoint import WaveKinematicsNodePointBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine

class WaveKinematicsNodePoint(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    line : ARLine
         Line
    nodeStep : int
         Calculating wave kinematics for each node step value. If value is 0 there is no kinematics for this line.(default 0)
    """

    def __init__(self , _id="", nodeStep=0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.line = None
        self.nodeStep = nodeStep
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WaveKinematicsNodePointBlueprint()


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
    def nodeStep(self) -> int:
        """Calculating wave kinematics for each node step value. If value is 0 there is no kinematics for this line."""
        return self.__nodeStep

    @nodeStep.setter
    def nodeStep(self, value: int):
        """Set nodeStep"""
        self.__nodeStep = int(value)
