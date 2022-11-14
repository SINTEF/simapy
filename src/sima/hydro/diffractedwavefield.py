# This an autogenerated file
# 
# Generated with DiffractedWaveField
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.diffractedwavefield import DiffractedWaveFieldBlueprint
from typing import Dict
from sima.hydro.diffractedwave import DiffractedWave
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class DiffractedWaveField(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    waves : List[DiffractedWave]
    """

    def __init__(self , description="", _id=None, name=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.waves = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DiffractedWaveFieldBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def waves(self) -> List[DiffractedWave]:
        """"""
        return self.__waves

    @waves.setter
    def waves(self, value: List[DiffractedWave]):
        """Set waves"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__waves = value
