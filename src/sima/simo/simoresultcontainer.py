# This an autogenerated file
# 
# Generated with SIMOResultContainer
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.simoresultcontainer import SIMOResultContainerBlueprint
from typing import Dict
from sima.sima.conditionresultcontainer import ConditionResultContainer
from sima.sima.property import Property
from sima.sima.resultentry import ResultEntry
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.simodynamicresultentry import SIMODynamicResultEntry
from sima.simo.simostaticresultentry import SIMOStaticResultEntry

class SIMOResultContainer(ConditionResultContainer):
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
    modelOutputFile : str
         (default "")
    probability : float
         (default 0.0)
    static : SIMOStaticResultEntry
    dynamic : SIMODynamicResultEntry
    stability : ResultEntry
    preRunResults : ResultEntry
    """

    def __init__(self , name="", description="", _id="", modelOutputFile="", probability=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.properties = list()
        self.modelOutputFile = modelOutputFile
        self.probability = probability
        self.static = None
        self.dynamic = None
        self.stability = None
        self.preRunResults = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SIMOResultContainerBlueprint()


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
    def modelOutputFile(self) -> str:
        """"""
        return self.__modelOutputFile

    @modelOutputFile.setter
    def modelOutputFile(self, value: str):
        """Set modelOutputFile"""
        self.__modelOutputFile = str(value)

    @property
    def probability(self) -> float:
        """"""
        return self.__probability

    @probability.setter
    def probability(self, value: float):
        """Set probability"""
        self.__probability = float(value)

    @property
    def static(self) -> SIMOStaticResultEntry:
        """"""
        return self.__static

    @static.setter
    def static(self, value: SIMOStaticResultEntry):
        """Set static"""
        self.__static = value

    @property
    def dynamic(self) -> SIMODynamicResultEntry:
        """"""
        return self.__dynamic

    @dynamic.setter
    def dynamic(self, value: SIMODynamicResultEntry):
        """Set dynamic"""
        self.__dynamic = value

    @property
    def stability(self) -> ResultEntry:
        """"""
        return self.__stability

    @stability.setter
    def stability(self, value: ResultEntry):
        """Set stability"""
        self.__stability = value

    @property
    def preRunResults(self) -> ResultEntry:
        """"""
        return self.__preRunResults

    @preRunResults.setter
    def preRunResults(self, value: ResultEntry):
        """Set preRunResults"""
        self.__preRunResults = value
