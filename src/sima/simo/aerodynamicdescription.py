# This an autogenerated file
# 
# Generated with AerodynamicDescription
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.aerodynamicdescription import AerodynamicDescriptionBlueprint
from typing import Dict
from .aerodynamicdescriptiontype import AerodynamicDescriptionType
from sima.sima import MOAO
from sima.sima import ScriptableValue

class AerodynamicDescription(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    quadraticLongitudinalDrag : float
         Quadratic longitudinal drag coefficient(default 0.0)
    quadraticTransverseY : float
         Quadratic transverse (Y) drag coefficient(default 0.0)
    quadraticTransverseZ : float
         Quadratic transverse (Z) drag coefficient(default 0.0)
    aerodynamicType : AerodynamicDescriptionType
         Type of aerodynamic forces
    """

    def __init__(self , description="", quadraticLongitudinalDrag=0.0, quadraticTransverseY=0.0, quadraticTransverseZ=0.0, aerodynamicType=AerodynamicDescriptionType.DRAG, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.quadraticLongitudinalDrag = quadraticLongitudinalDrag
        self.quadraticTransverseY = quadraticTransverseY
        self.quadraticTransverseZ = quadraticTransverseZ
        self.aerodynamicType = aerodynamicType
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AerodynamicDescriptionBlueprint()


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
    def quadraticLongitudinalDrag(self) -> float:
        """Quadratic longitudinal drag coefficient"""
        return self.__quadraticLongitudinalDrag

    @quadraticLongitudinalDrag.setter
    def quadraticLongitudinalDrag(self, value: float):
        """Set quadraticLongitudinalDrag"""
        self.__quadraticLongitudinalDrag = float(value)

    @property
    def quadraticTransverseY(self) -> float:
        """Quadratic transverse (Y) drag coefficient"""
        return self.__quadraticTransverseY

    @quadraticTransverseY.setter
    def quadraticTransverseY(self, value: float):
        """Set quadraticTransverseY"""
        self.__quadraticTransverseY = float(value)

    @property
    def quadraticTransverseZ(self) -> float:
        """Quadratic transverse (Z) drag coefficient"""
        return self.__quadraticTransverseZ

    @quadraticTransverseZ.setter
    def quadraticTransverseZ(self, value: float):
        """Set quadraticTransverseZ"""
        self.__quadraticTransverseZ = float(value)

    @property
    def aerodynamicType(self) -> AerodynamicDescriptionType:
        """Type of aerodynamic forces"""
        return self.__aerodynamicType

    @aerodynamicType.setter
    def aerodynamicType(self, value: AerodynamicDescriptionType):
        """Set aerodynamicType"""
        self.__aerodynamicType = value
