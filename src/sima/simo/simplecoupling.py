# This an autogenerated file
# 
# Generated with SimpleCoupling
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.simplecoupling import SimpleCouplingBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.activationfailuremode import ActivationFailureMode
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.simobodypoint import SIMOBodyPoint

class SimpleCoupling(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    endPoint1 : SIMOBodyPoint
    endPoint2 : SIMOBodyPoint
    failureMode : ActivationFailureMode
         Failure mode of coupling element
    failureTime : float
         Earliest possible time of failure(default 0.0)
    breakingStrength : float
         Breaking strength(default 0.0)
    """

    def __init__(self , description="", _id=None, name=None, failureMode=ActivationFailureMode.NONE, failureTime=0.0, breakingStrength=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.endPoint1 = None
        self.endPoint2 = None
        self.failureMode = failureMode
        self.failureTime = failureTime
        self.breakingStrength = breakingStrength
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SimpleCouplingBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def endPoint1(self) -> SIMOBodyPoint:
        """"""
        return self.__endPoint1

    @endPoint1.setter
    def endPoint1(self, value: SIMOBodyPoint):
        """Set endPoint1"""
        self.__endPoint1 = value

    @property
    def endPoint2(self) -> SIMOBodyPoint:
        """"""
        return self.__endPoint2

    @endPoint2.setter
    def endPoint2(self, value: SIMOBodyPoint):
        """Set endPoint2"""
        self.__endPoint2 = value

    @property
    def failureMode(self) -> ActivationFailureMode:
        """Failure mode of coupling element"""
        return self.__failureMode

    @failureMode.setter
    def failureMode(self, value: ActivationFailureMode):
        """Set failureMode"""
        self.__failureMode = value

    @property
    def failureTime(self) -> float:
        """Earliest possible time of failure"""
        return self.__failureTime

    @failureTime.setter
    def failureTime(self, value: float):
        """Set failureTime"""
        self.__failureTime = float(value)

    @property
    def breakingStrength(self) -> float:
        """Breaking strength"""
        return self.__breakingStrength

    @breakingStrength.setter
    def breakingStrength(self, value: float):
        """Set breakingStrength"""
        self.__breakingStrength = float(value)
