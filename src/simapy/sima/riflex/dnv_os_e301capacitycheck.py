# This an autogenerated file
# 
# Generated with DNV_OS_E301CapacityCheck
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dnv_os_e301capacitycheck import DNV_OS_E301CapacityCheckBlueprint
from typing import Dict
from ..post import LimitStateCategory
from ..sima import ScriptableValue
from .capacitycheck import CapacityCheck
from .elementreference import ElementReference
from .typeofunit import TypeOfUnit

class DNV_OS_E301CapacityCheck(CapacityCheck):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    limitTimeInterval : bool
         Specify time window to be applied for assessment of utilization. In case 'end time' exceeds the time series duration, the end of the time series will be used as the end time(default False)
    startTime : float
         (default 0.0)
    endTime : float
         (default 0.0)
    addIntermediateResults : bool
         Add intermediate element results to the output(default False)
    sections : List[ElementReference]
         Specification of nodes for displacement storage
    useDistributionFitting : bool
         Calculate characteristic extreme values of utilization factors using Gumbel distribution fitting(default False)
    seastateReturnPeriod : float
         Return period used for estimating the characteristic extreme value(default 3.0)
    typeOfUnit : TypeOfUnit
    limitStateCategory : LimitStateCategory
    safetyFactorOnPretension : float
         (default 0.0)
    safetyFactorOnEnvironmentTension : float
         (default 0.0)
    lastFunctionalLoadGroup : int
         Number of the last load group in static calculation parameter that is part of the functional load(default 0)
    """

    def __init__(self , description="", limitTimeInterval=False, startTime=0.0, endTime=0.0, addIntermediateResults=False, useDistributionFitting=False, seastateReturnPeriod=3.0, typeOfUnit=TypeOfUnit.PERMANENT, limitStateCategory=LimitStateCategory.ULS, safetyFactorOnPretension=0.0, safetyFactorOnEnvironmentTension=0.0, lastFunctionalLoadGroup=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.limitTimeInterval = limitTimeInterval
        self.startTime = startTime
        self.endTime = endTime
        self.addIntermediateResults = addIntermediateResults
        self.sections = list()
        self.useDistributionFitting = useDistributionFitting
        self.seastateReturnPeriod = seastateReturnPeriod
        self.typeOfUnit = typeOfUnit
        self.limitStateCategory = limitStateCategory
        self.safetyFactorOnPretension = safetyFactorOnPretension
        self.safetyFactorOnEnvironmentTension = safetyFactorOnEnvironmentTension
        self.lastFunctionalLoadGroup = lastFunctionalLoadGroup
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DNV_OS_E301CapacityCheckBlueprint()


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
    def limitTimeInterval(self) -> bool:
        """Specify time window to be applied for assessment of utilization. In case 'end time' exceeds the time series duration, the end of the time series will be used as the end time"""
        return self.__limitTimeInterval

    @limitTimeInterval.setter
    def limitTimeInterval(self, value: bool):
        """Set limitTimeInterval"""
        self.__limitTimeInterval = bool(value)

    @property
    def startTime(self) -> float:
        """"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: float):
        """Set startTime"""
        self.__startTime = float(value)

    @property
    def endTime(self) -> float:
        """"""
        return self.__endTime

    @endTime.setter
    def endTime(self, value: float):
        """Set endTime"""
        self.__endTime = float(value)

    @property
    def addIntermediateResults(self) -> bool:
        """Add intermediate element results to the output"""
        return self.__addIntermediateResults

    @addIntermediateResults.setter
    def addIntermediateResults(self, value: bool):
        """Set addIntermediateResults"""
        self.__addIntermediateResults = bool(value)

    @property
    def sections(self) -> List[ElementReference]:
        """Specification of nodes for displacement storage"""
        return self.__sections

    @sections.setter
    def sections(self, value: List[ElementReference]):
        """Set sections"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__sections = value

    @property
    def useDistributionFitting(self) -> bool:
        """Calculate characteristic extreme values of utilization factors using Gumbel distribution fitting"""
        return self.__useDistributionFitting

    @useDistributionFitting.setter
    def useDistributionFitting(self, value: bool):
        """Set useDistributionFitting"""
        self.__useDistributionFitting = bool(value)

    @property
    def seastateReturnPeriod(self) -> float:
        """Return period used for estimating the characteristic extreme value"""
        return self.__seastateReturnPeriod

    @seastateReturnPeriod.setter
    def seastateReturnPeriod(self, value: float):
        """Set seastateReturnPeriod"""
        self.__seastateReturnPeriod = float(value)

    @property
    def typeOfUnit(self) -> TypeOfUnit:
        """"""
        return self.__typeOfUnit

    @typeOfUnit.setter
    def typeOfUnit(self, value: TypeOfUnit):
        """Set typeOfUnit"""
        self.__typeOfUnit = value

    @property
    def limitStateCategory(self) -> LimitStateCategory:
        """"""
        return self.__limitStateCategory

    @limitStateCategory.setter
    def limitStateCategory(self, value: LimitStateCategory):
        """Set limitStateCategory"""
        self.__limitStateCategory = value

    @property
    def safetyFactorOnPretension(self) -> float:
        """"""
        return self.__safetyFactorOnPretension

    @safetyFactorOnPretension.setter
    def safetyFactorOnPretension(self, value: float):
        """Set safetyFactorOnPretension"""
        self.__safetyFactorOnPretension = float(value)

    @property
    def safetyFactorOnEnvironmentTension(self) -> float:
        """"""
        return self.__safetyFactorOnEnvironmentTension

    @safetyFactorOnEnvironmentTension.setter
    def safetyFactorOnEnvironmentTension(self, value: float):
        """Set safetyFactorOnEnvironmentTension"""
        self.__safetyFactorOnEnvironmentTension = float(value)

    @property
    def lastFunctionalLoadGroup(self) -> int:
        """Number of the last load group in static calculation parameter that is part of the functional load"""
        return self.__lastFunctionalLoadGroup

    @lastFunctionalLoadGroup.setter
    def lastFunctionalLoadGroup(self, value: int):
        """Set lastFunctionalLoadGroup"""
        self.__lastFunctionalLoadGroup = int(value)
