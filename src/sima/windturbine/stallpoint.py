# This an autogenerated file
# 
# Generated with StallPoint
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.stallpoint import StallPointBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class StallPoint(MOAO):
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
    angleZeroLift : float
         Angle of attack at zero lift (Typical value: -2 deg)(default 0.0)
    maxLinearClSlopePos : float
         Max linear CL slope (positive) (Typical value: 0.12/deg)(default 0.0)
    maxLinearClSlopeNeg : float
         Max linear CL slope (negative) (Typical value: 0.12/deg)(default 0.0)
    angleFullSeparationPos : float
         Angle of attack at full separation (positive) (Typical value: 20 deg)(default 0.0)
    angleFullSeparationNeg : float
         Angle of attack at full separation (negative) (Typical value: -20 deg)(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", angleZeroLift:float=0.0, maxLinearClSlopePos:float=0.0, maxLinearClSlopeNeg:float=0.0, angleFullSeparationPos:float=0.0, angleFullSeparationNeg:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__angleZeroLift = angleZeroLift
        self.__maxLinearClSlopePos = maxLinearClSlopePos
        self.__maxLinearClSlopeNeg = maxLinearClSlopeNeg
        self.__angleFullSeparationPos = angleFullSeparationPos
        self.__angleFullSeparationNeg = angleFullSeparationNeg
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StallPointBlueprint()


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
    def angleZeroLift(self) -> float:
        """Angle of attack at zero lift (Typical value: -2 deg)"""
        return self.__angleZeroLift

    @angleZeroLift.setter
    def angleZeroLift(self, value: float):
        """Set angleZeroLift"""
        self.__angleZeroLift = float(value)

    @property
    def maxLinearClSlopePos(self) -> float:
        """Max linear CL slope (positive) (Typical value: 0.12/deg)"""
        return self.__maxLinearClSlopePos

    @maxLinearClSlopePos.setter
    def maxLinearClSlopePos(self, value: float):
        """Set maxLinearClSlopePos"""
        self.__maxLinearClSlopePos = float(value)

    @property
    def maxLinearClSlopeNeg(self) -> float:
        """Max linear CL slope (negative) (Typical value: 0.12/deg)"""
        return self.__maxLinearClSlopeNeg

    @maxLinearClSlopeNeg.setter
    def maxLinearClSlopeNeg(self, value: float):
        """Set maxLinearClSlopeNeg"""
        self.__maxLinearClSlopeNeg = float(value)

    @property
    def angleFullSeparationPos(self) -> float:
        """Angle of attack at full separation (positive) (Typical value: 20 deg)"""
        return self.__angleFullSeparationPos

    @angleFullSeparationPos.setter
    def angleFullSeparationPos(self, value: float):
        """Set angleFullSeparationPos"""
        self.__angleFullSeparationPos = float(value)

    @property
    def angleFullSeparationNeg(self) -> float:
        """Angle of attack at full separation (negative) (Typical value: -20 deg)"""
        return self.__angleFullSeparationNeg

    @angleFullSeparationNeg.setter
    def angleFullSeparationNeg(self, value: float):
        """Set angleFullSeparationNeg"""
        self.__angleFullSeparationNeg = float(value)
