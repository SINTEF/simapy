# This an autogenerated file
# 
# Generated with GeoTechnical
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.geotechnical import GeoTechnicalBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import ScriptableValue
from .geotechnicalpiletype import GeotechnicalPileType
from .soilitem import SoilItem
from .soilstiffnesstype import SoilStiffnessType

class GeoTechnical(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    soilItems : List[SoilItem]
    scourDepth : float
         Length from mudline to actual contact point between mud and coductor(default 0.0)
    diameter : float
         Used for calculation of geotechnical spring properties(default 0.0)
    _type : SoilStiffnessType
    calculateDiameter : bool
         Calculate diameter from cross-sections(default True)
    calculateAxialPileResistance : bool
         Calculate axial pile resistance(default False)
    pileType : GeotechnicalPileType
    zoneOfInfluence : float
         Zone of influence(default 0.0)
    curveFittingFactor : float
         Curve fitting factor(default 0.0)
    """

    def __init__(self , description="", scourDepth=0.0, diameter=0.0, _type=SoilStiffnessType.STATIC, calculateDiameter=True, calculateAxialPileResistance=False, pileType=GeotechnicalPileType.OPEN, zoneOfInfluence=0.0, curveFittingFactor=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.soilItems = list()
        self.scourDepth = scourDepth
        self.diameter = diameter
        self._type = _type
        self.calculateDiameter = calculateDiameter
        self.calculateAxialPileResistance = calculateAxialPileResistance
        self.pileType = pileType
        self.zoneOfInfluence = zoneOfInfluence
        self.curveFittingFactor = curveFittingFactor
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GeoTechnicalBlueprint()


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
    def soilItems(self) -> List[SoilItem]:
        """"""
        return self.__soilItems

    @soilItems.setter
    def soilItems(self, value: List[SoilItem]):
        """Set soilItems"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__soilItems = value

    @property
    def scourDepth(self) -> float:
        """Length from mudline to actual contact point between mud and coductor"""
        return self.__scourDepth

    @scourDepth.setter
    def scourDepth(self, value: float):
        """Set scourDepth"""
        self.__scourDepth = float(value)

    @property
    def diameter(self) -> float:
        """Used for calculation of geotechnical spring properties"""
        return self.__diameter

    @diameter.setter
    def diameter(self, value: float):
        """Set diameter"""
        self.__diameter = float(value)

    @property
    def _type(self) -> SoilStiffnessType:
        """"""
        return self.___type

    @_type.setter
    def _type(self, value: SoilStiffnessType):
        """Set _type"""
        self.___type = value

    @property
    def calculateDiameter(self) -> bool:
        """Calculate diameter from cross-sections"""
        return self.__calculateDiameter

    @calculateDiameter.setter
    def calculateDiameter(self, value: bool):
        """Set calculateDiameter"""
        self.__calculateDiameter = bool(value)

    @property
    def calculateAxialPileResistance(self) -> bool:
        """Calculate axial pile resistance"""
        return self.__calculateAxialPileResistance

    @calculateAxialPileResistance.setter
    def calculateAxialPileResistance(self, value: bool):
        """Set calculateAxialPileResistance"""
        self.__calculateAxialPileResistance = bool(value)

    @property
    def pileType(self) -> GeotechnicalPileType:
        """"""
        return self.__pileType

    @pileType.setter
    def pileType(self, value: GeotechnicalPileType):
        """Set pileType"""
        self.__pileType = value

    @property
    def zoneOfInfluence(self) -> float:
        """Zone of influence"""
        return self.__zoneOfInfluence

    @zoneOfInfluence.setter
    def zoneOfInfluence(self, value: float):
        """Set zoneOfInfluence"""
        self.__zoneOfInfluence = float(value)

    @property
    def curveFittingFactor(self) -> float:
        """Curve fitting factor"""
        return self.__curveFittingFactor

    @curveFittingFactor.setter
    def curveFittingFactor(self, value: float):
        """Set curveFittingFactor"""
        self.__curveFittingFactor = float(value)