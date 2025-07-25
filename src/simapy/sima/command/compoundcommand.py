# This an autogenerated file
# 
# Generated with CompoundCommand
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.compoundcommand import CompoundCommandBlueprint
from typing import Dict
from ..sima import Command
from ..sima import Property
from ..sima import ScriptableValue

class CompoundCommand(Command):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    parameters : List[Property]
         Additional parameters
    commands : List[Command]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.parameters = list()
        self.commands = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CompoundCommandBlueprint()


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
    def parameters(self) -> List[Property]:
        """Additional parameters"""
        return self.__parameters

    @parameters.setter
    def parameters(self, value: List[Property]):
        """Set parameters"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__parameters = value

    @property
    def commands(self) -> List[Command]:
        """"""
        return self.__commands

    @commands.setter
    def commands(self, value: List[Command]):
        """Set commands"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__commands = value
