# This an autogenerated file
# 
# Generated with Sletringen
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.sletringen import SletringenBlueprint
from sima.environment.wind import Wind
from sima.sima.scriptablevalue import ScriptableValue

class Sletringen(Wind):
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
    direction : float
         Wind propagation direction(default 0.0)
    profileExponent : float
         Wind profile exponent(default 0.11)
    averageVelocity : float
         Average velocity at reference height(default 0.0)
    friction : float
         Surface drag coefficient.\nAlso used for transverse gust spectrum, if specified in DYNMOD.(default 0.002)
    gamma : float
         Temperature stability parameter(default 10.0)
    referenceHeight : float
         Reference height for wind velocity(default 10.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", direction:float=0.0, profileExponent:float=0.11, averageVelocity:float=0.0, friction:float=0.002, gamma:float=10.0, referenceHeight:float=10.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__direction = direction
        self.__profileExponent = profileExponent
        self.__averageVelocity = averageVelocity
        self.__friction = friction
        self.__gamma = gamma
        self.__referenceHeight = referenceHeight
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SletringenBlueprint()


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
    def direction(self) -> float:
        """Wind propagation direction"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def profileExponent(self) -> float:
        """Wind profile exponent"""
        return self.__profileExponent

    @profileExponent.setter
    def profileExponent(self, value: float):
        """Set profileExponent"""
        self.__profileExponent = float(value)

    @property
    def averageVelocity(self) -> float:
        """Average velocity at reference height"""
        return self.__averageVelocity

    @averageVelocity.setter
    def averageVelocity(self, value: float):
        """Set averageVelocity"""
        self.__averageVelocity = float(value)

    @property
    def friction(self) -> float:
        """Surface drag coefficient.
Also used for transverse gust spectrum, if specified in DYNMOD."""
        return self.__friction

    @friction.setter
    def friction(self, value: float):
        """Set friction"""
        self.__friction = float(value)

    @property
    def gamma(self) -> float:
        """Temperature stability parameter"""
        return self.__gamma

    @gamma.setter
    def gamma(self, value: float):
        """Set gamma"""
        self.__gamma = float(value)

    @property
    def referenceHeight(self) -> float:
        """Reference height for wind velocity"""
        return self.__referenceHeight

    @referenceHeight.setter
    def referenceHeight(self, value: float):
        """Set referenceHeight"""
        self.__referenceHeight = float(value)
