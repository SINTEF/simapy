# This an autogenerated file
# 
# Generated with SIMOPreference
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.simopreference import SIMOPreferenceBlueprint
from numpy import ndarray,asarray
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.simapreference import SIMAPreference

class SIMOPreference(SIMAPreference):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    selectedVersion : str
         Selected SIMO/RIFLEX installation(default 'Default')
    locations : ndarray
    frevesLocation : str
         Freves bin folder(default None)
    frelinLocation : str
         Frelin bin folder(default None)
    """

    def __init__(self , description="", selectedVersion='Default', **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.selectedVersion = selectedVersion
        self.locations = ndarray(1)
        self.frevesLocation = None
        self.frelinLocation = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SIMOPreferenceBlueprint()


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
    def selectedVersion(self) -> str:
        """Selected SIMO/RIFLEX installation"""
        return self.__selectedVersion

    @selectedVersion.setter
    def selectedVersion(self, value: str):
        """Set selectedVersion"""
        self.__selectedVersion = value

    @property
    def locations(self) -> ndarray:
        """"""
        return self.__locations

    @locations.setter
    def locations(self, value: ndarray):
        """Set locations"""
        self.__locations = asarray(value)

    @property
    def frevesLocation(self) -> str:
        """Freves bin folder"""
        return self.__frevesLocation

    @frevesLocation.setter
    def frevesLocation(self, value: str):
        """Set frevesLocation"""
        self.__frevesLocation = value

    @property
    def frelinLocation(self) -> str:
        """Frelin bin folder"""
        return self.__frelinLocation

    @frelinLocation.setter
    def frelinLocation(self, value: str):
        """Set frelinLocation"""
        self.__frelinLocation = value
