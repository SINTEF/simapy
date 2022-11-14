# This an autogenerated file
# 
# Generated with RollerBerthingFender
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.rollerberthingfender import RollerBerthingFenderBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.vector3 import Vector3
from sima.simo.fenderattachment import FenderAttachment
from sima.simo.forcedampingcharacteristic import ForceDampingCharacteristic
from sima.simo.plane import Plane

class RollerBerthingFender(NamedObject):
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
    dynamicFriction : float
         Dynamic friction coefficient, sliding(default 0.0)
    staticFriction : float
         Friction coefficient, when not sliding (stiction)(default 0.0)
    shearStiffnes : float
         Shear stiffness associated with friction(default 0.0)
    velocityLimit : float
         Velocity limit for normal friction force(default 0.0)
    contactPlane : Plane
    characteristic : ForceDampingCharacteristic
    attachment : FenderAttachment
         Fender attachment
    contactPoint : Point3
    axisVector : Vector3
    """

    def __init__(self , description="", _id=None, name=None, dynamicFriction=0.0, staticFriction=0.0, shearStiffnes=0.0, velocityLimit=0.0, attachment=FenderAttachment.GLOBAL_POINT, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.dynamicFriction = dynamicFriction
        self.staticFriction = staticFriction
        self.shearStiffnes = shearStiffnes
        self.velocityLimit = velocityLimit
        self.contactPlane = None
        self.characteristic = None
        self.attachment = attachment
        self.contactPoint = None
        self.axisVector = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RollerBerthingFenderBlueprint()


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
    def dynamicFriction(self) -> float:
        """Dynamic friction coefficient, sliding"""
        return self.__dynamicFriction

    @dynamicFriction.setter
    def dynamicFriction(self, value: float):
        """Set dynamicFriction"""
        self.__dynamicFriction = float(value)

    @property
    def staticFriction(self) -> float:
        """Friction coefficient, when not sliding (stiction)"""
        return self.__staticFriction

    @staticFriction.setter
    def staticFriction(self, value: float):
        """Set staticFriction"""
        self.__staticFriction = float(value)

    @property
    def shearStiffnes(self) -> float:
        """Shear stiffness associated with friction"""
        return self.__shearStiffnes

    @shearStiffnes.setter
    def shearStiffnes(self, value: float):
        """Set shearStiffnes"""
        self.__shearStiffnes = float(value)

    @property
    def velocityLimit(self) -> float:
        """Velocity limit for normal friction force"""
        return self.__velocityLimit

    @velocityLimit.setter
    def velocityLimit(self, value: float):
        """Set velocityLimit"""
        self.__velocityLimit = float(value)

    @property
    def contactPlane(self) -> Plane:
        """"""
        return self.__contactPlane

    @contactPlane.setter
    def contactPlane(self, value: Plane):
        """Set contactPlane"""
        self.__contactPlane = value

    @property
    def characteristic(self) -> ForceDampingCharacteristic:
        """"""
        return self.__characteristic

    @characteristic.setter
    def characteristic(self, value: ForceDampingCharacteristic):
        """Set characteristic"""
        self.__characteristic = value

    @property
    def attachment(self) -> FenderAttachment:
        """Fender attachment"""
        return self.__attachment

    @attachment.setter
    def attachment(self, value: FenderAttachment):
        """Set attachment"""
        self.__attachment = value

    @property
    def contactPoint(self) -> Point3:
        """"""
        return self.__contactPoint

    @contactPoint.setter
    def contactPoint(self, value: Point3):
        """Set contactPoint"""
        self.__contactPoint = value

    @property
    def axisVector(self) -> Vector3:
        """"""
        return self.__axisVector

    @axisVector.setter
    def axisVector(self, value: Vector3):
        """Set axisVector"""
        self.__axisVector = value
