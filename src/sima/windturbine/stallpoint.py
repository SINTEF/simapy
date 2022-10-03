# This an autogenerated file
# 
# Generated with StallPoint
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.stallpoint import StallPointBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class StallPoint(MOAO):
    """
    Keyword arguments
    -----------------
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

    def __init__(self , _id="", angleZeroLift=0.0, maxLinearClSlopePos=0.0, maxLinearClSlopeNeg=0.0, angleFullSeparationPos=0.0, angleFullSeparationNeg=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.angleZeroLift = angleZeroLift
        self.maxLinearClSlopePos = maxLinearClSlopePos
        self.maxLinearClSlopeNeg = maxLinearClSlopeNeg
        self.angleFullSeparationPos = angleFullSeparationPos
        self.angleFullSeparationNeg = angleFullSeparationNeg
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StallPointBlueprint()


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
