# This an autogenerated file
# 
# Generated with DoubleVariable
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.doublevariable import DoubleVariableBlueprint
from typing import Dict
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.variable import Variable

class DoubleVariable(Variable):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    value : float
         The current value for the variable(default 0.0)
    unit : str
         unit of variable(default '-')
    """

    def __init__(self , description="", _id=None, name=None, value=0.0, unit='-', **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.value = value
        self.unit = unit
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DoubleVariableBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def value(self) -> float:
        """The current value for the variable"""
        return self.__value

    @value.setter
    def value(self, value: float):
        """Set value"""
        self.__value = float(value)

    @property
    def unit(self) -> str:
        """unit of variable"""
        return self.__unit

    @unit.setter
    def unit(self, value: str):
        """Set unit"""
        self.__unit = str(value)
