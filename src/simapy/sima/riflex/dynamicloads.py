# This an autogenerated file
# 
# Generated with DynamicLoads
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dynamicloads import DynamicLoadsBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .dynamiccurrentvariation import DynamicCurrentVariation
from .dynamicnodalforces import DynamicNodalForces
from .rigidmoonpoolcolumn import RigidMoonpoolColumn

class DynamicLoads(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    dynamicNodalForces : DynamicNodalForces
    dynamicCurrentVariation : DynamicCurrentVariation
    rigidMoonpoolColumns : RigidMoonpoolColumn
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.dynamicNodalForces = None
        self.dynamicCurrentVariation = None
        self.rigidMoonpoolColumns = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DynamicLoadsBlueprint()


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
    def dynamicNodalForces(self) -> DynamicNodalForces:
        """"""
        return self.__dynamicNodalForces

    @dynamicNodalForces.setter
    def dynamicNodalForces(self, value: DynamicNodalForces):
        """Set dynamicNodalForces"""
        self.__dynamicNodalForces = value

    @property
    def dynamicCurrentVariation(self) -> DynamicCurrentVariation:
        """"""
        return self.__dynamicCurrentVariation

    @dynamicCurrentVariation.setter
    def dynamicCurrentVariation(self, value: DynamicCurrentVariation):
        """Set dynamicCurrentVariation"""
        self.__dynamicCurrentVariation = value

    @property
    def rigidMoonpoolColumns(self) -> RigidMoonpoolColumn:
        """"""
        return self.__rigidMoonpoolColumns

    @rigidMoonpoolColumns.setter
    def rigidMoonpoolColumns(self, value: RigidMoonpoolColumn):
        """Set rigidMoonpoolColumns"""
        self.__rigidMoonpoolColumns = value
