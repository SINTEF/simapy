# This an autogenerated file
# 
# Generated with MultiEnvironmentItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.multienvironmentitem import MultiEnvironmentItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.environment.singleenvironment import SingleEnvironment

class MultiEnvironmentItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    environment : SingleEnvironment
    startingTime : float
         Time to begin fading to this environment. Note that the new environment is not fully in effect until startingTime + ramp duration(default 0.0)
    rampDuration : float
         Duration of cosine fading from previous to new environment. It is recommended to use at least 10*peak period for the fade-in duration.(default 0.0)
    """

    def __init__(self , description="", _id=None, startingTime=0.0, rampDuration=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.environment = None
        self.startingTime = startingTime
        self.rampDuration = rampDuration
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MultiEnvironmentItemBlueprint()


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
    def environment(self) -> SingleEnvironment:
        """"""
        return self.__environment

    @environment.setter
    def environment(self, value: SingleEnvironment):
        """Set environment"""
        self.__environment = value

    @property
    def startingTime(self) -> float:
        """Time to begin fading to this environment. Note that the new environment is not fully in effect until startingTime + ramp duration"""
        return self.__startingTime

    @startingTime.setter
    def startingTime(self, value: float):
        """Set startingTime"""
        self.__startingTime = float(value)

    @property
    def rampDuration(self) -> float:
        """Duration of cosine fading from previous to new environment. It is recommended to use at least 10*peak period for the fade-in duration."""
        return self.__rampDuration

    @rampDuration.setter
    def rampDuration(self, value: float):
        """Set rampDuration"""
        self.__rampDuration = float(value)
