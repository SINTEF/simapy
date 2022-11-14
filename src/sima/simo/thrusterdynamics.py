# This an autogenerated file
# 
# Generated with ThrusterDynamics
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.thrusterdynamics import ThrusterDynamicsBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ThrusterDynamics(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    minTimeChange : float
         Minimum time to change from 10% to 90% of maximum thrust(default 0.0)
    tcThrust : float
         Time constant of thrust(default 0.0)
    maxRevolvingSpeed : float
         Maximum revolving speed(default 10.0)
    tcAzimuth : float
         Time constant of azimuth change(default 0.0)
    """

    def __init__(self , description="", _id=None, minTimeChange=0.0, tcThrust=0.0, maxRevolvingSpeed=10.0, tcAzimuth=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.minTimeChange = minTimeChange
        self.tcThrust = tcThrust
        self.maxRevolvingSpeed = maxRevolvingSpeed
        self.tcAzimuth = tcAzimuth
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ThrusterDynamicsBlueprint()


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
    def minTimeChange(self) -> float:
        """Minimum time to change from 10% to 90% of maximum thrust"""
        return self.__minTimeChange

    @minTimeChange.setter
    def minTimeChange(self, value: float):
        """Set minTimeChange"""
        self.__minTimeChange = float(value)

    @property
    def tcThrust(self) -> float:
        """Time constant of thrust"""
        return self.__tcThrust

    @tcThrust.setter
    def tcThrust(self, value: float):
        """Set tcThrust"""
        self.__tcThrust = float(value)

    @property
    def maxRevolvingSpeed(self) -> float:
        """Maximum revolving speed"""
        return self.__maxRevolvingSpeed

    @maxRevolvingSpeed.setter
    def maxRevolvingSpeed(self, value: float):
        """Set maxRevolvingSpeed"""
        self.__maxRevolvingSpeed = float(value)

    @property
    def tcAzimuth(self) -> float:
        """Time constant of azimuth change"""
        return self.__tcAzimuth

    @tcAzimuth.setter
    def tcAzimuth(self, value: float):
        """Set tcAzimuth"""
        self.__tcAzimuth = float(value)
