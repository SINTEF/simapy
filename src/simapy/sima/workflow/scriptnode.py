# This an autogenerated file
# 
# Generated with ScriptNode
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.scriptnode import ScriptNodeBlueprint
from typing import Dict
from ..post import ControlSignalInputSlot
from ..post import OutputSlot
from ..post import RunNode
from ..post import SignalProperties
from ..post import SignalPropertiesContainer
from ..sima import ScriptableValue
from .scriptinputslot import ScriptInputSlot

class ScriptNode(RunNode,SignalPropertiesContainer):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
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
    inline : bool
         Use inline script or external(default True)
    path : str
         Path to the output file.(default None)
    script : str
         (default None)
    variableInputSlots : List[ScriptInputSlot]
    outputSlot : OutputSlot
    """

    def __init__(self , description="", x=0, y=0, h=0, w=0, inline=True, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.properties = list()
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.inline = inline
        self.path = None
        self.script = None
        self.variableInputSlots = list()
        self.outputSlot = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ScriptNodeBlueprint()


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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def properties(self) -> List[SignalProperties]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[SignalProperties]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__controlSignalInputSlots = value

    @property
    def inline(self) -> bool:
        """Use inline script or external"""
        return self.__inline

    @inline.setter
    def inline(self, value: bool):
        """Set inline"""
        self.__inline = bool(value)

    @property
    def path(self) -> str:
        """Path to the output file."""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = value

    @property
    def script(self) -> str:
        """"""
        return self.__script

    @script.setter
    def script(self, value: str):
        """Set script"""
        self.__script = value

    @property
    def variableInputSlots(self) -> List[ScriptInputSlot]:
        """"""
        return self.__variableInputSlots

    @variableInputSlots.setter
    def variableInputSlots(self, value: List[ScriptInputSlot]):
        """Set variableInputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__variableInputSlots = value

    @property
    def outputSlot(self) -> OutputSlot:
        """"""
        return self.__outputSlot

    @outputSlot.setter
    def outputSlot(self, value: OutputSlot):
        """Set outputSlot"""
        self.__outputSlot = value
