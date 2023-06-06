# This an autogenerated file
# 
# Generated with ConditionSetResultContainer
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.conditionsetresultcontainer import ConditionSetResultContainerBlueprint
from typing import Dict
from ..sima import ConditionResultContainer
from ..sima import Property
from ..sima import ResultContainer
from ..sima import ScriptableValue

class ConditionSetResultContainer(ResultContainer):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    properties : List[Property]
    resultContainers : List[ConditionResultContainer]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.properties = list()
        self.resultContainers = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ConditionSetResultContainerBlueprint()


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
    def properties(self) -> List[Property]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[Property]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__properties = value

    @property
    def resultContainers(self) -> List[ConditionResultContainer]:
        """"""
        return self.__resultContainers

    @resultContainers.setter
    def resultContainers(self, value: List[ConditionResultContainer]):
        """Set resultContainers"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__resultContainers = value
