# This an autogenerated file
# 
# Generated with TextInput
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.textinput import TextInputBlueprint
from numpy import ndarray,asarray
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.outputslot import OutputSlot
from sima.post.signalproperties import SignalProperties
from sima.sima.scriptablevalue import ScriptableValue
from sima.workflow.valueinputnode import ValueInputNode

class TextInput(ValueInputNode):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    x : int
         (default 0)
    y : int
         (default 0)
    h : int
         (default 0)
    w : int
         (default 0)
    controlSignalInputSlots : List[ControlSignalInputSlot]
    root : str
         (default "")
    resultId : str
         (default "")
    outputSlot : OutputSlot
    properties : List[SignalProperties]
    specifyAdditionalProperties : bool
         Specify additional properties in the signal(default False)
    value : str
         (default "")
    array : bool
         Create a text array output(default False)
    values : ndarray
    """

    def __init__(self , _id="", name="", x=0, y=0, h=0, w=0, root="", resultId="", specifyAdditionalProperties=False, value="", array=False, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.root = root
        self.resultId = resultId
        self.outputSlot = None
        self.properties = list()
        self.specifyAdditionalProperties = specifyAdditionalProperties
        self.value = value
        self.array = array
        self.values = ndarray(1)
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TextInputBlueprint()


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
    def root(self) -> str:
        """"""
        return self.__root

    @root.setter
    def root(self, value: str):
        """Set root"""
        self.__root = str(value)

    @property
    def resultId(self) -> str:
        """"""
        return self.__resultId

    @resultId.setter
    def resultId(self, value: str):
        """Set resultId"""
        self.__resultId = str(value)

    @property
    def outputSlot(self) -> OutputSlot:
        """"""
        return self.__outputSlot

    @outputSlot.setter
    def outputSlot(self, value: OutputSlot):
        """Set outputSlot"""
        self.__outputSlot = value

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
    def specifyAdditionalProperties(self) -> bool:
        """Specify additional properties in the signal"""
        return self.__specifyAdditionalProperties

    @specifyAdditionalProperties.setter
    def specifyAdditionalProperties(self, value: bool):
        """Set specifyAdditionalProperties"""
        self.__specifyAdditionalProperties = bool(value)

    @property
    def value(self) -> str:
        """"""
        return self.__value

    @value.setter
    def value(self, value: str):
        """Set value"""
        self.__value = str(value)

    @property
    def array(self) -> bool:
        """Create a text array output"""
        return self.__array

    @array.setter
    def array(self, value: bool):
        """Set array"""
        self.__array = bool(value)

    @property
    def values(self) -> ndarray:
        """"""
        return self.__values

    @values.setter
    def values(self, value: ndarray):
        """Set values"""
        self.__values = asarray(value)
