# This an autogenerated file
# 
# Generated with ModelReferenceInput
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.modelreferenceinput import ModelReferenceInputBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.outputslot import OutputSlot
from sima.post.signalproperties import SignalProperties
from sima.sima.scriptablevalue import ScriptableValue
from sima.workflow.modelreference import ModelReference
from sima.workflow.valueinputnode import ValueInputNode
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima.moao import MOAO

class ModelReferenceInput(ValueInputNode,ModelReference):
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
    root : str
         (default None)
    resultId : str
         (default None)
    outputSlot : OutputSlot
    properties : List[SignalProperties]
    model : MOAO
    reference : str
         (default 'workflow')
    specifyAdditionalProperties : bool
         Specify additional properties in the signal(default False)
    _type : str
         (default 'workflow')
    useReference : bool
         Uses a soft link to the referenced model, meaning the relation is not cleared if the references object is deleted or does not exist(default False)
    array : bool
         Create an array output(default False)
    modelReferences : List[ModelReference]
    """

    def __init__(self , description="", _id=None, name=None, x=0, y=0, h=0, w=0, root=None, resultId=None, reference='workflow', specifyAdditionalProperties=False, _type='workflow', useReference=False, array=False, **kwargs):
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
        self.root = root
        self.resultId = resultId
        self.outputSlot = None
        self.properties = list()
        self.model = None
        self.reference = reference
        self.specifyAdditionalProperties = specifyAdditionalProperties
        self._type = _type
        self.useReference = useReference
        self.array = array
        self.modelReferences = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ModelReferenceInputBlueprint()


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
    def model(self) -> MOAO:
        """"""
        return self.__model

    @model.setter
    def model(self, value: MOAO):
        """Set model"""
        self.__model = value

    @property
    def reference(self) -> str:
        """"""
        return self.__reference

    @reference.setter
    def reference(self, value: str):
        """Set reference"""
        self.__reference = str(value)

    @property
    def specifyAdditionalProperties(self) -> bool:
        """Specify additional properties in the signal"""
        return self.__specifyAdditionalProperties

    @specifyAdditionalProperties.setter
    def specifyAdditionalProperties(self, value: bool):
        """Set specifyAdditionalProperties"""
        self.__specifyAdditionalProperties = bool(value)

    @property
    def _type(self) -> str:
        """"""
        return self.___type

    @_type.setter
    def _type(self, value: str):
        """Set _type"""
        self.___type = str(value)

    @property
    def useReference(self) -> bool:
        """Uses a soft link to the referenced model, meaning the relation is not cleared if the references object is deleted or does not exist"""
        return self.__useReference

    @useReference.setter
    def useReference(self, value: bool):
        """Set useReference"""
        self.__useReference = bool(value)

    @property
    def array(self) -> bool:
        """Create an array output"""
        return self.__array

    @array.setter
    def array(self, value: bool):
        """Set array"""
        self.__array = bool(value)

    @property
    def modelReferences(self) -> List[ModelReference]:
        """"""
        return self.__modelReferences

    @modelReferences.setter
    def modelReferences(self, value: List[ModelReference]):
        """Set modelReferences"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__modelReferences = value
