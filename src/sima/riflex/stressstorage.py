# This an autogenerated file
# 
# Generated with StressStorage
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.stressstorage import StressStorageBlueprint
from typing import Dict
from .elementstressstorage import ElementStressStorage
from sima.sima import MOAO
from sima.sima import ScriptableValue

class StressStorage(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    elements : List[ElementStressStorage]
         Specification of nodes for displacement storage
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.elements = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StressStorageBlueprint()


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
    def elements(self) -> List[ElementStressStorage]:
        """Specification of nodes for displacement storage"""
        return self.__elements

    @elements.setter
    def elements(self, value: List[ElementStressStorage]):
        """Set elements"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__elements = value
