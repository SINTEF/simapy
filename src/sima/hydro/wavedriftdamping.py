# This an autogenerated file
# 
# Generated with WaveDriftDamping
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wavedriftdamping import WaveDriftDampingBlueprint
from numpy import ndarray,asarray
from sima.hydro.directionsymmetry import DirectionSymmetry
from sima.hydro.wavedriftdampingdofitem import WaveDriftDampingDofItem
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class WaveDriftDamping(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    directions : ndarray
    frequencies : ndarray
    symmetry : DirectionSymmetry
    items : List[WaveDriftDampingDofItem]
    """

    def __init__(self , description="", _id=None, symmetry=DirectionSymmetry.NO_SYMMETRY, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.directions = ndarray(1)
        self.frequencies = ndarray(1)
        self.symmetry = symmetry
        self.items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WaveDriftDampingBlueprint()


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
    def directions(self) -> ndarray:
        """"""
        return self.__directions

    @directions.setter
    def directions(self, value: ndarray):
        """Set directions"""
        self.__directions = asarray(value)

    @property
    def frequencies(self) -> ndarray:
        """"""
        return self.__frequencies

    @frequencies.setter
    def frequencies(self, value: ndarray):
        """Set frequencies"""
        self.__frequencies = asarray(value)

    @property
    def symmetry(self) -> DirectionSymmetry:
        """"""
        return self.__symmetry

    @symmetry.setter
    def symmetry(self, value: DirectionSymmetry):
        """Set symmetry"""
        self.__symmetry = value

    @property
    def items(self) -> List[WaveDriftDampingDofItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[WaveDriftDampingDofItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__items = value
