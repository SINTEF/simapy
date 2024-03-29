# This an autogenerated file
# 
# Generated with AxisymmetricCrossSectionMassVolume
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.axisymmetriccrosssectionmassvolume import AxisymmetricCrossSectionMassVolumeBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class AxisymmetricCrossSectionMassVolume(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    massCoefficient : float
         Mass / unit length(default 0.0)
    extCrossSectionalArea : float
         External cross-sectional area(default 0.0)
    intCrossSectionalArea : float
         Internal cross-sectional area(default 0.0)
    gyrationRadius : float
         Radius of gyration about local x-axis(default 0.0)
    crossSectionArea : float
         Cross-section area for stress calculations(default 0.0)
    crossSectionModulus : float
         Cross-section modulus for stress calculations(default 0.0)
    diameter : float
         Diameter for stress calculations (default = 2 * sqrt(external area/pi))(default 0.0)
    thickness : float
         Thickness for stress calculations (default = sqrt(external area/pi) - sqrt(internal area/pi))(default 0.0)
    defaultStressCalculation : bool
         Use default stress calculation settings(default True)
    extContactRadius : float
         External contact radius (default = 0.0)(default 0.0)
    innerContactRadius : float
         Inner contact radius (default = 0.0)(default 0.0)
    """

    def __init__(self , description="", massCoefficient=0.0, extCrossSectionalArea=0.0, intCrossSectionalArea=0.0, gyrationRadius=0.0, crossSectionArea=0.0, crossSectionModulus=0.0, diameter=0.0, thickness=0.0, defaultStressCalculation=True, extContactRadius=0.0, innerContactRadius=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.massCoefficient = massCoefficient
        self.extCrossSectionalArea = extCrossSectionalArea
        self.intCrossSectionalArea = intCrossSectionalArea
        self.gyrationRadius = gyrationRadius
        self.crossSectionArea = crossSectionArea
        self.crossSectionModulus = crossSectionModulus
        self.diameter = diameter
        self.thickness = thickness
        self.defaultStressCalculation = defaultStressCalculation
        self.extContactRadius = extContactRadius
        self.innerContactRadius = innerContactRadius
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AxisymmetricCrossSectionMassVolumeBlueprint()


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
    def massCoefficient(self) -> float:
        """Mass / unit length"""
        return self.__massCoefficient

    @massCoefficient.setter
    def massCoefficient(self, value: float):
        """Set massCoefficient"""
        self.__massCoefficient = float(value)

    @property
    def extCrossSectionalArea(self) -> float:
        """External cross-sectional area"""
        return self.__extCrossSectionalArea

    @extCrossSectionalArea.setter
    def extCrossSectionalArea(self, value: float):
        """Set extCrossSectionalArea"""
        self.__extCrossSectionalArea = float(value)

    @property
    def intCrossSectionalArea(self) -> float:
        """Internal cross-sectional area"""
        return self.__intCrossSectionalArea

    @intCrossSectionalArea.setter
    def intCrossSectionalArea(self, value: float):
        """Set intCrossSectionalArea"""
        self.__intCrossSectionalArea = float(value)

    @property
    def gyrationRadius(self) -> float:
        """Radius of gyration about local x-axis"""
        return self.__gyrationRadius

    @gyrationRadius.setter
    def gyrationRadius(self, value: float):
        """Set gyrationRadius"""
        self.__gyrationRadius = float(value)

    @property
    def crossSectionArea(self) -> float:
        """Cross-section area for stress calculations"""
        return self.__crossSectionArea

    @crossSectionArea.setter
    def crossSectionArea(self, value: float):
        """Set crossSectionArea"""
        self.__crossSectionArea = float(value)

    @property
    def crossSectionModulus(self) -> float:
        """Cross-section modulus for stress calculations"""
        return self.__crossSectionModulus

    @crossSectionModulus.setter
    def crossSectionModulus(self, value: float):
        """Set crossSectionModulus"""
        self.__crossSectionModulus = float(value)

    @property
    def diameter(self) -> float:
        """Diameter for stress calculations (default = 2 * sqrt(external area/pi))"""
        return self.__diameter

    @diameter.setter
    def diameter(self, value: float):
        """Set diameter"""
        self.__diameter = float(value)

    @property
    def thickness(self) -> float:
        """Thickness for stress calculations (default = sqrt(external area/pi) - sqrt(internal area/pi))"""
        return self.__thickness

    @thickness.setter
    def thickness(self, value: float):
        """Set thickness"""
        self.__thickness = float(value)

    @property
    def defaultStressCalculation(self) -> bool:
        """Use default stress calculation settings"""
        return self.__defaultStressCalculation

    @defaultStressCalculation.setter
    def defaultStressCalculation(self, value: bool):
        """Set defaultStressCalculation"""
        self.__defaultStressCalculation = bool(value)

    @property
    def extContactRadius(self) -> float:
        """External contact radius (default = 0.0)"""
        return self.__extContactRadius

    @extContactRadius.setter
    def extContactRadius(self, value: float):
        """Set extContactRadius"""
        self.__extContactRadius = float(value)

    @property
    def innerContactRadius(self) -> float:
        """Inner contact radius (default = 0.0)"""
        return self.__innerContactRadius

    @innerContactRadius.setter
    def innerContactRadius(self, value: float):
        """Set innerContactRadius"""
        self.__innerContactRadius = float(value)
