# This an autogenerated file
# 
# Generated with ComparisonOperation
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.comparisonoperation import ComparisonOperationBlueprint
from typing import Dict
from .controlsignalinputslot import ControlSignalInputSlot
from .inputslot import InputSlot
from .operationnode import OperationNode
from .outputslot import OutputSlot
from sima.sima import ScriptableValue

class ComparisonOperation(OperationNode):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
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
    first : InputSlot
    second : InputSlot
    outputSlot : OutputSlot
    factor : float
         Compares two values by using a factor times the smallest of the two numbers(default 1e-05)
    threshold : float
         Values less than this number is considered zero(default 1e-15)
    fail : bool
         If checked the operation will fail the current run when the inputs are different(default True)
    """

    def __init__(self , description="", x=0, y=0, h=0, w=0, factor=1e-05, threshold=1e-15, fail=True, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.first = None
        self.second = None
        self.outputSlot = None
        self.factor = factor
        self.threshold = threshold
        self.fail = fail
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ComparisonOperationBlueprint()


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
    def first(self) -> InputSlot:
        """"""
        return self.__first

    @first.setter
    def first(self, value: InputSlot):
        """Set first"""
        self.__first = value

    @property
    def second(self) -> InputSlot:
        """"""
        return self.__second

    @second.setter
    def second(self, value: InputSlot):
        """Set second"""
        self.__second = value

    @property
    def outputSlot(self) -> OutputSlot:
        """"""
        return self.__outputSlot

    @outputSlot.setter
    def outputSlot(self, value: OutputSlot):
        """Set outputSlot"""
        self.__outputSlot = value

    @property
    def factor(self) -> float:
        """Compares two values by using a factor times the smallest of the two numbers"""
        return self.__factor

    @factor.setter
    def factor(self, value: float):
        """Set factor"""
        self.__factor = float(value)

    @property
    def threshold(self) -> float:
        """Values less than this number is considered zero"""
        return self.__threshold

    @threshold.setter
    def threshold(self, value: float):
        """Set threshold"""
        self.__threshold = float(value)

    @property
    def fail(self) -> bool:
        """If checked the operation will fail the current run when the inputs are different"""
        return self.__fail

    @fail.setter
    def fail(self, value: bool):
        """Set fail"""
        self.__fail = bool(value)
