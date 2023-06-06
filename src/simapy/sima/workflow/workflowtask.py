# This an autogenerated file
# 
# Generated with WorkflowTask
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.workflowtask import WorkflowTaskBlueprint
from typing import Dict
from ..sima import DoubleVariable
from ..sima import IntegerVariable
from ..sima import SIMAScript
from ..sima import ScriptableValue
from ..sima import StringVariable
from ..sima import Task
from .workflow import Workflow
from .workflowcontainerpackage import WorkflowContainerPackage

class WorkflowTask(Task):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    doubleVariables : List[DoubleVariable]
    integerVariables : List[IntegerVariable]
    stringVariables : List[StringVariable]
    runNumber : int
         (default 0)
    scripts : List[SIMAScript]
    packages : List[WorkflowContainerPackage]
    workflows : List[Workflow]
    """

    def __init__(self , description="", runNumber=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.doubleVariables = list()
        self.integerVariables = list()
        self.stringVariables = list()
        self.runNumber = runNumber
        self.scripts = list()
        self.packages = list()
        self.workflows = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WorkflowTaskBlueprint()


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
    def doubleVariables(self) -> List[DoubleVariable]:
        """"""
        return self.__doubleVariables

    @doubleVariables.setter
    def doubleVariables(self, value: List[DoubleVariable]):
        """Set doubleVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__doubleVariables = value

    @property
    def integerVariables(self) -> List[IntegerVariable]:
        """"""
        return self.__integerVariables

    @integerVariables.setter
    def integerVariables(self, value: List[IntegerVariable]):
        """Set integerVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__integerVariables = value

    @property
    def stringVariables(self) -> List[StringVariable]:
        """"""
        return self.__stringVariables

    @stringVariables.setter
    def stringVariables(self, value: List[StringVariable]):
        """Set stringVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scripts = value

    @property
    def packages(self) -> List[WorkflowContainerPackage]:
        """"""
        return self.__packages

    @packages.setter
    def packages(self, value: List[WorkflowContainerPackage]):
        """Set packages"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__packages = value

    @property
    def workflows(self) -> List[Workflow]:
        """"""
        return self.__workflows

    @workflows.setter
    def workflows(self, value: List[Workflow]):
        """Set workflows"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__workflows = value
