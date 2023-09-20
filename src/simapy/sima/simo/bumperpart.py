# This an autogenerated file
# 
# Generated with BumperPart
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.bumperpart import BumperPartBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import Point3
from ..sima import ScriptableValue

class BumperPart(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    radius : float
         diameter of bumper element(default 0.0)
    stiffness : float
         Bumper force stiffness, normal to elements(default 0.0)
    damping : float
         Damping(default 0.0)
    end1 : Point3
    end2 : Point3
    """

    def __init__(self , description="", radius=0.0, stiffness=0.0, damping=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.radius = radius
        self.stiffness = stiffness
        self.damping = damping
        self.end1 = None
        self.end2 = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BumperPartBlueprint()


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
    def radius(self) -> float:
        """diameter of bumper element"""
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        """Set radius"""
        self.__radius = float(value)

    @property
    def stiffness(self) -> float:
        """Bumper force stiffness, normal to elements"""
        return self.__stiffness

    @stiffness.setter
    def stiffness(self, value: float):
        """Set stiffness"""
        self.__stiffness = float(value)

    @property
    def damping(self) -> float:
        """Damping"""
        return self.__damping

    @damping.setter
    def damping(self, value: float):
        """Set damping"""
        self.__damping = float(value)

    @property
    def end1(self) -> Point3:
        """"""
        return self.__end1

    @end1.setter
    def end1(self, value: Point3):
        """Set end1"""
        self.__end1 = value

    @property
    def end2(self) -> Point3:
        """"""
        return self.__end2

    @end2.setter
    def end2(self, value: Point3):
        """Set end2"""
        self.__end2 = value