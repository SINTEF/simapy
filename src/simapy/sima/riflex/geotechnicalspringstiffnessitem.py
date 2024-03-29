# This an autogenerated file
# 
# Generated with GeotechnicalSpringStiffnessItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.geotechnicalspringstiffnessitem import GeotechnicalSpringStiffnessItemBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class GeotechnicalSpringStiffnessItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    force : float
         Force corresponding to displacement(default 0.0)
    displacement : float
         Spring displacement.(default 0.0)
    """

    def __init__(self , description="", force=0.0, displacement=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.force = force
        self.displacement = displacement
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GeotechnicalSpringStiffnessItemBlueprint()


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
    def force(self) -> float:
        """Force corresponding to displacement"""
        return self.__force

    @force.setter
    def force(self, value: float):
        """Set force"""
        self.__force = float(value)

    @property
    def displacement(self) -> float:
        """Spring displacement."""
        return self.__displacement

    @displacement.setter
    def displacement(self, value: float):
        """Set displacement"""
        self.__displacement = float(value)
