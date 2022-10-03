# This an autogenerated file
# 
# Generated with ExcitationCoefficientsNonDimensionalFrequencyItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.excitationcoefficientsnondimensionalfrequencyitem import ExcitationCoefficientsNonDimensionalFrequencyItemBlueprint
from typing import Dict
from sima.riflex.amplitudediameterexcitationcoefficientitem import AmplitudeDiameterExcitationCoefficientItem
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ExcitationCoefficientsNonDimensionalFrequencyItem(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    nonDimensionalFrequency : float
         Non-dimensional frequency(default 0.0)
    amplitudeExcitationRatioProperties : List[AmplitudeDiameterExcitationCoefficientItem]
    """

    def __init__(self , _id="", nonDimensionalFrequency=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.nonDimensionalFrequency = nonDimensionalFrequency
        self.amplitudeExcitationRatioProperties = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExcitationCoefficientsNonDimensionalFrequencyItemBlueprint()


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
    def nonDimensionalFrequency(self) -> float:
        """Non-dimensional frequency"""
        return self.__nonDimensionalFrequency

    @nonDimensionalFrequency.setter
    def nonDimensionalFrequency(self, value: float):
        """Set nonDimensionalFrequency"""
        self.__nonDimensionalFrequency = float(value)

    @property
    def amplitudeExcitationRatioProperties(self) -> List[AmplitudeDiameterExcitationCoefficientItem]:
        """"""
        return self.__amplitudeExcitationRatioProperties

    @amplitudeExcitationRatioProperties.setter
    def amplitudeExcitationRatioProperties(self, value: List[AmplitudeDiameterExcitationCoefficientItem]):
        """Set amplitudeExcitationRatioProperties"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__amplitudeExcitationRatioProperties = value
