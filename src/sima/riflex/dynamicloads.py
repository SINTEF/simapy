# This an autogenerated file
# 
# Generated with DynamicLoads
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dynamicloads import DynamicLoadsBlueprint
from typing import Dict
from sima.riflex.dynamiccurrentvariation import DynamicCurrentVariation
from sima.riflex.dynamicnodalforces import DynamicNodalForces
from sima.riflex.rigidmoonpoolcolumn import RigidMoonpoolColumn
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class DynamicLoads(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    dynamicNodalForces : DynamicNodalForces
    dynamicCurrentVariation : DynamicCurrentVariation
    rigidMoonpoolColumns : RigidMoonpoolColumn
    """

    def __init__(self , description="", _id=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
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
