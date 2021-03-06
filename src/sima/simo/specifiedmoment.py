# This an autogenerated file
# 
# Generated with SpecifiedMoment
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.specifiedmoment import SpecifiedMomentBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.vector3 import Vector3
from sima.simo.referenceframetype import ReferenceFrameType
from sima.simo.specifiedloadtype import SpecifiedLoadType

class SpecifiedMoment(NamedObject):
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
    referenceFrame : ReferenceFrameType
         Direction vector in local or global coordinate system
    directionVector : Vector3
    activationTime : float
         Time for switching component on(default 0.0)
    deactivationTime : float
         Time for switching component off(default 100000.0)
    loadType : SpecifiedLoadType
    period : float
         (default 0.0)
    phase : float
         (default 0.0)
    magnitude : float
         Moment component magnitude parameter(default 0.0)
    momentDerivative : float
         Moment component moment derivative parameter(default 0.0)
    """

    def __init__(self , name="", description="", _id="", referenceFrame=ReferenceFrameType.LOCAL, activationTime=0.0, deactivationTime=100000.0, loadType=SpecifiedLoadType.CONSTANT, period=0.0, phase=0.0, magnitude=0.0, momentDerivative=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.referenceFrame = referenceFrame
        self.directionVector = None
        self.activationTime = activationTime
        self.deactivationTime = deactivationTime
        self.loadType = loadType
        self.period = period
        self.phase = phase
        self.magnitude = magnitude
        self.momentDerivative = momentDerivative
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SpecifiedMomentBlueprint()


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
    def referenceFrame(self) -> ReferenceFrameType:
        """Direction vector in local or global coordinate system"""
        return self.__referenceFrame

    @referenceFrame.setter
    def referenceFrame(self, value: ReferenceFrameType):
        """Set referenceFrame"""
        self.__referenceFrame = value

    @property
    def directionVector(self) -> Vector3:
        """"""
        return self.__directionVector

    @directionVector.setter
    def directionVector(self, value: Vector3):
        """Set directionVector"""
        self.__directionVector = value

    @property
    def activationTime(self) -> float:
        """Time for switching component on"""
        return self.__activationTime

    @activationTime.setter
    def activationTime(self, value: float):
        """Set activationTime"""
        self.__activationTime = float(value)

    @property
    def deactivationTime(self) -> float:
        """Time for switching component off"""
        return self.__deactivationTime

    @deactivationTime.setter
    def deactivationTime(self, value: float):
        """Set deactivationTime"""
        self.__deactivationTime = float(value)

    @property
    def loadType(self) -> SpecifiedLoadType:
        """"""
        return self.__loadType

    @loadType.setter
    def loadType(self, value: SpecifiedLoadType):
        """Set loadType"""
        self.__loadType = value

    @property
    def period(self) -> float:
        """"""
        return self.__period

    @period.setter
    def period(self, value: float):
        """Set period"""
        self.__period = float(value)

    @property
    def phase(self) -> float:
        """"""
        return self.__phase

    @phase.setter
    def phase(self, value: float):
        """Set phase"""
        self.__phase = float(value)

    @property
    def magnitude(self) -> float:
        """Moment component magnitude parameter"""
        return self.__magnitude

    @magnitude.setter
    def magnitude(self, value: float):
        """Set magnitude"""
        self.__magnitude = float(value)

    @property
    def momentDerivative(self) -> float:
        """Moment component moment derivative parameter"""
        return self.__momentDerivative

    @momentDerivative.setter
    def momentDerivative(self, value: float):
        """Set momentDerivative"""
        self.__momentDerivative = float(value)
