# This an autogenerated file
# 
# Generated with AddOperation
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.addoperation import AddOperationBlueprint
from sima.condition.modelvariationoperation import ModelVariationOperation
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima.moao import MOAO

class AddOperation(ModelVariationOperation):
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
    parent : MOAO
    children : List[MOAO]
    """

    def __init__(self , name:str="", description:str="", _id:str="", **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__parent = None
        self.__children = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AddOperationBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
        self.__children = value
