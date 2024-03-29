# This an autogenerated file
# 
# Generated with WaveDriftDampingItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wavedriftdampingitem import WaveDriftDampingItemBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class WaveDriftDampingItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    period : float
         Period(default 0.0)
    wd1 : float
         Wave drift damping coefficient surge. Relative change in drift force for unit velocity.(default 0.0)
    wd2 : float
         Wave drift damping coefficient sway. Relative change in drift force for unit velocity.(default 0.0)
    wd3 : float
         Wave drift damping coefficient heave. Relative change in drift force for unit velocity.(default 0.0)
    wd4 : float
         Wave drift damping coefficient roll. Relative change in drift force for unit velocity.(default 0.0)
    wd5 : float
         Wave drift damping coefficient pitch. Relative change in drift force for unit velocity.(default 0.0)
    wd6 : float
         Wave drift damping coefficient yaw. Relative change in drift force for unit velocity.(default 0.0)
    """

    def __init__(self , description="", period=0.0, wd1=0.0, wd2=0.0, wd3=0.0, wd4=0.0, wd5=0.0, wd6=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.period = period
        self.wd1 = wd1
        self.wd2 = wd2
        self.wd3 = wd3
        self.wd4 = wd4
        self.wd5 = wd5
        self.wd6 = wd6
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WaveDriftDampingItemBlueprint()


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
    def period(self) -> float:
        """Period"""
        return self.__period

    @period.setter
    def period(self, value: float):
        """Set period"""
        self.__period = float(value)

    @property
    def wd1(self) -> float:
        """Wave drift damping coefficient surge. Relative change in drift force for unit velocity."""
        return self.__wd1

    @wd1.setter
    def wd1(self, value: float):
        """Set wd1"""
        self.__wd1 = float(value)

    @property
    def wd2(self) -> float:
        """Wave drift damping coefficient sway. Relative change in drift force for unit velocity."""
        return self.__wd2

    @wd2.setter
    def wd2(self, value: float):
        """Set wd2"""
        self.__wd2 = float(value)

    @property
    def wd3(self) -> float:
        """Wave drift damping coefficient heave. Relative change in drift force for unit velocity."""
        return self.__wd3

    @wd3.setter
    def wd3(self, value: float):
        """Set wd3"""
        self.__wd3 = float(value)

    @property
    def wd4(self) -> float:
        """Wave drift damping coefficient roll. Relative change in drift force for unit velocity."""
        return self.__wd4

    @wd4.setter
    def wd4(self, value: float):
        """Set wd4"""
        self.__wd4 = float(value)

    @property
    def wd5(self) -> float:
        """Wave drift damping coefficient pitch. Relative change in drift force for unit velocity."""
        return self.__wd5

    @wd5.setter
    def wd5(self, value: float):
        """Set wd5"""
        self.__wd5 = float(value)

    @property
    def wd6(self) -> float:
        """Wave drift damping coefficient yaw. Relative change in drift force for unit velocity."""
        return self.__wd6

    @wd6.setter
    def wd6(self, value: float):
        """Set wd6"""
        self.__wd6 = float(value)
