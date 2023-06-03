# This an autogenerated file
# 
# Generated with InfrastructureBody
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.infrastructurebody import InfrastructureBodyBlueprint
from typing import Dict
from .appearance import Appearance
from .body import Body
from .bodyviewpoint import BodyViewpoint
from .position import Position
from .scriptablevalue import ScriptableValue

class InfrastructureBody(Body):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    length : float
         Length(default 10.0)
    width : float
         Width(default 5.0)
    height : float
         Height(default 5.0)
    appearance : Appearance
    initialPosition : Position
    viewpoints : List[BodyViewpoint]
    utmX : float
         UTM x coordinates(default 0.0)
    utmY : float
         UTM y coordinates(default 0.0)
    """

    def __init__(self , description="", length=10.0, width=5.0, height=5.0, utmX=0.0, utmY=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.length = length
        self.width = width
        self.height = height
        self.appearance = None
        self.initialPosition = None
        self.viewpoints = list()
        self.utmX = utmX
        self.utmY = utmY
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return InfrastructureBodyBlueprint()


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
    def length(self) -> float:
        """Length"""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def width(self) -> float:
        """Width"""
        return self.__width

    @width.setter
    def width(self, value: float):
        """Set width"""
        self.__width = float(value)

    @property
    def height(self) -> float:
        """Height"""
        return self.__height

    @height.setter
    def height(self, value: float):
        """Set height"""
        self.__height = float(value)

    @property
    def appearance(self) -> Appearance:
        """"""
        return self.__appearance

    @appearance.setter
    def appearance(self, value: Appearance):
        """Set appearance"""
        self.__appearance = value

    @property
    def initialPosition(self) -> Position:
        """"""
        return self.__initialPosition

    @initialPosition.setter
    def initialPosition(self, value: Position):
        """Set initialPosition"""
        self.__initialPosition = value

    @property
    def viewpoints(self) -> List[BodyViewpoint]:
        """"""
        return self.__viewpoints

    @viewpoints.setter
    def viewpoints(self, value: List[BodyViewpoint]):
        """Set viewpoints"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__viewpoints = value

    @property
    def utmX(self) -> float:
        """UTM x coordinates"""
        return self.__utmX

    @utmX.setter
    def utmX(self, value: float):
        """Set utmX"""
        self.__utmX = float(value)

    @property
    def utmY(self) -> float:
        """UTM y coordinates"""
        return self.__utmY

    @utmY.setter
    def utmY(self, value: float):
        """Set utmY"""
        self.__utmY = float(value)
