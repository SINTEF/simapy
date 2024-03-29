# This an autogenerated file
# 
# Generated with DisplacementResponseStorage
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.displacementresponsestorage import DisplacementResponseStorageBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .fileformatcode import FileFormatCode
from .nodereference import NodeReference

class DisplacementResponseStorage(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    storageStep : int
         Code for storage of nodal displacements. Storage for every <storage step> given.(default 1)
    format : FileFormatCode
         Format code for additional output of nodal displacement time series
    nodes : List[NodeReference]
         Specification of nodes for displacement storage
    """

    def __init__(self , description="", storageStep=1, format=FileFormatCode.BINARY_OUTPUT_ONLY, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.storageStep = storageStep
        self.format = format
        self.nodes = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DisplacementResponseStorageBlueprint()


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
    def storageStep(self) -> int:
        """Code for storage of nodal displacements. Storage for every <storage step> given."""
        return self.__storageStep

    @storageStep.setter
    def storageStep(self, value: int):
        """Set storageStep"""
        self.__storageStep = int(value)

    @property
    def format(self) -> FileFormatCode:
        """Format code for additional output of nodal displacement time series"""
        return self.__format

    @format.setter
    def format(self, value: FileFormatCode):
        """Set format"""
        self.__format = value

    @property
    def nodes(self) -> List[NodeReference]:
        """Specification of nodes for displacement storage"""
        return self.__nodes

    @nodes.setter
    def nodes(self, value: List[NodeReference]):
        """Set nodes"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__nodes = value
