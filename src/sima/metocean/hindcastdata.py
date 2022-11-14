# This an autogenerated file
# 
# Generated with HindcastData
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hindcastdata import HindcastDataBlueprint
from typing import Dict
from sima.metocean.hindcastlevelcontainer import HindcastLevelContainer
from sima.metocean.hindcastwavecontainer import HindcastWaveContainer
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class HindcastData(NamedObject):
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
    dataFile : str
         (default None)
    path : str
         (default None)
    firstDate : str
         (default None)
    lastDate : str
         (default None)
    waveData : HindcastWaveContainer
    windData : HindcastLevelContainer
    currentData : HindcastLevelContainer
    """

    def __init__(self , description="", _id=None, name=None, dataFile=None, path=None, firstDate=None, lastDate=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.dataFile = dataFile
        self.path = path
        self.firstDate = firstDate
        self.lastDate = lastDate
        self.waveData = None
        self.windData = None
        self.currentData = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HindcastDataBlueprint()


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
    def dataFile(self) -> str:
        """"""
        return self.__dataFile

    @dataFile.setter
    def dataFile(self, value: str):
        """Set dataFile"""
        self.__dataFile = str(value)

    @property
    def path(self) -> str:
        """"""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = str(value)

    @property
    def firstDate(self) -> str:
        """"""
        return self.__firstDate

    @firstDate.setter
    def firstDate(self, value: str):
        """Set firstDate"""
        self.__firstDate = str(value)

    @property
    def lastDate(self) -> str:
        """"""
        return self.__lastDate

    @lastDate.setter
    def lastDate(self, value: str):
        """Set lastDate"""
        self.__lastDate = str(value)

    @property
    def waveData(self) -> HindcastWaveContainer:
        """"""
        return self.__waveData

    @waveData.setter
    def waveData(self, value: HindcastWaveContainer):
        """Set waveData"""
        self.__waveData = value

    @property
    def windData(self) -> HindcastLevelContainer:
        """"""
        return self.__windData

    @windData.setter
    def windData(self, value: HindcastLevelContainer):
        """Set windData"""
        self.__windData = value

    @property
    def currentData(self) -> HindcastLevelContainer:
        """"""
        return self.__currentData

    @currentData.setter
    def currentData(self, value: HindcastLevelContainer):
        """Set currentData"""
        self.__currentData = value
