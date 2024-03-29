# This an autogenerated file
# 
# Generated with AddOperation
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.addoperation import AddOperationBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .modelvariationoperation import ModelVariationOperation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..sima import MOAO

class AddOperation(ModelVariationOperation):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    parent : MOAO
    children : List[MOAO]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.parent = None
        self.children = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AddOperationBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def parent(self) -> MOAO:
        """"""
        return self.__parent

    @parent.setter
    def parent(self, value: MOAO):
        """Set parent"""
        self.__parent = value

    @property
    def children(self) -> List[MOAO]:
        """"""
        return self.__children

    @children.setter
    def children(self, value: List[MOAO]):
        """Set children"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__children = value
