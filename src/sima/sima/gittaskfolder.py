# This an autogenerated file
# 
# Generated with GitTaskFolder
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.gittaskfolder import GitTaskFolderBlueprint
from typing import Dict
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.task import Task
from sima.sima.taskfolder import TaskFolder

class GitTaskFolder(TaskFolder):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    childFolders : List[TaskFolder]
    childTasks : List[Task]
    visible : bool
         (default True)
    remoteURI : str
         (default None)
    branch : str
         (default None)
    lastCommitMessage : str
         (default None)
    repositoryFolder : str
         (default None)
    """

    def __init__(self , description="", visible=True, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.childFolders = list()
        self.childTasks = list()
        self.visible = visible
        self.remoteURI = None
        self.branch = None
        self.lastCommitMessage = None
        self.repositoryFolder = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GitTaskFolderBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
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
    def childFolders(self) -> List[TaskFolder]:
        """"""
        return self.__childFolders

    @childFolders.setter
    def childFolders(self, value: List[TaskFolder]):
        """Set childFolders"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__childFolders = value

    @property
    def childTasks(self) -> List[Task]:
        """"""
        return self.__childTasks

    @childTasks.setter
    def childTasks(self, value: List[Task]):
        """Set childTasks"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__childTasks = value

    @property
    def visible(self) -> bool:
        """"""
        return self.__visible

    @visible.setter
    def visible(self, value: bool):
        """Set visible"""
        self.__visible = bool(value)

    @property
    def remoteURI(self) -> str:
        """"""
        return self.__remoteURI

    @remoteURI.setter
    def remoteURI(self, value: str):
        """Set remoteURI"""
        self.__remoteURI = value

    @property
    def branch(self) -> str:
        """"""
        return self.__branch

    @branch.setter
    def branch(self, value: str):
        """Set branch"""
        self.__branch = value

    @property
    def lastCommitMessage(self) -> str:
        """"""
        return self.__lastCommitMessage

    @lastCommitMessage.setter
    def lastCommitMessage(self, value: str):
        """Set lastCommitMessage"""
        self.__lastCommitMessage = value

    @property
    def repositoryFolder(self) -> str:
        """"""
        return self.__repositoryFolder

    @repositoryFolder.setter
    def repositoryFolder(self, value: str):
        """Set repositoryFolder"""
        self.__repositoryFolder = value
