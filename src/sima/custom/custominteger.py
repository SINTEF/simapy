# This an autogenerated file
# 
# Generated with CustomInteger
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.custominteger import CustomIntegerBlueprint
from typing import Dict
from .parameterfield import ParameterField
from sima.sima import Named
from sima.sima import ScriptableValue

class CustomInteger(ParameterField,Named):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    label : str
         (default None)
    tooltip : str
         (default None)
    value : int
         (default 0)
    constraints : str
         Give a valid range for a number: Use <,> for excluding and [] for including.\nExampless: \n- [0,4] Number from and including 0 to and including 4\n- <0,4> From and to, excluding \n- <,0> All negative numbers excluding 0\n- [0,> All positive numbers, including 0\n(default None)
    """

    def __init__(self , description="", value=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.label = None
        self.tooltip = None
        self.value = value
        self.constraints = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomIntegerBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = value

    @property
    def tooltip(self) -> str:
        """"""
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, value: str):
        """Set tooltip"""
        self.__tooltip = value

    @property
    def value(self) -> int:
        """"""
        return self.__value

    @value.setter
    def value(self, value: int):
        """Set value"""
        self.__value = int(value)

    @property
    def constraints(self) -> str:
        """Give a valid range for a number: Use <,> for excluding and [] for including.
Exampless: 
- [0,4] Number from and including 0 to and including 4
- <0,4> From and to, excluding 
- <,0> All negative numbers excluding 0
- [0,> All positive numbers, including 0
"""
        return self.__constraints

    @constraints.setter
    def constraints(self, value: str):
        """Set constraints"""
        self.__constraints = value
