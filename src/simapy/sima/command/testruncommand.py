# This an autogenerated file
# 
# Generated with TestRunCommand
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.testruncommand import TestRunCommandBlueprint
from typing import Dict
from ..sima import Command
from ..sima import Property
from ..sima import ScriptableValue

class TestRunCommand(Command):
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
    task : str
         Name of Verification task(default None)
    test : str
         Name of test to run(default None)
    file : str
         File path to export json status report(default None)
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.parameters = list()
        self.task = None
        self.test = None
        self.file = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TestRunCommandBlueprint()


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
    def task(self) -> str:
        """Name of Verification task"""
        return self.__task

    @task.setter
    def task(self, value: str):
        """Set task"""
        self.__task = value

    @property
    def test(self) -> str:
        """Name of test to run"""
        return self.__test

    @test.setter
    def test(self, value: str):
        """Set test"""
        self.__test = value

    @property
    def file(self) -> str:
        """File path to export json status report"""
        return self.__file

    @file.setter
    def file(self, value: str):
        """Set file"""
        self.__file = value
