# This an autogenerated file
# 
# Generated with Workflow
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.workflow import WorkflowBlueprint
from sima.post.runnode import RunNode
from sima.post.slotconnection import SlotConnection
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class Workflow(NamedObject):
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
    nodes : List[RunNode]
    connections : List[SlotConnection]
    computeServiceID : str
         (default "")
    """

    def __init__(self , name:str="", description:str="", _id:str="", computeServiceID:str="", **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__nodes = list()
        self.__connections = list()
        self.__computeServiceID = computeServiceID
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WorkflowBlueprint()


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
    def nodes(self) -> List[RunNode]:
        """"""
        return self.__nodes

    @nodes.setter
    def nodes(self, value: List[RunNode]):
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

    @property
    def computeServiceID(self) -> str:
        """"""
        return self.__computeServiceID

    @computeServiceID.setter
    def computeServiceID(self, value: str):
        """Set computeServiceID"""
        self.__computeServiceID = str(value)
