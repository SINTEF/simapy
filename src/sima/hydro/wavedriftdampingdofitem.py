# This an autogenerated file
# 
# Generated with WaveDriftDampingDofItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wavedriftdampingdofitem import WaveDriftDampingDofItemBlueprint
from typing import Dict
from sima.hydro.directiondependentvalues import DirectionDependentValues
from sima.hydro.dof import DOF
from sima.hydro.values import Values
from sima.sima.scriptablevalue import ScriptableValue

class WaveDriftDampingDofItem(DirectionDependentValues):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    directionalValues : List[Values]
    dof1 : DOF
    dof2 : DOF
    """

    def __init__(self , description="", dof1=DOF.X, dof2=DOF.X, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.directionalValues = list()
        self.dof1 = dof1
        self.dof2 = dof2
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WaveDriftDampingDofItemBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def directionalValues(self) -> List[Values]:
        """"""
        return self.__directionalValues

    @directionalValues.setter
    def directionalValues(self, value: List[Values]):
        """Set directionalValues"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__directionalValues = value

    @property
    def dof1(self) -> DOF:
        """"""
        return self.__dof1

    @dof1.setter
    def dof1(self, value: DOF):
        """Set dof1"""
        self.__dof1 = value

    @property
    def dof2(self) -> DOF:
        """"""
        return self.__dof2

    @dof2.setter
    def dof2(self, value: DOF):
        """Set dof2"""
        self.__dof2 = value
