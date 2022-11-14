# This an autogenerated file
# 
# Generated with MomentCoupling
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.momentcoupling import MomentCouplingBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.vector3 import Vector3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.simobody import SIMOBody

class MomentCoupling(NamedObject):
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
    body1 : SIMOBody
    rotationVector : Vector3
    body2 : SIMOBody
    initialMoment : float
         Initial moment(default 0.0)
    stiffness : float
         Moment stiffness(default 0.0)
    positiveDamping : float
         Damping coefficient for positive rotation(default 0.0)
    positiveExponent : float
         Exponent in damping for positive rotation(default 0.0)
    negativeDamping : float
         Damping coefficient for negative rotation(default 0.0)
    negativeExponent : float
         Exponent in damping for negative rotation(default 0.0)
    """

    def __init__(self , description="", _id=None, name=None, initialMoment=0.0, stiffness=0.0, positiveDamping=0.0, positiveExponent=0.0, negativeDamping=0.0, negativeExponent=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.body1 = None
        self.rotationVector = None
        self.body2 = None
        self.initialMoment = initialMoment
        self.stiffness = stiffness
        self.positiveDamping = positiveDamping
        self.positiveExponent = positiveExponent
        self.negativeDamping = negativeDamping
        self.negativeExponent = negativeExponent
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MomentCouplingBlueprint()


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
    def body1(self) -> SIMOBody:
        """"""
        return self.__body1

    @body1.setter
    def body1(self, value: SIMOBody):
        """Set body1"""
        self.__body1 = value

    @property
    def rotationVector(self) -> Vector3:
        """"""
        return self.__rotationVector

    @rotationVector.setter
    def rotationVector(self, value: Vector3):
        """Set rotationVector"""
        self.__rotationVector = value

    @property
    def body2(self) -> SIMOBody:
        """"""
        return self.__body2

    @body2.setter
    def body2(self, value: SIMOBody):
        """Set body2"""
        self.__body2 = value

    @property
    def initialMoment(self) -> float:
        """Initial moment"""
        return self.__initialMoment

    @initialMoment.setter
    def initialMoment(self, value: float):
        """Set initialMoment"""
        self.__initialMoment = float(value)

    @property
    def stiffness(self) -> float:
        """Moment stiffness"""
        return self.__stiffness

    @stiffness.setter
    def stiffness(self, value: float):
        """Set stiffness"""
        self.__stiffness = float(value)

    @property
    def positiveDamping(self) -> float:
        """Damping coefficient for positive rotation"""
        return self.__positiveDamping

    @positiveDamping.setter
    def positiveDamping(self, value: float):
        """Set positiveDamping"""
        self.__positiveDamping = float(value)

    @property
    def positiveExponent(self) -> float:
        """Exponent in damping for positive rotation"""
        return self.__positiveExponent

    @positiveExponent.setter
    def positiveExponent(self, value: float):
        """Set positiveExponent"""
        self.__positiveExponent = float(value)

    @property
    def negativeDamping(self) -> float:
        """Damping coefficient for negative rotation"""
        return self.__negativeDamping

    @negativeDamping.setter
    def negativeDamping(self, value: float):
        """Set negativeDamping"""
        self.__negativeDamping = float(value)

    @property
    def negativeExponent(self) -> float:
        """Exponent in damping for negative rotation"""
        return self.__negativeExponent

    @negativeExponent.setter
    def negativeExponent(self, value: float):
        """Set negativeExponent"""
        self.__negativeExponent = float(value)
