# This an autogenerated file
# 
# Generated with NPDWind
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.npdwind import NPDWindBlueprint
from typing import Dict
from .wind import Wind
from sima.sima import ScriptableValue

class NPDWind(Wind):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    direction : float
         Wind propagation direction(default 0.0)
    averageVelocity : float
         Average velocity at reference height(default 0.0)
    profileExponent : float
         Wind profile exponent(default 0.11)
    friction : float
         Surface drag coefficient.\nAlso used for transverse gust spectrum, if specified.(default 0.002)
    referenceHeight : float
         Reference height for wind velocity, fixed = 10 m.(default 10.0)
    """

    def __init__(self , description="", direction=0.0, averageVelocity=0.0, profileExponent=0.11, friction=0.002, referenceHeight=10.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.direction = direction
        self.averageVelocity = averageVelocity
        self.profileExponent = profileExponent
        self.friction = friction
        self.referenceHeight = referenceHeight
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return NPDWindBlueprint()


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
    def direction(self) -> float:
        """Wind propagation direction"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def averageVelocity(self) -> float:
        """Average velocity at reference height"""
        return self.__averageVelocity

    @averageVelocity.setter
    def averageVelocity(self, value: float):
        """Set averageVelocity"""
        self.__averageVelocity = float(value)

    @property
    def profileExponent(self) -> float:
        """Wind profile exponent"""
        return self.__profileExponent

    @profileExponent.setter
    def profileExponent(self, value: float):
        """Set profileExponent"""
        self.__profileExponent = float(value)

    @property
    def friction(self) -> float:
        """Surface drag coefficient.
Also used for transverse gust spectrum, if specified."""
        return self.__friction

    @friction.setter
    def friction(self, value: float):
        """Set friction"""
        self.__friction = float(value)

    @property
    def referenceHeight(self) -> float:
        """Reference height for wind velocity, fixed = 10 m."""
        return self.__referenceHeight

    @referenceHeight.setter
    def referenceHeight(self, value: float):
        """Set referenceHeight"""
        self.__referenceHeight = float(value)
