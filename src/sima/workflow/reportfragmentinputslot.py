# This an autogenerated file
# 
# Generated with ReportFragmentInputSlot
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.reportfragmentinputslot import ReportFragmentInputSlotBlueprint
from typing import Dict
from sima.post.inputslot import InputSlot
from sima.sima.scriptablevalue import ScriptableValue
from sima.workflow.reportfragmentitem import ReportFragmentItem

class ReportFragmentInputSlot(ReportFragmentItem,InputSlot):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    """

    def __init__(self , _id="", name="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ReportFragmentInputSlotBlueprint()


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
