# This an autogenerated file
# 
# Generated with TurbineResponseStorage
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.turbineresponsestorage import TurbineResponseStorageBlueprint
from typing import Dict
from sima.riflex.storagetype import StorageType
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class TurbineResponseStorage(MOAO):
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
    store : bool
         (default False)
    timeInterval : float
         Desired time interval for storage. A value of 0 gives storage at each time step.(default 0.0)
    fileFormat : StorageType
    """

    def __init__(self , name="", description="", _id="", store=False, timeInterval=0.0, fileFormat=StorageType.BINARY, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.store = store
        self.timeInterval = timeInterval
        self.fileFormat = fileFormat
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TurbineResponseStorageBlueprint()


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
    def store(self) -> bool:
        """"""
        return self.__store

    @store.setter
    def store(self, value: bool):
        """Set store"""
        self.__store = bool(value)

    @property
    def timeInterval(self) -> float:
        """Desired time interval for storage. A value of 0 gives storage at each time step."""
        return self.__timeInterval

    @timeInterval.setter
    def timeInterval(self, value: float):
        """Set timeInterval"""
        self.__timeInterval = float(value)

    @property
    def fileFormat(self) -> StorageType:
        """"""
        return self.__fileFormat

    @fileFormat.setter
    def fileFormat(self, value: StorageType):
        """Set fileFormat"""
        self.__fileFormat = value
