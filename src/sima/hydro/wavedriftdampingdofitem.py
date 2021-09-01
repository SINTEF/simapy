# This an autogenerated file
# 
# Generated with WaveDriftDampingDofItem
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.wavedriftdampingdofitem import WaveDriftDampingDofItemBlueprint
from sima.hydro.directiondependentvalues import DirectionDependentValues
from sima.hydro.dof import DOF
from sima.hydro.values import Values
from sima.sima.scriptablevalue import ScriptableValue

class WaveDriftDampingDofItem(DirectionDependentValues):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    directionalValues : List[Values]
    dof1 : DOF
    dof2 : DOF
    """

    def __init__(self , name:str="", description:str="", _id:str="", dof1:DOF=DOF.X, dof2:DOF=DOF.X, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__directionalValues = list()
        self.__dof1 = dof1
        self.__dof2 = dof2
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WaveDriftDampingDofItemBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

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
