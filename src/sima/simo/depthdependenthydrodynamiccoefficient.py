# This an autogenerated file
# 
# Generated with DepthDependenthydrodynamicCoefficient
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.depthdependenthydrodynamiccoefficient import DepthDependenthydrodynamicCoefficientBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class DepthDependenthydrodynamicCoefficient(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    zd : float
         Vertical position(default 1.0)
    rvol : float
         Volume relative to fully submerged volume(default 1.0)
    ramx : float
         Relative added mass in 1. degree of freedom(default 1.0)
    ramy : float
         Relative added mass in 2. degree of freedom(default 1.0)
    ramz : float
         Relative added mass in 3. degree of freedom(default 1.0)
    rc11 : float
         Relative linear drag in 1. degree of freedom(default 0.0)
    rc12 : float
         Relative linear drag in 2. degree of freedom(default 0.0)
    rc13 : float
         Relative linear drag in 3. degree of freedom(default 0.0)
    rc21 : float
         Relative quadratic drag in 1. degree of freedom(default 0.0)
    rc22 : float
         Relative quadrativ drag in 2. degree of freedom(default 0.0)
    rc23 : float
         Relative quadratic drag in 3. degree of freedom(default 0.0)
    """

    def __init__(self , description="", zd=1.0, rvol=1.0, ramx=1.0, ramy=1.0, ramz=1.0, rc11=0.0, rc12=0.0, rc13=0.0, rc21=0.0, rc22=0.0, rc23=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.zd = zd
        self.rvol = rvol
        self.ramx = ramx
        self.ramy = ramy
        self.ramz = ramz
        self.rc11 = rc11
        self.rc12 = rc12
        self.rc13 = rc13
        self.rc21 = rc21
        self.rc22 = rc22
        self.rc23 = rc23
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DepthDependenthydrodynamicCoefficientBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def zd(self) -> float:
        """Vertical position"""
        return self.__zd

    @zd.setter
    def zd(self, value: float):
        """Set zd"""
        self.__zd = float(value)

    @property
    def rvol(self) -> float:
        """Volume relative to fully submerged volume"""
        return self.__rvol

    @rvol.setter
    def rvol(self, value: float):
        """Set rvol"""
        self.__rvol = float(value)

    @property
    def ramx(self) -> float:
        """Relative added mass in 1. degree of freedom"""
        return self.__ramx

    @ramx.setter
    def ramx(self, value: float):
        """Set ramx"""
        self.__ramx = float(value)

    @property
    def ramy(self) -> float:
        """Relative added mass in 2. degree of freedom"""
        return self.__ramy

    @ramy.setter
    def ramy(self, value: float):
        """Set ramy"""
        self.__ramy = float(value)

    @property
    def ramz(self) -> float:
        """Relative added mass in 3. degree of freedom"""
        return self.__ramz

    @ramz.setter
    def ramz(self, value: float):
        """Set ramz"""
        self.__ramz = float(value)

    @property
    def rc11(self) -> float:
        """Relative linear drag in 1. degree of freedom"""
        return self.__rc11

    @rc11.setter
    def rc11(self, value: float):
        """Set rc11"""
        self.__rc11 = float(value)

    @property
    def rc12(self) -> float:
        """Relative linear drag in 2. degree of freedom"""
        return self.__rc12

    @rc12.setter
    def rc12(self, value: float):
        """Set rc12"""
        self.__rc12 = float(value)

    @property
    def rc13(self) -> float:
        """Relative linear drag in 3. degree of freedom"""
        return self.__rc13

    @rc13.setter
    def rc13(self, value: float):
        """Set rc13"""
        self.__rc13 = float(value)

    @property
    def rc21(self) -> float:
        """Relative quadratic drag in 1. degree of freedom"""
        return self.__rc21

    @rc21.setter
    def rc21(self, value: float):
        """Set rc21"""
        self.__rc21 = float(value)

    @property
    def rc22(self) -> float:
        """Relative quadrativ drag in 2. degree of freedom"""
        return self.__rc22

    @rc22.setter
    def rc22(self, value: float):
        """Set rc22"""
        self.__rc22 = float(value)

    @property
    def rc23(self) -> float:
        """Relative quadratic drag in 3. degree of freedom"""
        return self.__rc23

    @rc23.setter
    def rc23(self, value: float):
        """Set rc23"""
        self.__rc23 = float(value)
