# This an autogenerated file
# 
# Generated with WaveTimeSeries
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wavetimeseries import WaveTimeSeriesBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class WaveTimeSeries(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    scaleFactor : float
         Wave scale factor(default 1.0)
    refPointX : float
         Reference point X(default 0.0)
    refPointY : float
         Reference point Y(default 0.0)
    waterDepth : float
         Water depth in FULL scale(default 0.0)
    fileName : str
         (default None)
    filterInputTimeseries : bool
         Apply filtering to the wave signal(default True)
    specifyLowerPeriod : bool
         Override default computation of lower cut off period(default False)
    lowerCutOffPeriod : float
         Lower cut off period for filtering of wave signal(default 0.0)
    upperCutOffPeriod : float
         Upper cut off period for filtering of wave signal(default 40.0)
    """

    def __init__(self , description="", _id=None, scaleFactor=1.0, refPointX=0.0, refPointY=0.0, waterDepth=0.0, fileName=None, filterInputTimeseries=True, specifyLowerPeriod=False, lowerCutOffPeriod=0.0, upperCutOffPeriod=40.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.scaleFactor = scaleFactor
        self.refPointX = refPointX
        self.refPointY = refPointY
        self.waterDepth = waterDepth
        self.fileName = fileName
        self.filterInputTimeseries = filterInputTimeseries
        self.specifyLowerPeriod = specifyLowerPeriod
        self.lowerCutOffPeriod = lowerCutOffPeriod
        self.upperCutOffPeriod = upperCutOffPeriod
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WaveTimeSeriesBlueprint()


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
    def scaleFactor(self) -> float:
        """Wave scale factor"""
        return self.__scaleFactor

    @scaleFactor.setter
    def scaleFactor(self, value: float):
        """Set scaleFactor"""
        self.__scaleFactor = float(value)

    @property
    def refPointX(self) -> float:
        """Reference point X"""
        return self.__refPointX

    @refPointX.setter
    def refPointX(self, value: float):
        """Set refPointX"""
        self.__refPointX = float(value)

    @property
    def refPointY(self) -> float:
        """Reference point Y"""
        return self.__refPointY

    @refPointY.setter
    def refPointY(self, value: float):
        """Set refPointY"""
        self.__refPointY = float(value)

    @property
    def waterDepth(self) -> float:
        """Water depth in FULL scale"""
        return self.__waterDepth

    @waterDepth.setter
    def waterDepth(self, value: float):
        """Set waterDepth"""
        self.__waterDepth = float(value)

    @property
    def fileName(self) -> str:
        """"""
        return self.__fileName

    @fileName.setter
    def fileName(self, value: str):
        """Set fileName"""
        self.__fileName = str(value)

    @property
    def filterInputTimeseries(self) -> bool:
        """Apply filtering to the wave signal"""
        return self.__filterInputTimeseries

    @filterInputTimeseries.setter
    def filterInputTimeseries(self, value: bool):
        """Set filterInputTimeseries"""
        self.__filterInputTimeseries = bool(value)

    @property
    def specifyLowerPeriod(self) -> bool:
        """Override default computation of lower cut off period"""
        return self.__specifyLowerPeriod

    @specifyLowerPeriod.setter
    def specifyLowerPeriod(self, value: bool):
        """Set specifyLowerPeriod"""
        self.__specifyLowerPeriod = bool(value)

    @property
    def lowerCutOffPeriod(self) -> float:
        """Lower cut off period for filtering of wave signal"""
        return self.__lowerCutOffPeriod

    @lowerCutOffPeriod.setter
    def lowerCutOffPeriod(self, value: float):
        """Set lowerCutOffPeriod"""
        self.__lowerCutOffPeriod = float(value)

    @property
    def upperCutOffPeriod(self) -> float:
        """Upper cut off period for filtering of wave signal"""
        return self.__upperCutOffPeriod

    @upperCutOffPeriod.setter
    def upperCutOffPeriod(self, value: float):
        """Set upperCutOffPeriod"""
        self.__upperCutOffPeriod = float(value)
