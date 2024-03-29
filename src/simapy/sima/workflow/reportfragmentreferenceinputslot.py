# This an autogenerated file
# 
# Generated with ReportFragmentReferenceInputSlot
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.reportfragmentreferenceinputslot import ReportFragmentReferenceInputSlotBlueprint
from typing import Dict
from ..post import InputSlot
from ..sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..report import ReportFragment

class ReportFragmentReferenceInputSlot(InputSlot):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    fragment : ReportFragment
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.fragment = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ReportFragmentReferenceInputSlotBlueprint()


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
    def fragment(self) -> ReportFragment:
        """"""
        return self.__fragment

    @fragment.setter
    def fragment(self, value: ReportFragment):
        """Set fragment"""
        self.__fragment = value
