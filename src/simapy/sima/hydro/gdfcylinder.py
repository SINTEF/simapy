# This an autogenerated file
# 
# Generated with GDFCylinder
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.gdfcylinder import GDFCylinderBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class GDFCylinder(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    dimensionalLength : float
         Dimensional length(default 1.0)
    centerX : float
         Global x-coordinate(default 0.0)
    centerY : float
         Global y-coordinate(default 0.0)
    radius : float
         Radius of cyllinder(default 40.0)
    numberOfRadialPanels : int
         Number of panels around the circumference(default 20)
    depth : float
         Depth of cylinder (1 means equidistant)(default 20.0)
    numberOfVerticalPanels : int
         Number of depth levels(default 10)
    exponent : float
         Exponent in depth distribution(default 2.0)
    """

    def __init__(self , description="", dimensionalLength=1.0, centerX=0.0, centerY=0.0, radius=40.0, numberOfRadialPanels=20, depth=20.0, numberOfVerticalPanels=10, exponent=2.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.dimensionalLength = dimensionalLength
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        self.numberOfRadialPanels = numberOfRadialPanels
        self.depth = depth
        self.numberOfVerticalPanels = numberOfVerticalPanels
        self.exponent = exponent
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GDFCylinderBlueprint()


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
    def dimensionalLength(self) -> float:
        """Dimensional length"""
        return self.__dimensionalLength

    @dimensionalLength.setter
    def dimensionalLength(self, value: float):
        """Set dimensionalLength"""
        self.__dimensionalLength = float(value)

    @property
    def centerX(self) -> float:
        """Global x-coordinate"""
        return self.__centerX

    @centerX.setter
    def centerX(self, value: float):
        """Set centerX"""
        self.__centerX = float(value)

    @property
    def centerY(self) -> float:
        """Global y-coordinate"""
        return self.__centerY

    @centerY.setter
    def centerY(self, value: float):
        """Set centerY"""
        self.__centerY = float(value)

    @property
    def radius(self) -> float:
        """Radius of cyllinder"""
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        """Set radius"""
        self.__radius = float(value)

    @property
    def numberOfRadialPanels(self) -> int:
        """Number of panels around the circumference"""
        return self.__numberOfRadialPanels

    @numberOfRadialPanels.setter
    def numberOfRadialPanels(self, value: int):
        """Set numberOfRadialPanels"""
        self.__numberOfRadialPanels = int(value)

    @property
    def depth(self) -> float:
        """Depth of cylinder (1 means equidistant)"""
        return self.__depth

    @depth.setter
    def depth(self, value: float):
        """Set depth"""
        self.__depth = float(value)

    @property
    def numberOfVerticalPanels(self) -> int:
        """Number of depth levels"""
        return self.__numberOfVerticalPanels

    @numberOfVerticalPanels.setter
    def numberOfVerticalPanels(self, value: int):
        """Set numberOfVerticalPanels"""
        self.__numberOfVerticalPanels = int(value)

    @property
    def exponent(self) -> float:
        """Exponent in depth distribution"""
        return self.__exponent

    @exponent.setter
    def exponent(self, value: float):
        """Set exponent"""
        self.__exponent = float(value)
