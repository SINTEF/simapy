# This an autogenerated file
# 
# Generated with LisFile
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.lisfile import LisFileBlueprint
from typing import Dict
from sima.sima.property import Property
from sima.sima.result import Result
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.simamessage import SimaMessage

class LisFile(Result):
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
    runFailed : bool
         (default True)
    version : str
         (default "")
    """

    def __init__(self , name="", description="", _id="", resource="", relative=False, _type="", time=-1, size=-1, runNumber=-1, runFailed=True, version="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.properties = list()
        self.resource = resource
        self.relative = relative
        self._type = _type
        self.time = time
        self.size = size
        self.runNumber = runNumber
        self.messages = list()
        self.runFailed = runFailed
        self.version = version
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return LisFileBlueprint()


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

    @property
    def runFailed(self) -> bool:
        """"""
        return self.__runFailed

    @runFailed.setter
    def runFailed(self, value: bool):
        """Set runFailed"""
        self.__runFailed = bool(value)

    @property
    def version(self) -> str:
        """"""
        return self.__version

    @version.setter
    def version(self, value: str):
        """Set version"""
        self.__version = str(value)
