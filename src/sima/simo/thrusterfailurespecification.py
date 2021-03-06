# This an autogenerated file
# 
# Generated with ThrusterFailureSpecification
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.thrusterfailurespecification import ThrusterFailureSpecificationBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.thrusterfailuremode import ThrusterFailureMode

class ThrusterFailureSpecification(MOAO):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    failureMode : ThrusterFailureMode
         Thruster failure mode
    failureTime : float
         Time for thruster failure(default 0.0)
    """

    def __init__(self , name="", description="", _id="", failureMode=ThrusterFailureMode.NO_FAILURE, failureTime=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.failureMode = failureMode
        self.failureTime = failureTime
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ThrusterFailureSpecificationBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

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
    def failureMode(self) -> ThrusterFailureMode:
        """Thruster failure mode"""
        return self.__failureMode

    @failureMode.setter
    def failureMode(self, value: ThrusterFailureMode):
        """Set failureMode"""
        self.__failureMode = value

    @property
    def failureTime(self) -> float:
        """Time for thruster failure"""
        return self.__failureTime

    @failureTime.setter
    def failureTime(self, value: float):
        """Set failureTime"""
        self.__failureTime = float(value)
