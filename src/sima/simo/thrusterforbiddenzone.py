# This an autogenerated file
# 
# Generated with ThrusterForbiddenZone
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.thrusterforbiddenzone import ThrusterForbiddenZoneBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ThrusterForbiddenZone(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    zoneStart : float
         Start of forbidden zone of thrust force(default 0.0)
    zoneEnd : float
         End of forbidden zone of thrust force(default 0.0)
    """

    def __init__(self , _id="", zoneStart=0.0, zoneEnd=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.zoneStart = zoneStart
        self.zoneEnd = zoneEnd
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ThrusterForbiddenZoneBlueprint()


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
    def zoneStart(self) -> float:
        """Start of forbidden zone of thrust force"""
        return self.__zoneStart

    @zoneStart.setter
    def zoneStart(self, value: float):
        """Set zoneStart"""
        self.__zoneStart = float(value)

    @property
    def zoneEnd(self) -> float:
        """End of forbidden zone of thrust force"""
        return self.__zoneEnd

    @zoneEnd.setter
    def zoneEnd(self, value: float):
        """Set zoneEnd"""
        self.__zoneEnd = float(value)
