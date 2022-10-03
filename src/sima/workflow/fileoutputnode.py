# This an autogenerated file
# 
# Generated with FileOutputNode
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fileoutputnode import FileOutputNodeBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.decimalseparator import DecimalSeparator
from sima.post.fileformat import FileFormat
from sima.post.inputslot import InputSlot
from sima.post.outputnode import OutputNode
from sima.post.outputslot import OutputSlot
from sima.post.signalproperties import SignalProperties
from sima.post.signalpropertiescontainer import SignalPropertiesContainer
from sima.sima.scriptablevalue import ScriptableValue

class FileOutputNode(OutputNode,SignalPropertiesContainer):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    properties : List[SignalProperties]
    x : int
         (default 0)
    y : int
         (default 0)
    h : int
         (default 0)
    w : int
         (default 0)
    controlSignalInputSlots : List[ControlSignalInputSlot]
    inputSlot : InputSlot
    filePath : str
         Path to the output file.(default "")
    fileFormat : FileFormat
         Format of the exported file.
    shellCommand : str
         Shell command to execute after the export.(default "")
    addMetaTags : bool
         Include metadata tags in output(default False)
    decimalSeparator : DecimalSeparator
         Set according to the language of Excel. Comma as\ndecimal-separator will make semicolon the value-separator.
    skipHeader : bool
         Do not write a header on the file(default False)
    specifyAdditionalProperties : bool
         Specify additional properties in the file root(default False)
    writeRawText : bool
         Writes a single input string into the given file(default False)
    outputSlot : OutputSlot
    """

    def __init__(self , _id="", name="", x=0, y=0, h=0, w=0, filePath="", fileFormat=FileFormat.CSV, shellCommand="", addMetaTags=False, decimalSeparator=DecimalSeparator.PERIOD, skipHeader=False, specifyAdditionalProperties=False, writeRawText=False, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.properties = list()
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.inputSlot = None
        self.filePath = filePath
        self.fileFormat = fileFormat
        self.shellCommand = shellCommand
        self.addMetaTags = addMetaTags
        self.decimalSeparator = decimalSeparator
        self.skipHeader = skipHeader
        self.specifyAdditionalProperties = specifyAdditionalProperties
        self.writeRawText = writeRawText
        self.outputSlot = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FileOutputNodeBlueprint()


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
    def properties(self) -> List[SignalProperties]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[SignalProperties]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__properties = value

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
    def inputSlot(self) -> InputSlot:
        """"""
        return self.__inputSlot

    @inputSlot.setter
    def inputSlot(self, value: InputSlot):
        """Set inputSlot"""
        self.__inputSlot = value

    @property
    def filePath(self) -> str:
        """Path to the output file."""
        return self.__filePath

    @filePath.setter
    def filePath(self, value: str):
        """Set filePath"""
        self.__filePath = str(value)

    @property
    def fileFormat(self) -> FileFormat:
        """Format of the exported file."""
        return self.__fileFormat

    @fileFormat.setter
    def fileFormat(self, value: FileFormat):
        """Set fileFormat"""
        self.__fileFormat = value

    @property
    def shellCommand(self) -> str:
        """Shell command to execute after the export."""
        return self.__shellCommand

    @shellCommand.setter
    def shellCommand(self, value: str):
        """Set shellCommand"""
        self.__shellCommand = str(value)

    @property
    def addMetaTags(self) -> bool:
        """Include metadata tags in output"""
        return self.__addMetaTags

    @addMetaTags.setter
    def addMetaTags(self, value: bool):
        """Set addMetaTags"""
        self.__addMetaTags = bool(value)

    @property
    def decimalSeparator(self) -> DecimalSeparator:
        """Set according to the language of Excel. Comma as
decimal-separator will make semicolon the value-separator."""
        return self.__decimalSeparator

    @decimalSeparator.setter
    def decimalSeparator(self, value: DecimalSeparator):
        """Set decimalSeparator"""
        self.__decimalSeparator = value

    @property
    def skipHeader(self) -> bool:
        """Do not write a header on the file"""
        return self.__skipHeader

    @skipHeader.setter
    def skipHeader(self, value: bool):
        """Set skipHeader"""
        self.__skipHeader = bool(value)

    @property
    def specifyAdditionalProperties(self) -> bool:
        """Specify additional properties in the file root"""
        return self.__specifyAdditionalProperties

    @specifyAdditionalProperties.setter
    def specifyAdditionalProperties(self, value: bool):
        """Set specifyAdditionalProperties"""
        self.__specifyAdditionalProperties = bool(value)

    @property
    def writeRawText(self) -> bool:
        """Writes a single input string into the given file"""
        return self.__writeRawText

    @writeRawText.setter
    def writeRawText(self, value: bool):
        """Set writeRawText"""
        self.__writeRawText = bool(value)

    @property
    def outputSlot(self) -> OutputSlot:
        """"""
        return self.__outputSlot

    @outputSlot.setter
    def outputSlot(self, value: OutputSlot):
        """Set outputSlot"""
        self.__outputSlot = value
