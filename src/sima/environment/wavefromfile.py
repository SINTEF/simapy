# This an autogenerated file
# 
# Generated with WaveFromFile
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wavefromfile import WaveFromFileBlueprint
from typing import Dict
from sima.environment.wave import Wave
from sima.sima.scriptablevalue import ScriptableValue

class WaveFromFile(Wave):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    fileName : str
         Name of external file with specified wave data(default None)
    """

    def __init__(self , description="", _id=None, fileName=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.fileName = fileName
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WaveFromFileBlueprint()


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
    def fileName(self) -> str:
        """Name of external file with specified wave data"""
        return self.__fileName

    @fileName.setter
    def fileName(self, value: str):
        """Set fileName"""
        self.__fileName = str(value)
