# This an autogenerated file
# 
# Generated with ModelInputSlot
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.modelinputslot import ModelInputSlotBlueprint
from typing import Dict
from sima.post.inputslot import InputSlot
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.condition.modelreferencevariable import ModelReferenceVariable

class ModelInputSlot(InputSlot):
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
    reference : ModelReferenceVariable
         Model reference to be replaced
    replaceChildren : bool
         If checked the children of the reference will replaced(default False)
    """

    def __init__(self , name="", description="", _id="", replaceChildren=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.reference = None
        self.replaceChildren = replaceChildren
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ModelInputSlotBlueprint()


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
    def reference(self) -> ModelReferenceVariable:
        """Model reference to be replaced"""
        return self.__reference

    @reference.setter
    def reference(self, value: ModelReferenceVariable):
        """Set reference"""
        self.__reference = value

    @property
    def replaceChildren(self) -> bool:
        """If checked the children of the reference will replaced"""
        return self.__replaceChildren

    @replaceChildren.setter
    def replaceChildren(self, value: bool):
        """Set replaceChildren"""
        self.__replaceChildren = bool(value)
