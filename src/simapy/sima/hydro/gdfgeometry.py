# This an autogenerated file
# 
# Generated with GDFGeometry
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.gdfgeometry import GDFGeometryBlueprint
from numpy import ndarray,asarray
from ..sima import MOAO
from ..sima import ScriptableValue

class GDFGeometry(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    xSymmetry : int
         (default 0)
    ySymmetry : int
         (default 0)
    nValues : int
         (default 0)
    values : ndarray of float
    dimensionalLength : float
         (default 1.0)
    gravitationalAcceleration : float
         (default 9.81)
    """

    def __init__(self , description="", xSymmetry=0, ySymmetry=0, nValues=0, dimensionalLength=1.0, gravitationalAcceleration=9.81, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.xSymmetry = xSymmetry
        self.ySymmetry = ySymmetry
        self.nValues = nValues
        self.values = []
        self.dimensionalLength = dimensionalLength
        self.gravitationalAcceleration = gravitationalAcceleration
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GDFGeometryBlueprint()


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
    def xSymmetry(self) -> int:
        """"""
        return self.__xSymmetry

    @xSymmetry.setter
    def xSymmetry(self, value: int):
        """Set xSymmetry"""
        self.__xSymmetry = int(value)

    @property
    def ySymmetry(self) -> int:
        """"""
        return self.__ySymmetry

    @ySymmetry.setter
    def ySymmetry(self, value: int):
        """Set ySymmetry"""
        self.__ySymmetry = int(value)

    @property
    def nValues(self) -> int:
        """"""
        return self.__nValues

    @nValues.setter
    def nValues(self, value: int):
        """Set nValues"""
        self.__nValues = int(value)

    @property
    def values(self) -> ndarray:
        """"""
        return self.__values

    @values.setter
    def values(self, value: ndarray):
        """Set values"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__values = array

    @property
    def dimensionalLength(self) -> float:
        """"""
        return self.__dimensionalLength

    @dimensionalLength.setter
    def dimensionalLength(self, value: float):
        """Set dimensionalLength"""
        self.__dimensionalLength = float(value)

    @property
    def gravitationalAcceleration(self) -> float:
        """"""
        return self.__gravitationalAcceleration

    @gravitationalAcceleration.setter
    def gravitationalAcceleration(self, value: float):
        """Set gravitationalAcceleration"""
        self.__gravitationalAcceleration = float(value)