# This an autogenerated file
# 
# Generated with CRSAxialDamping
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.crsaxialdamping import CRSAxialDampingBlueprint
from typing import Dict
from sima.riflex.crsaxialdampingitem import CRSAxialDampingItem
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class CRSAxialDamping(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    constantDamping : bool
         Damping coefficient code(default False)
    strainVelocityExponent : float
         Exponent for strain velocity(default 1.0)
    dampingCoefficient : float
         Damping coefficient (constant)(default 0.0)
    dampingCoefficientCharacteristics : List[CRSAxialDampingItem]
    """

    def __init__(self , description="", constantDamping=False, strainVelocityExponent=1.0, dampingCoefficient=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.constantDamping = constantDamping
        self.strainVelocityExponent = strainVelocityExponent
        self.dampingCoefficient = dampingCoefficient
        self.dampingCoefficientCharacteristics = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CRSAxialDampingBlueprint()


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
    def constantDamping(self) -> bool:
        """Damping coefficient code"""
        return self.__constantDamping

    @constantDamping.setter
    def constantDamping(self, value: bool):
        """Set constantDamping"""
        self.__constantDamping = bool(value)

    @property
    def strainVelocityExponent(self) -> float:
        """Exponent for strain velocity"""
        return self.__strainVelocityExponent

    @strainVelocityExponent.setter
    def strainVelocityExponent(self, value: float):
        """Set strainVelocityExponent"""
        self.__strainVelocityExponent = float(value)

    @property
    def dampingCoefficient(self) -> float:
        """Damping coefficient (constant)"""
        return self.__dampingCoefficient

    @dampingCoefficient.setter
    def dampingCoefficient(self, value: float):
        """Set dampingCoefficient"""
        self.__dampingCoefficient = float(value)

    @property
    def dampingCoefficientCharacteristics(self) -> List[CRSAxialDampingItem]:
        """"""
        return self.__dampingCoefficientCharacteristics

    @dampingCoefficientCharacteristics.setter
    def dampingCoefficientCharacteristics(self, value: List[CRSAxialDampingItem]):
        """Set dampingCoefficientCharacteristics"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__dampingCoefficientCharacteristics = value
