# This an autogenerated file
# 
# Generated with ExternalPythonForce
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.externalpythonforce import ExternalPythonForceBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import ScriptableValue
from ..sima import SingleValue

class ExternalPythonForce(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    file : str
         (default None)
    className : str
         Python class name contained in the python file(default '0')
    parameters : List[SingleValue]
    """

    def __init__(self , description="", className='0', **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.file = None
        self.className = className
        self.parameters = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExternalPythonForceBlueprint()


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
    def file(self) -> str:
        """"""
        return self.__file

    @file.setter
    def file(self, value: str):
        """Set file"""
        self.__file = value

    @property
    def className(self) -> str:
        """Python class name contained in the python file"""
        return self.__className

    @className.setter
    def className(self, value: str):
        """Set className"""
        self.__className = value

    @property
    def parameters(self) -> List[SingleValue]:
        """"""
        return self.__parameters

    @parameters.setter
    def parameters(self, value: List[SingleValue]):
        """Set parameters"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__parameters = value
