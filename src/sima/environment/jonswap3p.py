# This an autogenerated file
# 
# Generated with Jonswap3P
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.jonswap3p import Jonswap3PBlueprint
from typing import Dict
from sima.environment.jonswap import Jonswap
from sima.environment.wavespreadingtype import WaveSpreadingType
from sima.sima.scriptablevalue import ScriptableValue

class Jonswap3P(Jonswap):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    direction : float
         Average wave propagation direction(default 0.0)
    spreadingExponent : float
         Exponent  η in cos spreading function(default 2.0)
    numDirections : int
         Number of directions in spreading function, must be odd(default 11)
    spreadingType : WaveSpreadingType
         Wave spreading code
    significantWaveHeight : float
         Significant wave height(default 0.0)
    peakPeriod : float
         Peak period, Tp(default 0.0)
    gamma : float
         Peakedness parameter, γ - calculated when not specified(default 3.3)
    """

    def __init__(self , description="", _id=None, direction=0.0, spreadingExponent=2.0, numDirections=11, spreadingType=WaveSpreadingType.UNIDIRECTIONAL, significantWaveHeight=0.0, peakPeriod=0.0, gamma=3.3, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.direction = direction
        self.spreadingExponent = spreadingExponent
        self.numDirections = numDirections
        self.spreadingType = spreadingType
        self.significantWaveHeight = significantWaveHeight
        self.peakPeriod = peakPeriod
        self.gamma = gamma
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return Jonswap3PBlueprint()


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
    def direction(self) -> float:
        """Average wave propagation direction"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def spreadingExponent(self) -> float:
        """Exponent  η in cos spreading function"""
        return self.__spreadingExponent

    @spreadingExponent.setter
    def spreadingExponent(self, value: float):
        """Set spreadingExponent"""
        self.__spreadingExponent = float(value)

    @property
    def numDirections(self) -> int:
        """Number of directions in spreading function, must be odd"""
        return self.__numDirections

    @numDirections.setter
    def numDirections(self, value: int):
        """Set numDirections"""
        self.__numDirections = int(value)

    @property
    def spreadingType(self) -> WaveSpreadingType:
        """Wave spreading code"""
        return self.__spreadingType

    @spreadingType.setter
    def spreadingType(self, value: WaveSpreadingType):
        """Set spreadingType"""
        self.__spreadingType = value

    @property
    def significantWaveHeight(self) -> float:
        """Significant wave height"""
        return self.__significantWaveHeight

    @significantWaveHeight.setter
    def significantWaveHeight(self, value: float):
        """Set significantWaveHeight"""
        self.__significantWaveHeight = float(value)

    @property
    def peakPeriod(self) -> float:
        """Peak period, Tp"""
        return self.__peakPeriod

    @peakPeriod.setter
    def peakPeriod(self, value: float):
        """Set peakPeriod"""
        self.__peakPeriod = float(value)

    @property
    def gamma(self) -> float:
        """Peakedness parameter, γ - calculated when not specified"""
        return self.__gamma

    @gamma.setter
    def gamma(self, value: float):
        """Set gamma"""
        self.__gamma = float(value)
