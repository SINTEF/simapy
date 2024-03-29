# This an autogenerated file
# 
# Generated with CoupledRadiationDataGroup
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.coupledradiationdatagroup import CoupledRadiationDataGroupBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .coupledaddedmassinfinitefrequency import CoupledAddedMassInfiniteFrequency
from .coupledaddedmasszerofrequency import CoupledAddedMassZeroFrequency
from .coupledfrequencydependentaddedmass import CoupledFrequencyDependentAddedMass
from .coupledfrequencydependentdamping import CoupledFrequencyDependentDamping
from .coupledretardationfunction import CoupledRetardationFunction

class CoupledRadiationDataGroup(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    frequencyDependentAddedMass : CoupledFrequencyDependentAddedMass
    frequencyDependentDamping : CoupledFrequencyDependentDamping
    retardationFunction : CoupledRetardationFunction
    addedMassZeroFrequency : CoupledAddedMassZeroFrequency
    addedMassInfiniteFrequency : CoupledAddedMassInfiniteFrequency
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.frequencyDependentAddedMass = None
        self.frequencyDependentDamping = None
        self.retardationFunction = None
        self.addedMassZeroFrequency = None
        self.addedMassInfiniteFrequency = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CoupledRadiationDataGroupBlueprint()


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
    def frequencyDependentAddedMass(self) -> CoupledFrequencyDependentAddedMass:
        """"""
        return self.__frequencyDependentAddedMass

    @frequencyDependentAddedMass.setter
    def frequencyDependentAddedMass(self, value: CoupledFrequencyDependentAddedMass):
        """Set frequencyDependentAddedMass"""
        self.__frequencyDependentAddedMass = value

    @property
    def frequencyDependentDamping(self) -> CoupledFrequencyDependentDamping:
        """"""
        return self.__frequencyDependentDamping

    @frequencyDependentDamping.setter
    def frequencyDependentDamping(self, value: CoupledFrequencyDependentDamping):
        """Set frequencyDependentDamping"""
        self.__frequencyDependentDamping = value

    @property
    def retardationFunction(self) -> CoupledRetardationFunction:
        """"""
        return self.__retardationFunction

    @retardationFunction.setter
    def retardationFunction(self, value: CoupledRetardationFunction):
        """Set retardationFunction"""
        self.__retardationFunction = value

    @property
    def addedMassZeroFrequency(self) -> CoupledAddedMassZeroFrequency:
        """"""
        return self.__addedMassZeroFrequency

    @addedMassZeroFrequency.setter
    def addedMassZeroFrequency(self, value: CoupledAddedMassZeroFrequency):
        """Set addedMassZeroFrequency"""
        self.__addedMassZeroFrequency = value

    @property
    def addedMassInfiniteFrequency(self) -> CoupledAddedMassInfiniteFrequency:
        """"""
        return self.__addedMassInfiniteFrequency

    @addedMassInfiniteFrequency.setter
    def addedMassInfiniteFrequency(self, value: CoupledAddedMassInfiniteFrequency):
        """Set addedMassInfiniteFrequency"""
        self.__addedMassInfiniteFrequency = value
