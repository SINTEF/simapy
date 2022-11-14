# This an autogenerated file
# 
# Generated with ExternalForceFromFile
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.externalforcefromfile import ExternalForceFromFileBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.referenceframetype import ReferenceFrameType

class ExternalForceFromFile(NamedObject):
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
    forceFile : str
         ' File heading,  arbitrary number of lines with \n' apostrophe in the first position of the input line\nNCOL: Number of columns (=6)\nNROW: Number of rows (i.e. no. of time incidents)\nSAMP: Sampling interval [T]\nForce components, NROW lines (one per time incident)\nFX   FY   FZ   MX   MY   MZ\nFX   FY   FZ   MX   MY   MZ\nFX   FY   FZ   MX   MY   MZ\nFX   FY   FZ   MX   MY   MZ\n(default None)
    referenceFrame : ReferenceFrameType
         Which coordinate system is the force is given in?
    attachmentPoint : Point3
         Attack point of force.
    fx : float
         Force in X-direction(default 0.0)
    fy : float
         Force in Y-direction(default 0.0)
    fz : float
         Force in Z-direction(default 0.0)
    mx : float
         Moment about X-axis(default 0.0)
    my : float
         Moment about Y-axis(default 0.0)
    mz : float
         Moment about Z-axis(default 0.0)
    """

    def __init__(self , description="", _id=None, name=None, forceFile=None, referenceFrame=ReferenceFrameType.LOCAL, fx=0.0, fy=0.0, fz=0.0, mx=0.0, my=0.0, mz=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.forceFile = forceFile
        self.referenceFrame = referenceFrame
        self.attachmentPoint = None
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.mx = mx
        self.my = my
        self.mz = mz
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExternalForceFromFileBlueprint()


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
    def forceFile(self) -> str:
        """' File heading,  arbitrary number of lines with 
' apostrophe in the first position of the input line
NCOL: Number of columns (=6)
NROW: Number of rows (i.e. no. of time incidents)
SAMP: Sampling interval [T]
Force components, NROW lines (one per time incident)
FX   FY   FZ   MX   MY   MZ
FX   FY   FZ   MX   MY   MZ
FX   FY   FZ   MX   MY   MZ
FX   FY   FZ   MX   MY   MZ
"""
        return self.__forceFile

    @forceFile.setter
    def forceFile(self, value: str):
        """Set forceFile"""
        self.__forceFile = str(value)

    @property
    def referenceFrame(self) -> ReferenceFrameType:
        """Which coordinate system is the force is given in?"""
        return self.__referenceFrame

    @referenceFrame.setter
    def referenceFrame(self, value: ReferenceFrameType):
        """Set referenceFrame"""
        self.__referenceFrame = value

    @property
    def attachmentPoint(self) -> Point3:
        """Attack point of force."""
        return self.__attachmentPoint

    @attachmentPoint.setter
    def attachmentPoint(self, value: Point3):
        """Set attachmentPoint"""
        self.__attachmentPoint = value

    @property
    def fx(self) -> float:
        """Force in X-direction"""
        return self.__fx

    @fx.setter
    def fx(self, value: float):
        """Set fx"""
        self.__fx = float(value)

    @property
    def fy(self) -> float:
        """Force in Y-direction"""
        return self.__fy

    @fy.setter
    def fy(self, value: float):
        """Set fy"""
        self.__fy = float(value)

    @property
    def fz(self) -> float:
        """Force in Z-direction"""
        return self.__fz

    @fz.setter
    def fz(self, value: float):
        """Set fz"""
        self.__fz = float(value)

    @property
    def mx(self) -> float:
        """Moment about X-axis"""
        return self.__mx

    @mx.setter
    def mx(self, value: float):
        """Set mx"""
        self.__mx = float(value)

    @property
    def my(self) -> float:
        """Moment about Y-axis"""
        return self.__my

    @my.setter
    def my(self, value: float):
        """Set my"""
        self.__my = float(value)

    @property
    def mz(self) -> float:
        """Moment about Z-axis"""
        return self.__mz

    @mz.setter
    def mz(self, value: float):
        """Set mz"""
        self.__mz = float(value)
