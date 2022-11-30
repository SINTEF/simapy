# This an autogenerated file
# 
# Generated with Requirement
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.requirement import RequirementBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class Requirement(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    attribute : str
         (default None)
    value : str
         (default None)
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.attribute = None
        self.value = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RequirementBlueprint()


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
    def attribute(self) -> str:
        """"""
        return self.__attribute

    @attribute.setter
    def attribute(self, value: str):
        """Set attribute"""
        self.__attribute = value

    @property
    def value(self) -> str:
        """"""
        return self.__value

    @value.setter
    def value(self, value: str):
        """Set value"""
        self.__value = value
