# This an autogenerated file
# 
# Generated with TimeSimulationResult
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.timesimulationresult import TimeSimulationResultBlueprint
from sima.sima.property import Property
from sima.sima.result import Result
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.simamessage import SimaMessage

class TimeSimulationResult(Result):
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
    properties : List[Property]
    resource : str
         (default "")
    relative : bool
         (default False)
    _type : str
         (default "")
    time : int
         (default -1)
    size : int
         (default -1)
    runNumber : int
         (default -1)
    messages : List[SimaMessage]
    """

    def __init__(self , name:str="", description:str="", _id:str="", resource:str="", relative:bool=False, _type:str="", time:int=-1, size:int=-1, runNumber:int=-1, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__properties = list()
        self.__resource = resource
        self.__relative = relative
        self.___type = _type
        self.__time = time
        self.__size = size
        self.__runNumber = runNumber
        self.__messages = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TimeSimulationResultBlueprint()


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
    def properties(self) -> List[Property]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[Property]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__properties = value

    @property
    def resource(self) -> str:
        """"""
        return self.__resource

    @resource.setter
    def resource(self, value: str):
        """Set resource"""
        self.__resource = str(value)

    @property
    def relative(self) -> bool:
        """"""
        return self.__relative

    @relative.setter
    def relative(self, value: bool):
        """Set relative"""
        self.__relative = bool(value)

    @property
    def _type(self) -> str:
        """"""
        return self.___type

    @_type.setter
    def _type(self, value: str):
        """Set _type"""
        self.___type = str(value)

    @property
    def time(self) -> int:
        """"""
        return self.__time

    @time.setter
    def time(self, value: int):
        """Set time"""
        self.__time = int(value)

    @property
    def size(self) -> int:
        """"""
        return self.__size

    @size.setter
    def size(self, value: int):
        """Set size"""
        self.__size = int(value)

    @property
    def runNumber(self) -> int:
        """"""
        return self.__runNumber

    @runNumber.setter
    def runNumber(self, value: int):
        """Set runNumber"""
        self.__runNumber = int(value)

    @property
    def messages(self) -> List[SimaMessage]:
        """"""
        return self.__messages

    @messages.setter
    def messages(self, value: List[SimaMessage]):
        """Set messages"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__messages = value
