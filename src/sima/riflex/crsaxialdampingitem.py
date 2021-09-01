# This an autogenerated file
# 
# Generated with CRSAxialDampingItem
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.crsaxialdampingitem import CRSAxialDampingItemBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class CRSAxialDampingItem(MOAO):
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
         Damping coefficient corresponding to relative elongation.(default 0.0)
    relativeElongation : float
         Relative elongation(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", dampingCoefficient:float=0.0, relativeElongation:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__dampingCoefficient = dampingCoefficient
        self.__relativeElongation = relativeElongation
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CRSAxialDampingItemBlueprint()


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
        """Damping coefficient corresponding to relative elongation."""
        return self.__dampingCoefficient

    @dampingCoefficient.setter
    def dampingCoefficient(self, value: float):
        """Set dampingCoefficient"""
        self.__dampingCoefficient = float(value)

    @property
    def relativeElongation(self) -> float:
        """Relative elongation"""
        return self.__relativeElongation

    @relativeElongation.setter
    def relativeElongation(self, value: float):
        """Set relativeElongation"""
        self.__relativeElongation = float(value)
