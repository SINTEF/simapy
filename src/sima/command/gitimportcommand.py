# This an autogenerated file
# 
# Generated with GitImportCommand
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.gitimportcommand import GitImportCommandBlueprint
from typing import Dict
from .command import Command
from sima.sima import Property
from sima.sima import ScriptableValue

class GitImportCommand(Command):
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
    uri : str
         URI of the git repository(default None)
    branch : str
         Branch name(default 'master')
    location : str
         location of repository on disk (default is within workspace)(default None)
    """

    def __init__(self , description="", branch='master', **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.parameters = list()
        self.uri = None
        self.branch = branch
        self.location = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GitImportCommandBlueprint()


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
    def uri(self) -> str:
        """URI of the git repository"""
        return self.__uri

    @uri.setter
    def uri(self, value: str):
        """Set uri"""
        self.__uri = value

    @property
    def branch(self) -> str:
        """Branch name"""
        return self.__branch

    @branch.setter
    def branch(self, value: str):
        """Set branch"""
        self.__branch = value

    @property
    def location(self) -> str:
        """location of repository on disk (default is within workspace)"""
        return self.__location

    @location.setter
    def location(self, value: str):
        """Set location"""
        self.__location = value