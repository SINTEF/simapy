# This an autogenerated file
# 
# Generated with SurfaceProximityReductionFactor
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.surfaceproximityreductionfactor import SurfaceProximityReductionFactorBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class SurfaceProximityReductionFactor(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    zd : float
         Z/D value(default 0.0)
    reductionFactor : float
         Reduction factor(default 0.0)
    """

    def __init__(self , description="", _id=None, zd=0.0, reductionFactor=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.zd = zd
        self.reductionFactor = reductionFactor
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SurfaceProximityReductionFactorBlueprint()


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
    def zd(self) -> float:
        """Z/D value"""
        return self.__zd

    @zd.setter
    def zd(self, value: float):
        """Set zd"""
        self.__zd = float(value)

    @property
    def reductionFactor(self) -> float:
        """Reduction factor"""
        return self.__reductionFactor

    @reductionFactor.setter
    def reductionFactor(self, value: float):
        """Set reductionFactor"""
        self.__reductionFactor = float(value)
