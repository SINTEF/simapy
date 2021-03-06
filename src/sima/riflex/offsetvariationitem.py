# This an autogenerated file
# 
# Generated with OffsetVariationItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.offsetvariationitem import OffsetVariationItemBlueprint
from typing import Dict
from sima.riflex.referencetype import ReferenceType
from sima.riflex.rotationcode import RotationCode
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.supernode import SuperNode
    from sima.riflex.supportvessel import SupportVessel

class OffsetVariationItem(MOAO):
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
    referenceType : ReferenceType
         Reference to moving point
    dx : float
         Displacement increment, x-direction(default 0.0)
    dy : float
         Displacement increment, y-direction(default 0.0)
    dz : float
         Displacement increment, z-direction(default 0.0)
    rotationCode : RotationCode
         Rotation about axis
    rotationIncrement : float
         Rotation increments(default 0.0)
    supernode : SuperNode
    supportVessel : SupportVessel
    """

    def __init__(self , name="", description="", _id="", referenceType=ReferenceType.SUPER_NODE, dx=0.0, dy=0.0, dz=0.0, rotationCode=RotationCode.NONE, rotationIncrement=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.referenceType = referenceType
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.rotationCode = rotationCode
        self.rotationIncrement = rotationIncrement
        self.supernode = None
        self.supportVessel = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return OffsetVariationItemBlueprint()


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
    def referenceType(self) -> ReferenceType:
        """Reference to moving point"""
        return self.__referenceType

    @referenceType.setter
    def referenceType(self, value: ReferenceType):
        """Set referenceType"""
        self.__referenceType = value

    @property
    def dx(self) -> float:
        """Displacement increment, x-direction"""
        return self.__dx

    @dx.setter
    def dx(self, value: float):
        """Set dx"""
        self.__dx = float(value)

    @property
    def dy(self) -> float:
        """Displacement increment, y-direction"""
        return self.__dy

    @dy.setter
    def dy(self, value: float):
        """Set dy"""
        self.__dy = float(value)

    @property
    def dz(self) -> float:
        """Displacement increment, z-direction"""
        return self.__dz

    @dz.setter
    def dz(self, value: float):
        """Set dz"""
        self.__dz = float(value)

    @property
    def rotationCode(self) -> RotationCode:
        """Rotation about axis"""
        return self.__rotationCode

    @rotationCode.setter
    def rotationCode(self, value: RotationCode):
        """Set rotationCode"""
        self.__rotationCode = value

    @property
    def rotationIncrement(self) -> float:
        """Rotation increments"""
        return self.__rotationIncrement

    @rotationIncrement.setter
    def rotationIncrement(self, value: float):
        """Set rotationIncrement"""
        self.__rotationIncrement = float(value)

    @property
    def supernode(self) -> SuperNode:
        """"""
        return self.__supernode

    @supernode.setter
    def supernode(self, value: SuperNode):
        """Set supernode"""
        self.__supernode = value

    @property
    def supportVessel(self) -> SupportVessel:
        """"""
        return self.__supportVessel

    @supportVessel.setter
    def supportVessel(self, value: SupportVessel):
        """Set supportVessel"""
        self.__supportVessel = value
