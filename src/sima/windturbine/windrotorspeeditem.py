# This an autogenerated file
# 
# Generated with WindRotorSpeedItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.windrotorspeeditem import WindRotorSpeedItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class WindRotorSpeedItem(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    windSpeed : float
         Wind speed at hub(default 0.0)
    rotorSpeed : float
         Rotor speed(default 0.0)
    """

    def __init__(self , _id="", windSpeed=0.0, rotorSpeed=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.windSpeed = windSpeed
        self.rotorSpeed = rotorSpeed
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WindRotorSpeedItemBlueprint()


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
    def windSpeed(self) -> float:
        """Wind speed at hub"""
        return self.__windSpeed

    @windSpeed.setter
    def windSpeed(self, value: float):
        """Set windSpeed"""
        self.__windSpeed = float(value)

    @property
    def rotorSpeed(self) -> float:
        """Rotor speed"""
        return self.__rotorSpeed

    @rotorSpeed.setter
    def rotorSpeed(self, value: float):
        """Set rotorSpeed"""
        self.__rotorSpeed = float(value)
