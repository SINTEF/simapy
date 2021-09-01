# This an autogenerated file
# 
# Generated with CurrentVariationItem
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.currentvariationitem import CurrentVariationItemBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class CurrentVariationItem(MOAO):
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
    velocityIncrement : float
         Current velocity increment(default 0.0)
    directionIncrement : float
         Current direction increment(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", velocityIncrement:float=0.0, directionIncrement:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__velocityIncrement = velocityIncrement
        self.__directionIncrement = directionIncrement
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CurrentVariationItemBlueprint()


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
    def velocityIncrement(self) -> float:
        """Current velocity increment"""
        return self.__velocityIncrement

    @velocityIncrement.setter
    def velocityIncrement(self, value: float):
        """Set velocityIncrement"""
        self.__velocityIncrement = float(value)

    @property
    def directionIncrement(self) -> float:
        """Current direction increment"""
        return self.__directionIncrement

    @directionIncrement.setter
    def directionIncrement(self, value: float):
        """Set directionIncrement"""
        self.__directionIncrement = float(value)
