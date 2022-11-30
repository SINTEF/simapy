# This an autogenerated file
# 
# Generated with ARLine
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.arline import ARLineBlueprint
from typing import Dict
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.lineforceprovider import LineForceProvider
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arlinetype import ARLineType
    from sima.riflex.supernode import SuperNode

class ARLine(LineForceProvider):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    lineType : ARLineType
         Line type.
    end1 : SuperNode
         Supernode at end 1.
    end2 : SuperNode
         Supernode at end 2.
    disabled : bool
         Do not include this line in the calculations(default False)
    """

    def __init__(self , description="", disabled=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.lineType = None
        self.end1 = None
        self.end2 = None
        self.disabled = disabled
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ARLineBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
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
    def lineType(self) -> ARLineType:
        """Line type."""
        return self.__lineType

    @lineType.setter
    def lineType(self, value: ARLineType):
        """Set lineType"""
        self.__lineType = value

    @property
    def end1(self) -> SuperNode:
        """Supernode at end 1."""
        return self.__end1

    @end1.setter
    def end1(self, value: SuperNode):
        """Set end1"""
        self.__end1 = value

    @property
    def end2(self) -> SuperNode:
        """Supernode at end 2."""
        return self.__end2

    @end2.setter
    def end2(self, value: SuperNode):
        """Set end2"""
        self.__end2 = value

    @property
    def disabled(self) -> bool:
        """Do not include this line in the calculations"""
        return self.__disabled

    @disabled.setter
    def disabled(self, value: bool):
        """Set disabled"""
        self.__disabled = bool(value)
