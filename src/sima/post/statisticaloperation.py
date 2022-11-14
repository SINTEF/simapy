# This an autogenerated file
# 
# Generated with StatisticalOperation
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.statisticaloperation import StatisticalOperationBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.inputslot import InputSlot
from sima.post.operationnode import OperationNode
from sima.post.outputslot import OutputSlot
from sima.post.statisticsoperation import StatisticsOperation
from sima.sima.scriptablevalue import ScriptableValue

class StatisticalOperation(OperationNode):
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
    renameOutput : bool
         (default True)
    operation : StatisticsOperation
    combine : bool
         This will run the operation a second time on the transformed input to produce a combined output such as maxima of maxima etc.(default False)
    inputSlot : InputSlot
    outputSlot : OutputSlot
    outputIndex : bool
         Output the index of the event ( valid for maxima and minima)(default False)
    combinedName : str
         Name of output when using combined operation(default None)
    """

    def __init__(self , description="", _id=None, name=None, x=0, y=0, h=0, w=0, renameOutput=True, operation=StatisticsOperation.MAX, combine=False, outputIndex=False, combinedName=None, **kwargs):
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
        self.renameOutput = renameOutput
        self.operation = operation
        self.combine = combine
        self.inputSlot = None
        self.outputSlot = None
        self.outputIndex = outputIndex
        self.combinedName = combinedName
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StatisticalOperationBlueprint()


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
    def renameOutput(self) -> bool:
        """"""
        return self.__renameOutput

    @renameOutput.setter
    def renameOutput(self, value: bool):
        """Set renameOutput"""
        self.__renameOutput = bool(value)

    @property
    def operation(self) -> StatisticsOperation:
        """"""
        return self.__operation

    @operation.setter
    def operation(self, value: StatisticsOperation):
        """Set operation"""
        self.__operation = value

    @property
    def combine(self) -> bool:
        """This will run the operation a second time on the transformed input to produce a combined output such as maxima of maxima etc."""
        return self.__combine

    @combine.setter
    def combine(self, value: bool):
        """Set combine"""
        self.__combine = bool(value)

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

    @property
    def outputIndex(self) -> bool:
        """Output the index of the event ( valid for maxima and minima)"""
        return self.__outputIndex

    @outputIndex.setter
    def outputIndex(self, value: bool):
        """Set outputIndex"""
        self.__outputIndex = bool(value)

    @property
    def combinedName(self) -> str:
        """Name of output when using combined operation"""
        return self.__combinedName

    @combinedName.setter
    def combinedName(self, value: str):
        """Set combinedName"""
        self.__combinedName = str(value)
