# This an autogenerated file
# 
# Generated with CustomPlot
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.customplot import CustomPlotBlueprint
from typing import Dict
from sima.custom.customcomponent import CustomComponent
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.post.outputnode import OutputNode

class CustomPlot(CustomComponent):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    output : OutputNode
    path : str
         (default "")
    showTree : bool
         (default False)
    """

    def __init__(self , _id="", path="", showTree=False, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.output = None
        self.path = path
        self.showTree = showTree
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomPlotBlueprint()


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
    def output(self) -> OutputNode:
        """"""
        return self.__output

    @output.setter
    def output(self, value: OutputNode):
        """Set output"""
        self.__output = value

    @property
    def path(self) -> str:
        """"""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = str(value)

    @property
    def showTree(self) -> bool:
        """"""
        return self.__showTree

    @showTree.setter
    def showTree(self, value: bool):
        """Set showTree"""
        self.__showTree = bool(value)
