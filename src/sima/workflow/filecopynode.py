# This an autogenerated file
# 
# Generated with FileCopyNode
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.filecopynode import FileCopyNodeBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.inputslot import InputSlot
from sima.post.outputslot import OutputSlot
from sima.post.runnode import RunNode
from sima.sima.scriptablevalue import ScriptableValue

class FileCopyNode(RunNode):
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
    ignoreEmptyInput : bool
         Do not run if input is empty(default False)
    folder : bool
         If this is set, all files that er input to the operation will be copied to the destination, otherwise a single file is expected(default False)
    path : str
         Path to the output file.(default None)
    retainStructure : bool
         Retain structure of input(default False)
    cleanUpFolder : bool
         Delete all contained files and folders in the given folder before copying(default False)
    inputSlot : InputSlot
    outputSlot : OutputSlot
    """

    def __init__(self , description="", _id=None, name=None, x=0, y=0, h=0, w=0, ignoreEmptyInput=False, folder=False, path=None, retainStructure=False, cleanUpFolder=False, **kwargs):
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
        self.ignoreEmptyInput = ignoreEmptyInput
        self.folder = folder
        self.path = path
        self.retainStructure = retainStructure
        self.cleanUpFolder = cleanUpFolder
        self.inputSlot = None
        self.outputSlot = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FileCopyNodeBlueprint()


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
    def ignoreEmptyInput(self) -> bool:
        """Do not run if input is empty"""
        return self.__ignoreEmptyInput

    @ignoreEmptyInput.setter
    def ignoreEmptyInput(self, value: bool):
        """Set ignoreEmptyInput"""
        self.__ignoreEmptyInput = bool(value)

    @property
    def folder(self) -> bool:
        """If this is set, all files that er input to the operation will be copied to the destination, otherwise a single file is expected"""
        return self.__folder

    @folder.setter
    def folder(self, value: bool):
        """Set folder"""
        self.__folder = bool(value)

    @property
    def path(self) -> str:
        """Path to the output file."""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = str(value)

    @property
    def retainStructure(self) -> bool:
        """Retain structure of input"""
        return self.__retainStructure

    @retainStructure.setter
    def retainStructure(self, value: bool):
        """Set retainStructure"""
        self.__retainStructure = bool(value)

    @property
    def cleanUpFolder(self) -> bool:
        """Delete all contained files and folders in the given folder before copying"""
        return self.__cleanUpFolder

    @cleanUpFolder.setter
    def cleanUpFolder(self, value: bool):
        """Set cleanUpFolder"""
        self.__cleanUpFolder = bool(value)

    @property
    def inputSlot(self) -> InputSlot:
        """"""
        return self.__inputSlot

    @inputSlot.setter
    def inputSlot(self, value: InputSlot):
        """Set inputSlot"""
        self.__inputSlot = value

    @property
    def outputSlot(self) -> OutputSlot:
        """"""
        return self.__outputSlot

    @outputSlot.setter
    def outputSlot(self, value: OutputSlot):
        """Set outputSlot"""
        self.__outputSlot = value
