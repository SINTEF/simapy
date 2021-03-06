# This an autogenerated file
# 
# Generated with PhysicalConstants
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.physicalconstants import PhysicalConstantsBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class PhysicalConstants(MOAO):
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
    waterDensity : float
         Water density - rho water(default 1025.0)
    accOfGravity : float
         Acceleration of gravity - g(default 9.81)
    """

    def __init__(self , name="", description="", _id="", waterDensity=1025.0, accOfGravity=9.81, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.waterDensity = waterDensity
        self.accOfGravity = accOfGravity
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PhysicalConstantsBlueprint()


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
    def waterDensity(self) -> float:
        """Water density - rho water"""
        return self.__waterDensity

    @waterDensity.setter
    def waterDensity(self, value: float):
        """Set waterDensity"""
        self.__waterDensity = float(value)

    @property
    def accOfGravity(self) -> float:
        """Acceleration of gravity - g"""
        return self.__accOfGravity

    @accOfGravity.setter
    def accOfGravity(self, value: float):
        """Set accOfGravity"""
        self.__accOfGravity = float(value)
