# This an autogenerated file
# 
# Generated with PostProcessorSpecification
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.postprocessorspecification import PostProcessorSpecificationBlueprint
from typing import Dict
from sima.post.operationnode import OperationNode
from sima.post.slotconnection import SlotConnection
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class PostProcessorSpecification(NamedObject):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    nodes : List[OperationNode]
    connections : List[SlotConnection]
    """

    def __init__(self , _id="", name="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.nodes = list()
        self.connections = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PostProcessorSpecificationBlueprint()


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
    def nodes(self) -> List[OperationNode]:
        """"""
        return self.__nodes

    @nodes.setter
    def nodes(self, value: List[OperationNode]):
        """Set nodes"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__nodes = value

    @property
    def connections(self) -> List[SlotConnection]:
        """"""
        return self.__connections

    @connections.setter
    def connections(self, value: List[SlotConnection]):
        """Set connections"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__connections = value
