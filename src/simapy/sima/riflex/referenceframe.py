# This an autogenerated file
# 
# Generated with ReferenceFrame
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.referenceframe import ReferenceFrameBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import ScriptableValue

class ReferenceFrame(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    parent : ReferenceFrame
    xLocal : float
         Local (in parent frame) coordinate X(default 0.0)
    yLocal : float
         Local (in parent frame) coordinate Y(default 0.0)
    zLocal : float
         Local (in parent frame) coordinate Z(default 0.0)
    rxLocal : float
         Local (relative to parent frame)  X-axis rotation(default 0.0)
    ryLocal : float
         Local (relative to parent frame)  Y-axis rotation(default 0.0)
    rzLocal : float
         Local (relative to parent frame)  Z-axis rotation(default 0.0)
    """

    def __init__(self , description="", xLocal=0.0, yLocal=0.0, zLocal=0.0, rxLocal=0.0, ryLocal=0.0, rzLocal=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.parent = None
        self.xLocal = xLocal
        self.yLocal = yLocal
        self.zLocal = zLocal
        self.rxLocal = rxLocal
        self.ryLocal = ryLocal
        self.rzLocal = rzLocal
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ReferenceFrameBlueprint()


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
    def parent(self) -> ReferenceFrame:
        """"""
        return self.__parent

    @parent.setter
    def parent(self, value: ReferenceFrame):
        """Set parent"""
        self.__parent = value

    @property
    def xLocal(self) -> float:
        """Local (in parent frame) coordinate X"""
        return self.__xLocal

    @xLocal.setter
    def xLocal(self, value: float):
        """Set xLocal"""
        self.__xLocal = float(value)

    @property
    def yLocal(self) -> float:
        """Local (in parent frame) coordinate Y"""
        return self.__yLocal

    @yLocal.setter
    def yLocal(self, value: float):
        """Set yLocal"""
        self.__yLocal = float(value)

    @property
    def zLocal(self) -> float:
        """Local (in parent frame) coordinate Z"""
        return self.__zLocal

    @zLocal.setter
    def zLocal(self, value: float):
        """Set zLocal"""
        self.__zLocal = float(value)

    @property
    def rxLocal(self) -> float:
        """Local (relative to parent frame)  X-axis rotation"""
        return self.__rxLocal

    @rxLocal.setter
    def rxLocal(self, value: float):
        """Set rxLocal"""
        self.__rxLocal = float(value)

    @property
    def ryLocal(self) -> float:
        """Local (relative to parent frame)  Y-axis rotation"""
        return self.__ryLocal

    @ryLocal.setter
    def ryLocal(self, value: float):
        """Set ryLocal"""
        self.__ryLocal = float(value)

    @property
    def rzLocal(self) -> float:
        """Local (relative to parent frame)  Z-axis rotation"""
        return self.__rzLocal

    @rzLocal.setter
    def rzLocal(self, value: float):
        """Set rzLocal"""
        self.__rzLocal = float(value)
