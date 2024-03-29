# This an autogenerated file
# 
# Generated with ExternalHLAForce
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.externalhlaforce import ExternalHLAForceBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import Point3
from ..sima import ScriptableValue
from .referenceframetype import ReferenceFrameType
from .stringdoubleitem import StringDoubleItem
from .stringintitem import StringIntItem
from .stringitem import StringItem

class ExternalHLAForce(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    attachmentPoint : Point3
         Attack point of force.
    referenceFrame : ReferenceFrameType
         Which coordinate system is the force is given in?
    nStorageParameters : int
         Number of parameters for intermediate storage(default 0)
    intParameters : List[StringIntItem]
    doubleParameters : List[StringDoubleItem]
    stringParameters : List[StringItem]
    importAttackPoint : bool
         (default False)
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

    def __init__(self , description="", referenceFrame=ReferenceFrameType.LOCAL, nStorageParameters=0, importAttackPoint=False, fx=0.0, fy=0.0, fz=0.0, mx=0.0, my=0.0, mz=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.attachmentPoint = None
        self.referenceFrame = referenceFrame
        self.nStorageParameters = nStorageParameters
        self.intParameters = list()
        self.doubleParameters = list()
        self.stringParameters = list()
        self.importAttackPoint = importAttackPoint
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
        return ExternalHLAForceBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__intParameters = value

    @property
    def doubleParameters(self) -> List[StringDoubleItem]:
        """"""
        return self.__doubleParameters

    @doubleParameters.setter
    def doubleParameters(self, value: List[StringDoubleItem]):
        """Set doubleParameters"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__doubleParameters = value

    @property
    def stringParameters(self) -> List[StringItem]:
        """"""
        return self.__stringParameters

    @stringParameters.setter
    def stringParameters(self, value: List[StringItem]):
        """Set stringParameters"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__stringParameters = value

    @property
    def importAttackPoint(self) -> bool:
        """"""
        return self.__importAttackPoint

    @importAttackPoint.setter
    def importAttackPoint(self, value: bool):
        """Set importAttackPoint"""
        self.__importAttackPoint = bool(value)

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
