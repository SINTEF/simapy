# This an autogenerated file
# 
# Generated with WorkflowContainerPackage
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.workflowcontainerpackage import WorkflowContainerPackageBlueprint
from typing import Dict
from ..sima import Named
from ..sima import ScriptableValue
from .workflow import Workflow

class WorkflowContainerPackage(Named):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    packages : List[WorkflowContainerPackage]
    workflows : List[Workflow]
    visible : bool
         Make all workflows directly contained in this package visible outside of the task(default False)
    """

    def __init__(self , description="", visible=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.packages = list()
        self.workflows = list()
        self.visible = visible
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WorkflowContainerPackageBlueprint()


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

    @property
    def visible(self) -> bool:
        """Make all workflows directly contained in this package visible outside of the task"""
        return self.__visible

    @visible.setter
    def visible(self, value: bool):
        """Set visible"""
        self.__visible = bool(value)
