# This an autogenerated file
# 
# Generated with ForceResponseStorage
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.forceresponsestorage import ForceResponseStorageBlueprint
from typing import Dict
from .additionalfileformatcode import AdditionalFileFormatCode
from .elementangle import ElementAngle
from .elementreference import ElementReference
from .elementtransformation import ElementTransformation
from .fileformatcode import FileFormatCode
from .relativeelementangle import RelativeElementAngle
from sima.sima import MOAO
from sima.sima import ScriptableValue

class ForceResponseStorage(MOAO):
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
    matrixFormat : AdditionalFileFormatCode
         Format code for additional output of element transformation matrices
    readTransformationMatrices : bool
         Make transformation matrices available in the post processor(default False)
    relativeElementAngles : List[RelativeElementAngle]
    elementAngles : List[ElementAngle]
    storeBottomContactForces : bool
         Store results for seafloor contact elements and / or soil layer profile (SLP) contact elements(default False)
    transformations : List[ElementTransformation]
    """

    def __init__(self , description="", storageStep=1, format=FileFormatCode.BINARY_OUTPUT_ONLY, matrixFormat=AdditionalFileFormatCode.BINARY_OUTPUT, readTransformationMatrices=False, storeBottomContactForces=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.storageStep = storageStep
        self.format = format
        self.elements = list()
        self.matrixFormat = matrixFormat
        self.readTransformationMatrices = readTransformationMatrices
        self.relativeElementAngles = list()
        self.elementAngles = list()
        self.storeBottomContactForces = storeBottomContactForces
        self.transformations = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ForceResponseStorageBlueprint()


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

    @property
    def matrixFormat(self) -> AdditionalFileFormatCode:
        """Format code for additional output of element transformation matrices"""
        return self.__matrixFormat

    @matrixFormat.setter
    def matrixFormat(self, value: AdditionalFileFormatCode):
        """Set matrixFormat"""
        self.__matrixFormat = value

    @property
    def readTransformationMatrices(self) -> bool:
        """Make transformation matrices available in the post processor"""
        return self.__readTransformationMatrices

    @readTransformationMatrices.setter
    def readTransformationMatrices(self, value: bool):
        """Set readTransformationMatrices"""
        self.__readTransformationMatrices = bool(value)

    @property
    def relativeElementAngles(self) -> List[RelativeElementAngle]:
        """"""
        return self.__relativeElementAngles

    @relativeElementAngles.setter
    def relativeElementAngles(self, value: List[RelativeElementAngle]):
        """Set relativeElementAngles"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__relativeElementAngles = value

    @property
    def elementAngles(self) -> List[ElementAngle]:
        """"""
        return self.__elementAngles

    @elementAngles.setter
    def elementAngles(self, value: List[ElementAngle]):
        """Set elementAngles"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__elementAngles = value

    @property
    def storeBottomContactForces(self) -> bool:
        """Store results for seafloor contact elements and / or soil layer profile (SLP) contact elements"""
        return self.__storeBottomContactForces

    @storeBottomContactForces.setter
    def storeBottomContactForces(self, value: bool):
        """Set storeBottomContactForces"""
        self.__storeBottomContactForces = bool(value)

    @property
    def transformations(self) -> List[ElementTransformation]:
        """"""
        return self.__transformations

    @transformations.setter
    def transformations(self, value: List[ElementTransformation]):
        """Set transformations"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__transformations = value