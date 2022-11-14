# This an autogenerated file
# 
# Generated with FileInputNode
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fileinputnode import FileInputNodeBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.outputslot import OutputSlot
from sima.post.runnode import RunNode
from sima.sima.scriptablevalue import ScriptableValue

class FileInputNode(RunNode):
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
    x : int
         (default 0)
    y : int
         (default 0)
    h : int
         (default 0)
    w : int
         (default 0)
    controlSignalInputSlots : List[ControlSignalInputSlot]
    filePath : str
         Path to the input file.(default None)
    outputSlot : OutputSlot
    readRawText : bool
         read the file in as raw text data(default False)
    splitLines : bool
         split separate lines into array(default False)
    """

    def __init__(self , description="", _id=None, name=None, x=0, y=0, h=0, w=0, filePath=None, readRawText=False, splitLines=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.filePath = filePath
        self.outputSlot = None
        self.readRawText = readRawText
        self.splitLines = splitLines
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FileInputNodeBlueprint()


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
    def x(self) -> int:
        """"""
        return self.__x

    @x.setter
    def x(self, value: int):
        """Set x"""
        self.__x = int(value)

    @property
    def y(self) -> int:
        """"""
        return self.__y

    @y.setter
    def y(self, value: int):
        """Set y"""
        self.__y = int(value)

    @property
    def h(self) -> int:
        """"""
        return self.__h

    @h.setter
    def h(self, value: int):
        """Set h"""
        self.__h = int(value)

    @property
    def w(self) -> int:
        """"""
        return self.__w

    @w.setter
    def w(self, value: int):
        """Set w"""
        self.__w = int(value)

    @property
    def controlSignalInputSlots(self) -> List[ControlSignalInputSlot]:
        """"""
        return self.__controlSignalInputSlots

    @controlSignalInputSlots.setter
    def controlSignalInputSlots(self, value: List[ControlSignalInputSlot]):
        """Set controlSignalInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__controlSignalInputSlots = value

    @property
    def filePath(self) -> str:
        """Path to the input file."""
        return self.__filePath

    @filePath.setter
    def filePath(self, value: str):
        """Set filePath"""
        self.__filePath = str(value)

    @property
    def outputSlot(self) -> OutputSlot:
        """"""
        return self.__outputSlot

    @outputSlot.setter
    def outputSlot(self, value: OutputSlot):
        """Set outputSlot"""
        self.__outputSlot = value

    @property
    def readRawText(self) -> bool:
        """read the file in as raw text data"""
        return self.__readRawText

    @readRawText.setter
    def readRawText(self, value: bool):
        """Set readRawText"""
        self.__readRawText = bool(value)

    @property
    def splitLines(self) -> bool:
        """split separate lines into array"""
        return self.__splitLines

    @splitLines.setter
    def splitLines(self, value: bool):
        """Set splitLines"""
        self.__splitLines = bool(value)
