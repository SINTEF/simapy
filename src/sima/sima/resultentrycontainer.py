# This an autogenerated file
# 
# Generated with ResultEntryContainer
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.resultentrycontainer import ResultEntryContainerBlueprint
from sima.sima.property import Property
from sima.sima.result import Result
from sima.sima.resultcontainer import ResultContainer
from sima.sima.resultentry import ResultEntry
from sima.sima.scriptablevalue import ScriptableValue

class ResultEntryContainer(ResultContainer,ResultEntry):
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
    properties : List[Property]
    resource : str
         (default "")
    relative : bool
         (default False)
    changeNumber : int
         (default 0)
    results : List[Result]
    entries : List[ResultEntry]
    """

    def __init__(self , name:str="", description:str="", _id:str="", resource:str="", relative:bool=False, changeNumber:int=0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__properties = list()
        self.__resource = resource
        self.__relative = relative
        self.__changeNumber = changeNumber
        self.__results = list()
        self.__entries = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ResultEntryContainerBlueprint()


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
    def properties(self) -> List[Property]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[Property]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__properties = value

    @property
    def resource(self) -> str:
        """"""
        return self.__resource

    @resource.setter
    def resource(self, value: str):
        """Set resource"""
        self.__resource = str(value)

    @property
    def relative(self) -> bool:
        """"""
        return self.__relative

    @relative.setter
    def relative(self, value: bool):
        """Set relative"""
        self.__relative = bool(value)

    @property
    def changeNumber(self) -> int:
        """"""
        return self.__changeNumber

    @changeNumber.setter
    def changeNumber(self, value: int):
        """Set changeNumber"""
        self.__changeNumber = int(value)

    @property
    def results(self) -> List[Result]:
        """"""
        return self.__results

    @results.setter
    def results(self, value: List[Result]):
        """Set results"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__results = value

    @property
    def entries(self) -> List[ResultEntry]:
        """"""
        return self.__entries

    @entries.setter
    def entries(self, value: List[ResultEntry]):
        """Set entries"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__entries = value
