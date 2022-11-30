# This an autogenerated file
# 
# Generated with StaticConditionResult
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.staticconditionresult import StaticConditionResultBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.bodyresult import BodyResult

class StaticConditionResult(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    bodyResults : List[BodyResult]
    header : str
         (default None)
    dateTag : str
         (default None)
    filepart : str
         (default None)
    globalForces : bool
         (default True)
    """

    def __init__(self , description="", globalForces=True, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.bodyResults = list()
        self.header = None
        self.dateTag = None
        self.filepart = None
        self.globalForces = globalForces
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StaticConditionResultBlueprint()


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
    def bodyResults(self) -> List[BodyResult]:
        """"""
        return self.__bodyResults

    @bodyResults.setter
    def bodyResults(self, value: List[BodyResult]):
        """Set bodyResults"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__bodyResults = value

    @property
    def header(self) -> str:
        """"""
        return self.__header

    @header.setter
    def header(self, value: str):
        """Set header"""
        self.__header = value

    @property
    def dateTag(self) -> str:
        """"""
        return self.__dateTag

    @dateTag.setter
    def dateTag(self, value: str):
        """Set dateTag"""
        self.__dateTag = value

    @property
    def filepart(self) -> str:
        """"""
        return self.__filepart

    @filepart.setter
    def filepart(self, value: str):
        """Set filepart"""
        self.__filepart = value

    @property
    def globalForces(self) -> bool:
        """"""
        return self.__globalForces

    @globalForces.setter
    def globalForces(self, value: bool):
        """Set globalForces"""
        self.__globalForces = bool(value)
