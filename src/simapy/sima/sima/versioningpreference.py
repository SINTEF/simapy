# This an autogenerated file
# 
# Generated with VersioningPreference
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.versioningpreference import VersioningPreferenceBlueprint
from typing import Dict
from .scriptablevalue import ScriptableValue
from .simapreference import SIMAPreference

class VersioningPreference(SIMAPreference):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    userHome : str
         Override user home folder(default None)
    sshFolder : str
         Override ssh folder(default None)
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.userHome = None
        self.sshFolder = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return VersioningPreferenceBlueprint()


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
    def userHome(self) -> str:
        """Override user home folder"""
        return self.__userHome

    @userHome.setter
    def userHome(self, value: str):
        """Set userHome"""
        self.__userHome = value

    @property
    def sshFolder(self) -> str:
        """Override ssh folder"""
        return self.__sshFolder

    @sshFolder.setter
    def sshFolder(self, value: str):
        """Set sshFolder"""
        self.__sshFolder = value
