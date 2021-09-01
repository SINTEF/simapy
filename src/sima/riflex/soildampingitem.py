# This an autogenerated file
# 
# Generated with SoilDampingItem
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.soildampingitem import SoilDampingItemBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class SoilDampingItem(MOAO):
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
    dampingCoefficient : float
         Damping coefficient (strain dependent)(default 0.0)
    displacement : float
         Displacement(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", dampingCoefficient:float=0.0, displacement:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__dampingCoefficient = dampingCoefficient
        self.__displacement = displacement
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SoilDampingItemBlueprint()


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
    def dampingCoefficient(self) -> float:
        """Damping coefficient (strain dependent)"""
        return self.__dampingCoefficient

    @dampingCoefficient.setter
    def dampingCoefficient(self, value: float):
        """Set dampingCoefficient"""
        self.__dampingCoefficient = float(value)

    @property
    def displacement(self) -> float:
        """Displacement"""
        return self.__displacement

    @displacement.setter
    def displacement(self, value: float):
        """Set displacement"""
        self.__displacement = float(value)
