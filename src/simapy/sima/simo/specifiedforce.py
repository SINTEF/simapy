# This an autogenerated file
# 
# Generated with SpecifiedForce
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.specifiedforce import SpecifiedForceBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import Point3
from ..sima import ScriptableValue
from ..sima import Vector3
from .referenceframetype import ReferenceFrameType
from .specifiedloadtype import SpecifiedLoadType

class SpecifiedForce(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
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
         Force component magnitude parameter(default 0.0)
    forceDerivative : float
         Force component force derivative parameter(default 0.0)
    attachmentPoint : Point3
    """

    def __init__(self , description="", referenceFrame=ReferenceFrameType.LOCAL, activationTime=0.0, deactivationTime=100000.0, loadType=SpecifiedLoadType.CONSTANT, period=0.0, phase=0.0, magnitude=0.0, forceDerivative=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.referenceFrame = referenceFrame
        self.directionVector = None
        self.activationTime = activationTime
        self.deactivationTime = deactivationTime
        self.loadType = loadType
        self.period = period
        self.phase = phase
        self.magnitude = magnitude
        self.forceDerivative = forceDerivative
        self.attachmentPoint = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SpecifiedForceBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

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
        """Force component magnitude parameter"""
        return self.__magnitude

    @magnitude.setter
    def magnitude(self, value: float):
        """Set magnitude"""
        self.__magnitude = float(value)

    @property
    def forceDerivative(self) -> float:
        """Force component force derivative parameter"""
        return self.__forceDerivative

    @forceDerivative.setter
    def forceDerivative(self, value: float):
        """Set forceDerivative"""
        self.__forceDerivative = float(value)

    @property
    def attachmentPoint(self) -> Point3:
        """"""
        return self.__attachmentPoint

    @attachmentPoint.setter
    def attachmentPoint(self, value: Point3):
        """Set attachmentPoint"""
        self.__attachmentPoint = value
