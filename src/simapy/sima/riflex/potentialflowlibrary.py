# This an autogenerated file
# 
# Generated with PotentialFlowLibrary
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.potentialflowlibrary import PotentialFlowLibraryBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .elementreference import ElementReference

class PotentialFlowLibrary(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    file : str
         Potential flow library file(default None)
    elements : List[ElementReference]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.file = None
        self.elements = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PotentialFlowLibraryBlueprint()


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
    def file(self) -> str:
        """Potential flow library file"""
        return self.__file

    @file.setter
    def file(self, value: str):
        """Set file"""
        self.__file = value

    @property
    def elements(self) -> List[ElementReference]:
        """"""
        return self.__elements

    @elements.setter
    def elements(self, value: List[ElementReference]):
        """Set elements"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__elements = value
