# This an autogenerated file
# 
# Generated with DampingFactorUserDefinedProperty
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dampingfactoruserdefinedproperty import DampingFactorUserDefinedPropertyBlueprint
from typing import Dict
from .dampingfactorproperty import DampingFactorProperty
from sima.sima import ScriptableValue

class DampingFactorUserDefinedProperty(DampingFactorProperty):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    stillWaterDampingFactor : float
         Still water damping factor(default 1.0)
    """

    def __init__(self , description="", stillWaterDampingFactor=1.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.stillWaterDampingFactor = stillWaterDampingFactor
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DampingFactorUserDefinedPropertyBlueprint()


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
    def stillWaterDampingFactor(self) -> float:
        """Still water damping factor"""
        return self.__stillWaterDampingFactor

    @stillWaterDampingFactor.setter
    def stillWaterDampingFactor(self, value: float):
        """Set stillWaterDampingFactor"""
        self.__stillWaterDampingFactor = float(value)