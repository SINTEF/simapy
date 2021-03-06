# This an autogenerated file
# 
# Generated with RadiationDataGroup
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.radiationdatagroup import RadiationDataGroupBlueprint
from typing import Dict
from sima.hydro.addedmassinfinitefrequency import AddedMassInfiniteFrequency
from sima.hydro.addedmasszerofrequency import AddedMassZeroFrequency
from sima.hydro.frequencydependentaddedmass import FrequencyDependentAddedMass
from sima.hydro.frequencydependentdamping import FrequencyDependentDamping
from sima.hydro.retardationfunction import RetardationFunction
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class RadiationDataGroup(MOAO):
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
    frequencyDependentAddedMass : FrequencyDependentAddedMass
    frequencyDependentDamping : FrequencyDependentDamping
    retardationFunction : RetardationFunction
    addedMassZeroFrequency : AddedMassZeroFrequency
    addedMassInfiniteFrequency : AddedMassInfiniteFrequency
    """

    def __init__(self , name="", description="", _id="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
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
        return RadiationDataGroupBlueprint()


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
    def frequencyDependentAddedMass(self) -> FrequencyDependentAddedMass:
        """"""
        return self.__frequencyDependentAddedMass

    @frequencyDependentAddedMass.setter
    def frequencyDependentAddedMass(self, value: FrequencyDependentAddedMass):
        """Set frequencyDependentAddedMass"""
        self.__frequencyDependentAddedMass = value

    @property
    def frequencyDependentDamping(self) -> FrequencyDependentDamping:
        """"""
        return self.__frequencyDependentDamping

    @frequencyDependentDamping.setter
    def frequencyDependentDamping(self, value: FrequencyDependentDamping):
        """Set frequencyDependentDamping"""
        self.__frequencyDependentDamping = value

    @property
    def retardationFunction(self) -> RetardationFunction:
        """"""
        return self.__retardationFunction

    @retardationFunction.setter
    def retardationFunction(self, value: RetardationFunction):
        """Set retardationFunction"""
        self.__retardationFunction = value

    @property
    def addedMassZeroFrequency(self) -> AddedMassZeroFrequency:
        """"""
        return self.__addedMassZeroFrequency

    @addedMassZeroFrequency.setter
    def addedMassZeroFrequency(self, value: AddedMassZeroFrequency):
        """Set addedMassZeroFrequency"""
        self.__addedMassZeroFrequency = value

    @property
    def addedMassInfiniteFrequency(self) -> AddedMassInfiniteFrequency:
        """"""
        return self.__addedMassInfiniteFrequency

    @addedMassInfiniteFrequency.setter
    def addedMassInfiniteFrequency(self, value: AddedMassInfiniteFrequency):
        """Set addedMassInfiniteFrequency"""
        self.__addedMassInfiniteFrequency = value
