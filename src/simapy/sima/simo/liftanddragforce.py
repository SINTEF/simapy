# This an autogenerated file
# 
# Generated with LiftAndDragForce
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.liftanddragforce import LiftAndDragForceBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import Point3
from ..sima import ScriptableValue
from ..sima import Vector3
from .liftanddragforcecharacteristicitem import LiftAndDragForceCharacteristicItem
from .liftanddraginterpolation import LiftAndDragInterpolation

class LiftAndDragForce(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    point : Point3
    maxAngle : float
         Maximum rudder angle(default 0.0)
    maxAngleVelocity : float
         Maximum velocity of rudder angle(default 0.0)
    lengthZ : float
         Length in z-direction(default 0.0)
    lengthX : float
         Length in x-direction(default 0.0)
    vectorZ : Vector3
    vectorXZ : Vector3
    angle : float
         Rudder angle(default 0.0)
    currentFactor : float
         Factor that current velocity is multiplied with(default 0.0)
    vesselFactor : float
         Factor that vessel velocity is multiplied with(default 0.0)
    thrusterFactor : float
         Factor that thruster induced velocity is multiplied with(default 0.0)
    dragZ : float
         Quadratic force coefficient in rudder z-direction(default 0.0)
    items : List[LiftAndDragForceCharacteristicItem]
    interpolation : LiftAndDragInterpolation
         Interpolation method
    symmetric : bool
         Symmetry about x-axis(default False)
    """

    def __init__(self , description="", maxAngle=0.0, maxAngleVelocity=0.0, lengthZ=0.0, lengthX=0.0, angle=0.0, currentFactor=0.0, vesselFactor=0.0, thrusterFactor=0.0, dragZ=0.0, interpolation=LiftAndDragInterpolation.LINEAR, symmetric=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.point = None
        self.maxAngle = maxAngle
        self.maxAngleVelocity = maxAngleVelocity
        self.lengthZ = lengthZ
        self.lengthX = lengthX
        self.vectorZ = None
        self.vectorXZ = None
        self.angle = angle
        self.currentFactor = currentFactor
        self.vesselFactor = vesselFactor
        self.thrusterFactor = thrusterFactor
        self.dragZ = dragZ
        self.items = list()
        self.interpolation = interpolation
        self.symmetric = symmetric
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return LiftAndDragForceBlueprint()


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
    def point(self) -> Point3:
        """"""
        return self.__point

    @point.setter
    def point(self, value: Point3):
        """Set point"""
        self.__point = value

    @property
    def maxAngle(self) -> float:
        """Maximum rudder angle"""
        return self.__maxAngle

    @maxAngle.setter
    def maxAngle(self, value: float):
        """Set maxAngle"""
        self.__maxAngle = float(value)

    @property
    def maxAngleVelocity(self) -> float:
        """Maximum velocity of rudder angle"""
        return self.__maxAngleVelocity

    @maxAngleVelocity.setter
    def maxAngleVelocity(self, value: float):
        """Set maxAngleVelocity"""
        self.__maxAngleVelocity = float(value)

    @property
    def lengthZ(self) -> float:
        """Length in z-direction"""
        return self.__lengthZ

    @lengthZ.setter
    def lengthZ(self, value: float):
        """Set lengthZ"""
        self.__lengthZ = float(value)

    @property
    def lengthX(self) -> float:
        """Length in x-direction"""
        return self.__lengthX

    @lengthX.setter
    def lengthX(self, value: float):
        """Set lengthX"""
        self.__lengthX = float(value)

    @property
    def vectorZ(self) -> Vector3:
        """"""
        return self.__vectorZ

    @vectorZ.setter
    def vectorZ(self, value: Vector3):
        """Set vectorZ"""
        self.__vectorZ = value

    @property
    def vectorXZ(self) -> Vector3:
        """"""
        return self.__vectorXZ

    @vectorXZ.setter
    def vectorXZ(self, value: Vector3):
        """Set vectorXZ"""
        self.__vectorXZ = value

    @property
    def angle(self) -> float:
        """Rudder angle"""
        return self.__angle

    @angle.setter
    def angle(self, value: float):
        """Set angle"""
        self.__angle = float(value)

    @property
    def currentFactor(self) -> float:
        """Factor that current velocity is multiplied with"""
        return self.__currentFactor

    @currentFactor.setter
    def currentFactor(self, value: float):
        """Set currentFactor"""
        self.__currentFactor = float(value)

    @property
    def vesselFactor(self) -> float:
        """Factor that vessel velocity is multiplied with"""
        return self.__vesselFactor

    @vesselFactor.setter
    def vesselFactor(self, value: float):
        """Set vesselFactor"""
        self.__vesselFactor = float(value)

    @property
    def thrusterFactor(self) -> float:
        """Factor that thruster induced velocity is multiplied with"""
        return self.__thrusterFactor

    @thrusterFactor.setter
    def thrusterFactor(self, value: float):
        """Set thrusterFactor"""
        self.__thrusterFactor = float(value)

    @property
    def dragZ(self) -> float:
        """Quadratic force coefficient in rudder z-direction"""
        return self.__dragZ

    @dragZ.setter
    def dragZ(self, value: float):
        """Set dragZ"""
        self.__dragZ = float(value)

    @property
    def items(self) -> List[LiftAndDragForceCharacteristicItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[LiftAndDragForceCharacteristicItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__items = value

    @property
    def interpolation(self) -> LiftAndDragInterpolation:
        """Interpolation method"""
        return self.__interpolation

    @interpolation.setter
    def interpolation(self, value: LiftAndDragInterpolation):
        """Set interpolation"""
        self.__interpolation = value

    @property
    def symmetric(self) -> bool:
        """Symmetry about x-axis"""
        return self.__symmetric

    @symmetric.setter
    def symmetric(self, value: bool):
        """Set symmetric"""
        self.__symmetric = bool(value)
