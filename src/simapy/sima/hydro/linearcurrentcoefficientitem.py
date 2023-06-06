# This an autogenerated file
# 
# Generated with LinearCurrentCoefficientItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.linearcurrentcoefficientitem import LinearCurrentCoefficientItemBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class LinearCurrentCoefficientItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    direction : float
         Direction(default 0.0)
    c11 : float
         Linear current force coefficient for 1. degree of freedom(default 0.0)
    c12 : float
         Linear current force coefficient for 2. degree of freedom(default 0.0)
    c13 : float
         Linear current force coefficient for 3. degree of freedom(default 0.0)
    c14 : float
         Linear current force coefficient for 4. degree of freedom(default 0.0)
    c15 : float
         Linear current force coefficient for 5. degree of freedom(default 0.0)
    c16 : float
         Linear current force coefficient for 6. degree of freedom(default 0.0)
    """

    def __init__(self , description="", direction=0.0, c11=0.0, c12=0.0, c13=0.0, c14=0.0, c15=0.0, c16=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.direction = direction
        self.c11 = c11
        self.c12 = c12
        self.c13 = c13
        self.c14 = c14
        self.c15 = c15
        self.c16 = c16
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return LinearCurrentCoefficientItemBlueprint()


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
    def direction(self) -> float:
        """Direction"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def c11(self) -> float:
        """Linear current force coefficient for 1. degree of freedom"""
        return self.__c11

    @c11.setter
    def c11(self, value: float):
        """Set c11"""
        self.__c11 = float(value)

    @property
    def c12(self) -> float:
        """Linear current force coefficient for 2. degree of freedom"""
        return self.__c12

    @c12.setter
    def c12(self, value: float):
        """Set c12"""
        self.__c12 = float(value)

    @property
    def c13(self) -> float:
        """Linear current force coefficient for 3. degree of freedom"""
        return self.__c13

    @c13.setter
    def c13(self, value: float):
        """Set c13"""
        self.__c13 = float(value)

    @property
    def c14(self) -> float:
        """Linear current force coefficient for 4. degree of freedom"""
        return self.__c14

    @c14.setter
    def c14(self, value: float):
        """Set c14"""
        self.__c14 = float(value)

    @property
    def c15(self) -> float:
        """Linear current force coefficient for 5. degree of freedom"""
        return self.__c15

    @c15.setter
    def c15(self, value: float):
        """Set c15"""
        self.__c15 = float(value)

    @property
    def c16(self) -> float:
        """Linear current force coefficient for 6. degree of freedom"""
        return self.__c16

    @c16.setter
    def c16(self, value: float):
        """Set c16"""
        self.__c16 = float(value)
