# This an autogenerated file
# 
# Generated with CurvatureResponseStorage
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.curvatureresponsestorage import CurvatureResponseStorageBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .elementreference import ElementReference
from .fileformatcode import FileFormatCode

class CurvatureResponseStorage(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    storageStep : int
         Code for storage of internal forces. Storage for every <storage step> given.(default 1)
    format : FileFormatCode
         Format code for additional output of time series
    elements : List[ElementReference]
         Specification of nodes for displacement storage
    """

    def __init__(self , description="", storageStep=1, format=FileFormatCode.BINARY_OUTPUT_ONLY, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.storageStep = storageStep
        self.format = format
        self.elements = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CurvatureResponseStorageBlueprint()


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
        """Code for storage of internal forces. Storage for every <storage step> given."""
        return self.__storageStep

    @storageStep.setter
    def storageStep(self, value: int):
        """Set storageStep"""
        self.__storageStep = int(value)

    @property
    def format(self) -> FileFormatCode:
        """Format code for additional output of time series"""
        return self.__format

    @format.setter
    def format(self, value: FileFormatCode):
        """Set format"""
        self.__format = value

    @property
    def elements(self) -> List[ElementReference]:
        """Specification of nodes for displacement storage"""
        return self.__elements

    @elements.setter
    def elements(self, value: List[ElementReference]):
        """Set elements"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__elements = value
