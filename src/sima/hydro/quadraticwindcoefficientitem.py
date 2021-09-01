# This an autogenerated file
# 
# Generated with QuadraticWindCoefficientItem
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.quadraticwindcoefficientitem import QuadraticWindCoefficientItemBlueprint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class QuadraticWindCoefficientItem(MOAO):
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
    direction : float
         Direction(default 0.0)
    c1 : float
         Wind force coefficient for 1. degree of freedom(default 0.0)
    c2 : float
         Wind force coefficient for 2. degree of freedom(default 0.0)
    c3 : float
         Wind force coefficient for 3. degree of freedom(default 0.0)
    c4 : float
         Wind force coefficient for 4. degree of freedom(default 0.0)
    c5 : float
         Wind force coefficient for 5. degree of freedom(default 0.0)
    c6 : float
         Wind force coefficient for 6. degree of freedom(default 0.0)
    """

    def __init__(self , name:str="", description:str="", _id:str="", direction:float=0.0, c1:float=0.0, c2:float=0.0, c3:float=0.0, c4:float=0.0, c5:float=0.0, c6:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__direction = direction
        self.__c1 = c1
        self.__c2 = c2
        self.__c3 = c3
        self.__c4 = c4
        self.__c5 = c5
        self.__c6 = c6
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return QuadraticWindCoefficientItemBlueprint()


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
    def direction(self) -> float:
        """Direction"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def c1(self) -> float:
        """Wind force coefficient for 1. degree of freedom"""
        return self.__c1

    @c1.setter
    def c1(self, value: float):
        """Set c1"""
        self.__c1 = float(value)

    @property
    def c2(self) -> float:
        """Wind force coefficient for 2. degree of freedom"""
        return self.__c2

    @c2.setter
    def c2(self, value: float):
        """Set c2"""
        self.__c2 = float(value)

    @property
    def c3(self) -> float:
        """Wind force coefficient for 3. degree of freedom"""
        return self.__c3

    @c3.setter
    def c3(self, value: float):
        """Set c3"""
        self.__c3 = float(value)

    @property
    def c4(self) -> float:
        """Wind force coefficient for 4. degree of freedom"""
        return self.__c4

    @c4.setter
    def c4(self, value: float):
        """Set c4"""
        self.__c4 = float(value)

    @property
    def c5(self) -> float:
        """Wind force coefficient for 5. degree of freedom"""
        return self.__c5

    @c5.setter
    def c5(self, value: float):
        """Set c5"""
        self.__c5 = float(value)

    @property
    def c6(self) -> float:
        """Wind force coefficient for 6. degree of freedom"""
        return self.__c6

    @c6.setter
    def c6(self, value: float):
        """Set c6"""
        self.__c6 = float(value)
