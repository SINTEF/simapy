# This an autogenerated file
# 
# Generated with PostprocessorOutputSlot
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.postprocessoroutputslot import PostprocessorOutputSlotBlueprint
from typing import Dict
from sima.post.outputslot import OutputSlot
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.post.postworkflowoutput import PostWorkflowOutput

class PostprocessorOutputSlot(OutputSlot):
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
    postprocessorOutput : PostWorkflowOutput
    """

    def __init__(self , description="", _id=None, name=None, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.postprocessorOutput = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PostprocessorOutputSlotBlueprint()


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
    def postprocessorOutput(self) -> PostWorkflowOutput:
        """"""
        return self.__postprocessorOutput

    @postprocessorOutput.setter
    def postprocessorOutput(self, value: PostWorkflowOutput):
        """Set postprocessorOutput"""
        self.__postprocessorOutput = value
