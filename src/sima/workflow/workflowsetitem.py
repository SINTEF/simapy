# This an autogenerated file
# 
# Generated with WorkflowSetItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.workflowsetitem import WorkflowSetItemBlueprint
from numpy import ndarray,asarray
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class WorkflowSetItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    parameterId : str
         (default None)
    values : ndarray
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.parameterId = None
        self.values = ndarray(1)
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WorkflowSetItemBlueprint()


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
    def parameterId(self) -> str:
        """"""
        return self.__parameterId

    @parameterId.setter
    def parameterId(self, value: str):
        """Set parameterId"""
        self.__parameterId = value

    @property
    def values(self) -> ndarray:
        """"""
        return self.__values

    @values.setter
    def values(self, value: ndarray):
        """Set values"""
        self.__values = asarray(value)
