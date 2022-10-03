# This an autogenerated file
# 
# Generated with ScatterSector
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.scattersector import ScatterSectorBlueprint
from numpy import ndarray,asarray
from sima.metocean.scatterdimension import ScatterDimension
from sima.metocean.scatterlevelcontainer import ScatterLevelContainer
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ScatterSector(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    hsUpperLimits : ScatterDimension
    tpUpperLimits : ScatterDimension
    windScatter : ScatterLevelContainer
    currentScatter : ScatterLevelContainer
    occurrences : ndarray
    direction : float
         (default 0.0)
    """

    def __init__(self , _id="", direction=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.hsUpperLimits = None
        self.tpUpperLimits = None
        self.windScatter = None
        self.currentScatter = None
        self.occurrences = ndarray(1)
        self.direction = direction
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ScatterSectorBlueprint()


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
    def hsUpperLimits(self) -> ScatterDimension:
        """"""
        return self.__hsUpperLimits

    @hsUpperLimits.setter
    def hsUpperLimits(self, value: ScatterDimension):
        """Set hsUpperLimits"""
        self.__hsUpperLimits = value

    @property
    def tpUpperLimits(self) -> ScatterDimension:
        """"""
        return self.__tpUpperLimits

    @tpUpperLimits.setter
    def tpUpperLimits(self, value: ScatterDimension):
        """Set tpUpperLimits"""
        self.__tpUpperLimits = value

    @property
    def windScatter(self) -> ScatterLevelContainer:
        """"""
        return self.__windScatter

    @windScatter.setter
    def windScatter(self, value: ScatterLevelContainer):
        """Set windScatter"""
        self.__windScatter = value

    @property
    def currentScatter(self) -> ScatterLevelContainer:
        """"""
        return self.__currentScatter

    @currentScatter.setter
    def currentScatter(self, value: ScatterLevelContainer):
        """Set currentScatter"""
        self.__currentScatter = value

    @property
    def occurrences(self) -> ndarray:
        """"""
        return self.__occurrences

    @occurrences.setter
    def occurrences(self, value: ndarray):
        """Set occurrences"""
        self.__occurrences = asarray(value)

    @property
    def direction(self) -> float:
        """"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)
