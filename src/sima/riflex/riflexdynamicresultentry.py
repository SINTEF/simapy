# This an autogenerated file
# 
# Generated with RIFLEXDynamicResultEntry
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.riflexdynamicresultentry import RIFLEXDynamicResultEntryBlueprint
from typing import Dict
from .resfile import ResFile
from sima.sima import Property
from sima.sima import Result
from sima.sima import ResultEntry
from sima.sima import ScriptableValue
from sima.simo import LisFile
from sima.simo import SIMODynamicResultEntry
from sima.simo import TimeSimulationResult

class RIFLEXDynamicResultEntry(SIMODynamicResultEntry):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    properties : List[Property]
    resource : str
         (default None)
    relative : bool
         (default False)
    changeNumber : int
         (default 0)
    results : List[Result]
    entries : List[ResultEntry]
    lisFile : LisFile
    simoLDAT : Result
    timeSimulationResult : TimeSimulationResult
    riflexLDAT : Result
    resFile : ResFile
    combinedLoadingResuls : List[Result]
    outmodResuls : List[Result]
    """

    def __init__(self , description="", relative=False, changeNumber=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.properties = list()
        self.resource = None
        self.relative = relative
        self.changeNumber = changeNumber
        self.results = list()
        self.entries = list()
        self.lisFile = None
        self.simoLDAT = None
        self.timeSimulationResult = None
        self.riflexLDAT = None
        self.resFile = None
        self.combinedLoadingResuls = list()
        self.outmodResuls = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RIFLEXDynamicResultEntryBlueprint()


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
    def resource(self) -> str:
        """"""
        return self.__resource

    @resource.setter
    def resource(self, value: str):
        """Set resource"""
        self.__resource = value

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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__results = value

    @property
    def entries(self) -> List[ResultEntry]:
        """"""
        return self.__entries

    @entries.setter
    def entries(self, value: List[ResultEntry]):
        """Set entries"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__entries = value

    @property
    def lisFile(self) -> LisFile:
        """"""
        return self.__lisFile

    @lisFile.setter
    def lisFile(self, value: LisFile):
        """Set lisFile"""
        self.__lisFile = value

    @property
    def simoLDAT(self) -> Result:
        """"""
        return self.__simoLDAT

    @simoLDAT.setter
    def simoLDAT(self, value: Result):
        """Set simoLDAT"""
        self.__simoLDAT = value

    @property
    def timeSimulationResult(self) -> TimeSimulationResult:
        """"""
        return self.__timeSimulationResult

    @timeSimulationResult.setter
    def timeSimulationResult(self, value: TimeSimulationResult):
        """Set timeSimulationResult"""
        self.__timeSimulationResult = value

    @property
    def riflexLDAT(self) -> Result:
        """"""
        return self.__riflexLDAT

    @riflexLDAT.setter
    def riflexLDAT(self, value: Result):
        """Set riflexLDAT"""
        self.__riflexLDAT = value

    @property
    def resFile(self) -> ResFile:
        """"""
        return self.__resFile

    @resFile.setter
    def resFile(self, value: ResFile):
        """Set resFile"""
        self.__resFile = value

    @property
    def combinedLoadingResuls(self) -> List[Result]:
        """"""
        return self.__combinedLoadingResuls

    @combinedLoadingResuls.setter
    def combinedLoadingResuls(self, value: List[Result]):
        """Set combinedLoadingResuls"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__combinedLoadingResuls = value

    @property
    def outmodResuls(self) -> List[Result]:
        """"""
        return self.__outmodResuls

    @outmodResuls.setter
    def outmodResuls(self, value: List[Result]):
        """Set outmodResuls"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__outmodResuls = value