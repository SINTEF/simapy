# This an autogenerated file
# 
# Generated with SpringStiffnessItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.springstiffnessitem import SpringStiffnessItemBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class SpringStiffnessItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    force : float
         Pressure force corresponding to compression(default 0.0)
    compression : float
         Spring compression(default 0.0)
    """

    def __init__(self , description="", force=0.0, compression=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.force = force
        self.compression = compression
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SpringStiffnessItemBlueprint()


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
        """Pressure force corresponding to compression"""
        return self.__force

    @force.setter
    def force(self, value: float):
        """Set force"""
        self.__force = float(value)

    @property
    def compression(self) -> float:
        """Spring compression"""
        return self.__compression

    @compression.setter
    def compression(self, value: float):
        """Set compression"""
        self.__compression = float(value)
