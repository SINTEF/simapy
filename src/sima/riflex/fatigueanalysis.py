# This an autogenerated file
# 
# Generated with FatigueAnalysis
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fatigueanalysis import FatigueAnalysisBlueprint
from typing import Dict
from .fatigueanalysisitem import FatigueAnalysisItem
from sima.sima import Named
from sima.sima import ScriptableValue

class FatigueAnalysis(Named):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    numberOfPoints : int
         (default 8)
    includeAllPoints : bool
         Include the results from all points in output(default False)
    items : List[FatigueAnalysisItem]
         Specification of nodes for displacement storage
    specifyTimeWindow : bool
         (default False)
    startTime : float
         (default 0.0)
    endTime : float
         (default 0.0)
    """

    def __init__(self , description="", numberOfPoints=8, includeAllPoints=False, specifyTimeWindow=False, startTime=0.0, endTime=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.numberOfPoints = numberOfPoints
        self.includeAllPoints = includeAllPoints
        self.items = list()
        self.specifyTimeWindow = specifyTimeWindow
        self.startTime = startTime
        self.endTime = endTime
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FatigueAnalysisBlueprint()


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
    def numberOfPoints(self) -> int:
        """"""
        return self.__numberOfPoints

    @numberOfPoints.setter
    def numberOfPoints(self, value: int):
        """Set numberOfPoints"""
        self.__numberOfPoints = int(value)

    @property
    def includeAllPoints(self) -> bool:
        """Include the results from all points in output"""
        return self.__includeAllPoints

    @includeAllPoints.setter
    def includeAllPoints(self, value: bool):
        """Set includeAllPoints"""
        self.__includeAllPoints = bool(value)

    @property
    def items(self) -> List[FatigueAnalysisItem]:
        """Specification of nodes for displacement storage"""
        return self.__items

    @items.setter
    def items(self, value: List[FatigueAnalysisItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__items = value

    @property
    def specifyTimeWindow(self) -> bool:
        """"""
        return self.__specifyTimeWindow

    @specifyTimeWindow.setter
    def specifyTimeWindow(self, value: bool):
        """Set specifyTimeWindow"""
        self.__specifyTimeWindow = bool(value)

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
