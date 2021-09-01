# This an autogenerated file
# 
# Generated with PositioningElement
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.positioningelement import PositioningElementBlueprint
from sima.sima.namedobject import NamedObject
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.activationfailuremode import ActivationFailureMode

class PositioningElement(NamedObject):
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
    localPoint : Point3
    globalPoint : Point3
    failureMode : ActivationFailureMode
         Failure mode:\n - No failure\n - Failure by exceeding the breaking strength after specified time\n - Activation of element after specified time if absolute value of force is below breaking strength
    failureTime : float
         Earliest possible time of failure(default 0.0)
    breakingStrength : float
         Breaking strength(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", failureMode:ActivationFailureMode=ActivationFailureMode.NONE, failureTime:float=0.0, breakingStrength:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__localPoint = Point3()
        self.__globalPoint = Point3()
        self.__failureMode = failureMode
        self.__failureTime = failureTime
        self.__breakingStrength = breakingStrength
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PositioningElementBlueprint()


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
    def localPoint(self) -> Point3:
        """"""
        return self.__localPoint

    @localPoint.setter
    def localPoint(self, value: Point3):
        """Set localPoint"""
        self.__localPoint = value

    @property
    def globalPoint(self) -> Point3:
        """"""
        return self.__globalPoint

    @globalPoint.setter
    def globalPoint(self, value: Point3):
        """Set globalPoint"""
        self.__globalPoint = value

    @property
    def failureMode(self) -> ActivationFailureMode:
        """Failure mode:
 - No failure
 - Failure by exceeding the breaking strength after specified time
 - Activation of element after specified time if absolute value of force is below breaking strength"""
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
