# This an autogenerated file
# 
# Generated with VerificationTask
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.verificationtask import VerificationTaskBlueprint
from sima.doc.test import Test
from sima.sima.doublevariable import DoubleVariable
from sima.sima.integervariable import IntegerVariable
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.simascript import SIMAScript
from sima.sima.stringvariable import StringVariable
from sima.sima.task import Task
from sima.workflow.workflow import Workflow

class VerificationTask(Task):
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
    doubleVariables : List[DoubleVariable]
    integerVariables : List[IntegerVariable]
    stringVariables : List[StringVariable]
    runNumber : int
         (default 0)
    scripts : List[SIMAScript]
    tests : List[Test]
    workflows : List[Workflow]
    """

    def __init__(self , name:str="", description:str="", _id:str="", runNumber:int=0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__doubleVariables = list()
        self.__integerVariables = list()
        self.__stringVariables = list()
        self.__runNumber = runNumber
        self.__scripts = list()
        self.__tests = list()
        self.__workflows = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return VerificationTaskBlueprint()


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
    def doubleVariables(self) -> List[DoubleVariable]:
        """"""
        return self.__doubleVariables

    @doubleVariables.setter
    def doubleVariables(self, value: List[DoubleVariable]):
        """Set doubleVariables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__doubleVariables = value

    @property
    def integerVariables(self) -> List[IntegerVariable]:
        """"""
        return self.__integerVariables

    @integerVariables.setter
    def integerVariables(self, value: List[IntegerVariable]):
        """Set integerVariables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__integerVariables = value

    @property
    def stringVariables(self) -> List[StringVariable]:
        """"""
        return self.__stringVariables

    @stringVariables.setter
    def stringVariables(self, value: List[StringVariable]):
        """Set stringVariables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__stringVariables = value

    @property
    def runNumber(self) -> int:
        """"""
        return self.__runNumber

    @runNumber.setter
    def runNumber(self, value: int):
        """Set runNumber"""
        self.__runNumber = int(value)

    @property
    def scripts(self) -> List[SIMAScript]:
        """"""
        return self.__scripts

    @scripts.setter
    def scripts(self, value: List[SIMAScript]):
        """Set scripts"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__scripts = value

    @property
    def tests(self) -> List[Test]:
        """"""
        return self.__tests

    @tests.setter
    def tests(self, value: List[Test]):
        """Set tests"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__tests = value

    @property
    def workflows(self) -> List[Workflow]:
        """"""
        return self.__workflows

    @workflows.setter
    def workflows(self, value: List[Workflow]):
        """Set workflows"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__workflows = value
