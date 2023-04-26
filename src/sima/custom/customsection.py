# This an autogenerated file
# 
# Generated with CustomSection
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.customsection import CustomSectionBlueprint
from typing import Dict
from .customcomponent import CustomComponent
from sima.sima import ScriptableValue

class CustomSection(CustomComponent):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    children : List[CustomComponent]
    title : str
         (default None)
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.children = list()
        self.title = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomSectionBlueprint()


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
    def children(self) -> List[CustomComponent]:
        """"""
        return self.__children

    @children.setter
    def children(self, value: List[CustomComponent]):
        """Set children"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__children = value

    @property
    def title(self) -> str:
        """"""
        return self.__title

    @title.setter
    def title(self, value: str):
        """Set title"""
        self.__title = value