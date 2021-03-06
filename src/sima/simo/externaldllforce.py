# This an autogenerated file
# 
# Generated with ExternalDLLForce
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.externaldllforce import ExternalDLLForceBlueprint
from typing import Dict
from sima.sima.librarypaths import LibraryPaths
from sima.sima.namedobject import NamedObject
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.referenceframetype import ReferenceFrameType
from sima.simo.stringdoubleitem import StringDoubleItem
from sima.simo.stringintitem import StringIntItem
from sima.simo.stringitem import StringItem

class ExternalDLLForce(NamedObject):
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
    attachmentPoint : Point3
         Attack point of force.
    referenceFrame : ReferenceFrameType
         Which coordinate system is the force is given in?
    nStorageParameters : int
         Number of parameters for intermediate storage(default 0)
    intParameters : List[StringIntItem]
    doubleParameters : List[StringDoubleItem]
    stringParameters : List[StringItem]
    nCurrentPoints : int
         Number of points where current velocities shall be given.(default 1)
    dllFile : str
         (default "")
    libraryPaths : LibraryPaths
    """

    def __init__(self , name="", description="", _id="", referenceFrame=ReferenceFrameType.LOCAL, nStorageParameters=0, nCurrentPoints=1, dllFile="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.attachmentPoint = None
        self.referenceFrame = referenceFrame
        self.nStorageParameters = nStorageParameters
        self.intParameters = list()
        self.doubleParameters = list()
        self.stringParameters = list()
        self.nCurrentPoints = nCurrentPoints
        self.dllFile = dllFile
        self.libraryPaths = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExternalDLLForceBlueprint()


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
    def attachmentPoint(self) -> Point3:
        """Attack point of force."""
        return self.__attachmentPoint

    @attachmentPoint.setter
    def attachmentPoint(self, value: Point3):
        """Set attachmentPoint"""
        self.__attachmentPoint = value

    @property
    def referenceFrame(self) -> ReferenceFrameType:
        """Which coordinate system is the force is given in?"""
        return self.__referenceFrame

    @referenceFrame.setter
    def referenceFrame(self, value: ReferenceFrameType):
        """Set referenceFrame"""
        self.__referenceFrame = value

    @property
    def nStorageParameters(self) -> int:
        """Number of parameters for intermediate storage"""
        return self.__nStorageParameters

    @nStorageParameters.setter
    def nStorageParameters(self, value: int):
        """Set nStorageParameters"""
        self.__nStorageParameters = int(value)

    @property
    def intParameters(self) -> List[StringIntItem]:
        """"""
        return self.__intParameters

    @intParameters.setter
    def intParameters(self, value: List[StringIntItem]):
        """Set intParameters"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__intParameters = value

    @property
    def doubleParameters(self) -> List[StringDoubleItem]:
        """"""
        return self.__doubleParameters

    @doubleParameters.setter
    def doubleParameters(self, value: List[StringDoubleItem]):
        """Set doubleParameters"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__doubleParameters = value

    @property
    def stringParameters(self) -> List[StringItem]:
        """"""
        return self.__stringParameters

    @stringParameters.setter
    def stringParameters(self, value: List[StringItem]):
        """Set stringParameters"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__stringParameters = value

    @property
    def nCurrentPoints(self) -> int:
        """Number of points where current velocities shall be given."""
        return self.__nCurrentPoints

    @nCurrentPoints.setter
    def nCurrentPoints(self, value: int):
        """Set nCurrentPoints"""
        self.__nCurrentPoints = int(value)

    @property
    def dllFile(self) -> str:
        """"""
        return self.__dllFile

    @dllFile.setter
    def dllFile(self, value: str):
        """Set dllFile"""
        self.__dllFile = str(value)

    @property
    def libraryPaths(self) -> LibraryPaths:
        """"""
        return self.__libraryPaths

    @libraryPaths.setter
    def libraryPaths(self, value: LibraryPaths):
        """Set libraryPaths"""
        self.__libraryPaths = value
