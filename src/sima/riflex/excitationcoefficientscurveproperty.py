# This an autogenerated file
# 
# Generated with ExcitationCoefficientsCurveProperty
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.excitationcoefficientscurveproperty import ExcitationCoefficientsCurvePropertyBlueprint
from typing import Dict
from sima.riflex.amplitudediameterpropertyitem import AmplitudeDiameterPropertyItem
from sima.riflex.excitationcoefficientsproperty import ExcitationCoefficientsProperty
from sima.sima.scriptablevalue import ScriptableValue

class ExcitationCoefficientsCurveProperty(ExcitationCoefficientsProperty):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    amplitudeDiameterPropertyItems : List[AmplitudeDiameterPropertyItem]
    """

    def __init__(self , description="", _id=None, name=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.amplitudeDiameterPropertyItems = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExcitationCoefficientsCurvePropertyBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def amplitudeDiameterPropertyItems(self) -> List[AmplitudeDiameterPropertyItem]:
        """"""
        return self.__amplitudeDiameterPropertyItems

    @amplitudeDiameterPropertyItems.setter
    def amplitudeDiameterPropertyItems(self, value: List[AmplitudeDiameterPropertyItem]):
        """Set amplitudeDiameterPropertyItems"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__amplitudeDiameterPropertyItems = value
