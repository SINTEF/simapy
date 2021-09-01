# This an autogenerated file
# 
# Generated with DockingConePositioning
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.dockingconepositioning import DockingConePositioningBlueprint
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.vector3 import Vector3
from sima.simo.activationfailuremode import ActivationFailureMode
from sima.simo.dockingconecrosssection import DockingConeCrossSection
from sima.simo.interpolation import Interpolation
from sima.simo.positioningelement import PositioningElement

class DockingConePositioning(PositioningElement):
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
    dampingExponent : float
         Exponent of velocity in damping term(default 1.0)
    dampingInterpolation : Interpolation
         Interpolation method for damping
    forceInterpolation : Interpolation
         Interpolation method for force
    velocityLimit : float
         Velocity limit for friction force(default 0.0)
    numberOfPoints : int
         (default 0)
    crossSections : List[DockingConeCrossSection]
    directionVector : Vector3
    maxRadialDistance : float
         Maximum radial distance at entry(default 0.0)
    friction : float
         Friction coefficient(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", failureMode:ActivationFailureMode=ActivationFailureMode.NONE, failureTime:float=0.0, breakingStrength:float=0.0, dampingExponent:float=1.0, dampingInterpolation:Interpolation=Interpolation.LINEAR, forceInterpolation:Interpolation=Interpolation.LINEAR, velocityLimit:float=0.0, numberOfPoints:int=0, maxRadialDistance:float=0.0, friction:float=0.0, **kwargs):
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
        self.__dampingExponent = dampingExponent
        self.__dampingInterpolation = dampingInterpolation
        self.__forceInterpolation = forceInterpolation
        self.__velocityLimit = velocityLimit
        self.__numberOfPoints = numberOfPoints
        self.__crossSections = list()
        self.__directionVector = Vector3()
        self.__maxRadialDistance = maxRadialDistance
        self.__friction = friction
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DockingConePositioningBlueprint()


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

    @property
    def dampingExponent(self) -> float:
        """Exponent of velocity in damping term"""
        return self.__dampingExponent

    @dampingExponent.setter
    def dampingExponent(self, value: float):
        """Set dampingExponent"""
        self.__dampingExponent = float(value)

    @property
    def dampingInterpolation(self) -> Interpolation:
        """Interpolation method for damping"""
        return self.__dampingInterpolation

    @dampingInterpolation.setter
    def dampingInterpolation(self, value: Interpolation):
        """Set dampingInterpolation"""
        self.__dampingInterpolation = value

    @property
    def forceInterpolation(self) -> Interpolation:
        """Interpolation method for force"""
        return self.__forceInterpolation

    @forceInterpolation.setter
    def forceInterpolation(self, value: Interpolation):
        """Set forceInterpolation"""
        self.__forceInterpolation = value

    @property
    def velocityLimit(self) -> float:
        """Velocity limit for friction force"""
        return self.__velocityLimit

    @velocityLimit.setter
    def velocityLimit(self, value: float):
        """Set velocityLimit"""
        self.__velocityLimit = float(value)

    @property
    def numberOfPoints(self) -> int:
        """"""
        return self.__numberOfPoints

    @numberOfPoints.setter
    def numberOfPoints(self, value: int):
        """Set numberOfPoints"""
        self.__numberOfPoints = int(value)

    @property
    def crossSections(self) -> List[DockingConeCrossSection]:
        """"""
        return self.__crossSections

    @crossSections.setter
    def crossSections(self, value: List[DockingConeCrossSection]):
        """Set crossSections"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__crossSections = value

    @property
    def directionVector(self) -> Vector3:
        """"""
        return self.__directionVector

    @directionVector.setter
    def directionVector(self, value: Vector3):
        """Set directionVector"""
        self.__directionVector = value

    @property
    def maxRadialDistance(self) -> float:
        """Maximum radial distance at entry"""
        return self.__maxRadialDistance

    @maxRadialDistance.setter
    def maxRadialDistance(self, value: float):
        """Set maxRadialDistance"""
        self.__maxRadialDistance = float(value)

    @property
    def friction(self) -> float:
        """Friction coefficient"""
        return self.__friction

    @friction.setter
    def friction(self, value: float):
        """Set friction"""
        self.__friction = float(value)
