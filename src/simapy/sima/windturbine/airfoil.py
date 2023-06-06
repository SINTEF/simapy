# This an autogenerated file
# 
# Generated with Airfoil
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.airfoil import AirfoilBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import ScriptableValue
from .foilpoint import FoilPoint
from .reynolditem import ReynoldItem

class Airfoil(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    deepstallRegime : bool
         Whether or not a deep stall regime is to be used(default False)
    inputStallPoints : bool
         (default False)
    upperTailAngle : float
         Tail angle between a line perpendicular to the flow and the line from the tip of the wedge, low (negative) angles of attack(default 0.0)
    lowerTailAngle : float
         As upper tail angle, but for high (positive) angles of attack(default 0.0)
    upperNoseAngle : float
         Nose angle between a line perpendicular to the flow and the line from the tip of the wedge, low (negative) angles of attack(default 0.0)
    lowerNoseAngle : float
         As upper nose angle, but for high (positive) angles of attack(default 0.0)
    noseRadiusRatio : float
         The ratio of the nose radius to the chord of the airfoil.(default 0.0)
    reynoldItems : List[ReynoldItem]
    points : List[FoilPoint]
    """

    def __init__(self , description="", deepstallRegime=False, inputStallPoints=False, upperTailAngle=0.0, lowerTailAngle=0.0, upperNoseAngle=0.0, lowerNoseAngle=0.0, noseRadiusRatio=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.deepstallRegime = deepstallRegime
        self.inputStallPoints = inputStallPoints
        self.upperTailAngle = upperTailAngle
        self.lowerTailAngle = lowerTailAngle
        self.upperNoseAngle = upperNoseAngle
        self.lowerNoseAngle = lowerNoseAngle
        self.noseRadiusRatio = noseRadiusRatio
        self.reynoldItems = list()
        self.points = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AirfoilBlueprint()


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
    def deepstallRegime(self) -> bool:
        """Whether or not a deep stall regime is to be used"""
        return self.__deepstallRegime

    @deepstallRegime.setter
    def deepstallRegime(self, value: bool):
        """Set deepstallRegime"""
        self.__deepstallRegime = bool(value)

    @property
    def inputStallPoints(self) -> bool:
        """"""
        return self.__inputStallPoints

    @inputStallPoints.setter
    def inputStallPoints(self, value: bool):
        """Set inputStallPoints"""
        self.__inputStallPoints = bool(value)

    @property
    def upperTailAngle(self) -> float:
        """Tail angle between a line perpendicular to the flow and the line from the tip of the wedge, low (negative) angles of attack"""
        return self.__upperTailAngle

    @upperTailAngle.setter
    def upperTailAngle(self, value: float):
        """Set upperTailAngle"""
        self.__upperTailAngle = float(value)

    @property
    def lowerTailAngle(self) -> float:
        """As upper tail angle, but for high (positive) angles of attack"""
        return self.__lowerTailAngle

    @lowerTailAngle.setter
    def lowerTailAngle(self, value: float):
        """Set lowerTailAngle"""
        self.__lowerTailAngle = float(value)

    @property
    def upperNoseAngle(self) -> float:
        """Nose angle between a line perpendicular to the flow and the line from the tip of the wedge, low (negative) angles of attack"""
        return self.__upperNoseAngle

    @upperNoseAngle.setter
    def upperNoseAngle(self, value: float):
        """Set upperNoseAngle"""
        self.__upperNoseAngle = float(value)

    @property
    def lowerNoseAngle(self) -> float:
        """As upper nose angle, but for high (positive) angles of attack"""
        return self.__lowerNoseAngle

    @lowerNoseAngle.setter
    def lowerNoseAngle(self, value: float):
        """Set lowerNoseAngle"""
        self.__lowerNoseAngle = float(value)

    @property
    def noseRadiusRatio(self) -> float:
        """The ratio of the nose radius to the chord of the airfoil."""
        return self.__noseRadiusRatio

    @noseRadiusRatio.setter
    def noseRadiusRatio(self, value: float):
        """Set noseRadiusRatio"""
        self.__noseRadiusRatio = float(value)

    @property
    def reynoldItems(self) -> List[ReynoldItem]:
        """"""
        return self.__reynoldItems

    @reynoldItems.setter
    def reynoldItems(self, value: List[ReynoldItem]):
        """Set reynoldItems"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__reynoldItems = value

    @property
    def points(self) -> List[FoilPoint]:
        """"""
        return self.__points

    @points.setter
    def points(self, value: List[FoilPoint]):
        """Set points"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__points = value
