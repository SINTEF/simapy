# This an autogenerated file
# 
# Generated with SoilCapacityElement
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.soilcapacityelement import SoilCapacityElementBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class SoilCapacityElement(MOAO):
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
    dCap : float
         Penetration relative to ZCONT (positive upwards)(default 0.0)
    soilFr : float
         Soil capacity against failure at soil surface(default 0.0)
    frcDep : float
         Depth of each new soil failure(default 0.0)
    pSuct : float
         Suction pressure(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", dCap:float=0.0, soilFr:float=0.0, frcDep:float=0.0, pSuct:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__dCap = dCap
        self.__soilFr = soilFr
        self.__frcDep = frcDep
        self.__pSuct = pSuct
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SoilCapacityElementBlueprint()


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
    def dCap(self) -> float:
        """Penetration relative to ZCONT (positive upwards)"""
        return self.__dCap

    @dCap.setter
    def dCap(self, value: float):
        """Set dCap"""
        self.__dCap = float(value)

    @property
    def soilFr(self) -> float:
        """Soil capacity against failure at soil surface"""
        return self.__soilFr

    @soilFr.setter
    def soilFr(self, value: float):
        """Set soilFr"""
        self.__soilFr = float(value)

    @property
    def frcDep(self) -> float:
        """Depth of each new soil failure"""
        return self.__frcDep

    @frcDep.setter
    def frcDep(self, value: float):
        """Set frcDep"""
        self.__frcDep = float(value)

    @property
    def pSuct(self) -> float:
        """Suction pressure"""
        return self.__pSuct

    @pSuct.setter
    def pSuct(self, value: float):
        """Set pSuct"""
        self.__pSuct = float(value)
