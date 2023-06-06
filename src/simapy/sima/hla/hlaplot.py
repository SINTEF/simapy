# This an autogenerated file
# 
# Generated with HLAPlot
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hlaplot import HLAPlotBlueprint
from numpy import ndarray,asarray
from ..sima import ScriptableValue
from .hlaobject import HLAObject
from .range import Range

class HLAPlot(HLAObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    curves : ndarray of str
    crossPlotXAxisValues : str
         (default None)
    minMaxX : Range
    minMaxY : Range
    axisTitleX : str
         (default None)
    axisTitleY : str
         (default None)
    valueTypeX : str
         (default None)
    showTimeMarker : bool
         (default False)
    fadePrecedingCurves : bool
         (default False)
    fadePrecedingCurvesCount : int
         (default 5)
    """

    def __init__(self , description="", showTimeMarker=False, fadePrecedingCurves=False, fadePrecedingCurvesCount=5, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.curves = []
        self.crossPlotXAxisValues = None
        self.minMaxX = None
        self.minMaxY = None
        self.axisTitleX = None
        self.axisTitleY = None
        self.valueTypeX = None
        self.showTimeMarker = showTimeMarker
        self.fadePrecedingCurves = fadePrecedingCurves
        self.fadePrecedingCurvesCount = fadePrecedingCurvesCount
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HLAPlotBlueprint()


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
    def curves(self) -> ndarray:
        """"""
        return self.__curves

    @curves.setter
    def curves(self, value: ndarray):
        """Set curves"""
        array = asarray(value, dtype=str)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__curves = array

    @property
    def crossPlotXAxisValues(self) -> str:
        """"""
        return self.__crossPlotXAxisValues

    @crossPlotXAxisValues.setter
    def crossPlotXAxisValues(self, value: str):
        """Set crossPlotXAxisValues"""
        self.__crossPlotXAxisValues = value

    @property
    def minMaxX(self) -> Range:
        """"""
        return self.__minMaxX

    @minMaxX.setter
    def minMaxX(self, value: Range):
        """Set minMaxX"""
        self.__minMaxX = value

    @property
    def minMaxY(self) -> Range:
        """"""
        return self.__minMaxY

    @minMaxY.setter
    def minMaxY(self, value: Range):
        """Set minMaxY"""
        self.__minMaxY = value

    @property
    def axisTitleX(self) -> str:
        """"""
        return self.__axisTitleX

    @axisTitleX.setter
    def axisTitleX(self, value: str):
        """Set axisTitleX"""
        self.__axisTitleX = value

    @property
    def axisTitleY(self) -> str:
        """"""
        return self.__axisTitleY

    @axisTitleY.setter
    def axisTitleY(self, value: str):
        """Set axisTitleY"""
        self.__axisTitleY = value

    @property
    def valueTypeX(self) -> str:
        """"""
        return self.__valueTypeX

    @valueTypeX.setter
    def valueTypeX(self, value: str):
        """Set valueTypeX"""
        self.__valueTypeX = value

    @property
    def showTimeMarker(self) -> bool:
        """"""
        return self.__showTimeMarker

    @showTimeMarker.setter
    def showTimeMarker(self, value: bool):
        """Set showTimeMarker"""
        self.__showTimeMarker = bool(value)

    @property
    def fadePrecedingCurves(self) -> bool:
        """"""
        return self.__fadePrecedingCurves

    @fadePrecedingCurves.setter
    def fadePrecedingCurves(self, value: bool):
        """Set fadePrecedingCurves"""
        self.__fadePrecedingCurves = bool(value)

    @property
    def fadePrecedingCurvesCount(self) -> int:
        """"""
        return self.__fadePrecedingCurvesCount

    @fadePrecedingCurvesCount.setter
    def fadePrecedingCurvesCount(self, value: int):
        """Set fadePrecedingCurvesCount"""
        self.__fadePrecedingCurvesCount = int(value)