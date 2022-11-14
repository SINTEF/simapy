# This an autogenerated file
# 
# Generated with ForceDampingCharacteristic
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.forcedampingcharacteristic import ForceDampingCharacteristicBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.forcedampingitem import ForceDampingItem
from sima.simo.interpolation import Interpolation

class ForceDampingCharacteristic(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    dampingExponent : float
         Exponent of velocity in damping term(default 1.0)
    dampingInterpolation : Interpolation
         Interpolation method for damping
    forceInterpolation : Interpolation
         Interpolation method for force
    items : List[ForceDampingItem]
    """

    def __init__(self , description="", _id=None, dampingExponent=1.0, dampingInterpolation=Interpolation.LINEAR, forceInterpolation=Interpolation.LINEAR, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.dampingExponent = dampingExponent
        self.dampingInterpolation = dampingInterpolation
        self.forceInterpolation = forceInterpolation
        self.items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ForceDampingCharacteristicBlueprint()


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
    def dampingExponent(self) -> float:
        """Exponent of velocity in damping term"""
        return self.__dampingExponent

    @dampingExponent.setter
    def dampingExponent(self, value: float):
        """Set dampingExponent"""
        self.__dampingExponent = float(value)

    @property
    def dampingInterpolation(self) -> Interpolation:
        """Interpolation method for damping"""
        return self.__dampingInterpolation

    @dampingInterpolation.setter
    def dampingInterpolation(self, value: Interpolation):
        """Set dampingInterpolation"""
        self.__dampingInterpolation = value

    @property
    def forceInterpolation(self) -> Interpolation:
        """Interpolation method for force"""
        return self.__forceInterpolation

    @forceInterpolation.setter
    def forceInterpolation(self, value: Interpolation):
        """Set forceInterpolation"""
        self.__forceInterpolation = value

    @property
    def items(self) -> List[ForceDampingItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[ForceDampingItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__items = value
