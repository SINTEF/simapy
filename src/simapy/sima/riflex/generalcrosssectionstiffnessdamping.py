# This an autogenerated file
# 
# Generated with GeneralCrossSectionStiffnessDamping
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.generalcrosssectionstiffnessdamping import GeneralCrossSectionStiffnessDampingBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class GeneralCrossSectionStiffnessDamping(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    axialFactor : float
         Factor for stiffness proportional damping in axial dof(default 0.0)
    torsionalFactor : float
         Factor for stiffness proportional damping in torsional dof(default 0.0)
    bendingFactorV : float
         Factor for stiffness proportional damping for bending around principal V-axis and shear in principal W-axis(default 0.0)
    bendingFactorW : float
         Factor for stiffness proportional damping for bending around principal W-axis and shear in principal V-axis(default 0.0)
    """

    def __init__(self , description="", axialFactor=0.0, torsionalFactor=0.0, bendingFactorV=0.0, bendingFactorW=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.axialFactor = axialFactor
        self.torsionalFactor = torsionalFactor
        self.bendingFactorV = bendingFactorV
        self.bendingFactorW = bendingFactorW
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GeneralCrossSectionStiffnessDampingBlueprint()


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
    def axialFactor(self) -> float:
        """Factor for stiffness proportional damping in axial dof"""
        return self.__axialFactor

    @axialFactor.setter
    def axialFactor(self, value: float):
        """Set axialFactor"""
        self.__axialFactor = float(value)

    @property
    def torsionalFactor(self) -> float:
        """Factor for stiffness proportional damping in torsional dof"""
        return self.__torsionalFactor

    @torsionalFactor.setter
    def torsionalFactor(self, value: float):
        """Set torsionalFactor"""
        self.__torsionalFactor = float(value)

    @property
    def bendingFactorV(self) -> float:
        """Factor for stiffness proportional damping for bending around principal V-axis and shear in principal W-axis"""
        return self.__bendingFactorV

    @bendingFactorV.setter
    def bendingFactorV(self, value: float):
        """Set bendingFactorV"""
        self.__bendingFactorV = float(value)

    @property
    def bendingFactorW(self) -> float:
        """Factor for stiffness proportional damping for bending around principal W-axis and shear in principal V-axis"""
        return self.__bendingFactorW

    @bendingFactorW.setter
    def bendingFactorW(self, value: float):
        """Set bendingFactorW"""
        self.__bendingFactorW = float(value)