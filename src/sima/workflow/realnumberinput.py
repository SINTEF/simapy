# This an autogenerated file
# 
# Generated with RealNumberInput
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.realnumberinput import RealNumberInputBlueprint
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.outputslot import OutputSlot
from sima.post.signalproperties import SignalProperties
from sima.sima.scriptablevalue import ScriptableValue
from sima.workflow.valueinputnode import ValueInputNode

class RealNumberInput(ValueInputNode):
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
    value : float
         (default 0.0)
    array : bool
         Create an array output(default False)
    values : Sequence[float]
    """

    def __init__(self , name:str="", description:str="", _id:str="", x:int=0, y:int=0, h:int=0, w:int=0, root:str="", resultId:str="", specifyAdditionalProperties:bool=False, value:float=0.0, array:bool=False, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__x = x
        self.__y = y
        self.__h = h
        self.__w = w
        self.__controlSignalInputSlots = list()
        self.__root = root
        self.__resultId = resultId
        self.__outputSlot = OutputSlot()
        self.__properties = list()
        self.__specifyAdditionalProperties = specifyAdditionalProperties
        self.__value = value
        self.__array = array
        self.__values = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RealNumberInputBlueprint()


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
    def value(self) -> float:
        """"""
        return self.__value

    @value.setter
    def value(self, value: float):
        """Set value"""
        self.__value = float(value)

    @property
    def array(self) -> bool:
        """Create an array output"""
        return self.__array

    @array.setter
    def array(self, value: bool):
        """Set array"""
        self.__array = bool(value)

    @property
    def values(self) -> Sequence[float]:
        """"""
        return self.__values

    @values.setter
    def values(self, value: Sequence[float]):
        """Set values"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__values = value
