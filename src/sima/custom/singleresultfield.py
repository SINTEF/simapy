# This an autogenerated file
# 
# Generated with SingleResultField
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.singleresultfield import SingleResultFieldBlueprint
from typing import Dict
from .customcomponent import CustomComponent
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.post import OutputNode

class SingleResultField(CustomComponent):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    output : OutputNode
    path : str
         (default None)
    label : str
         (default None)
    tooltip : str
         (default None)
    autoFormat : bool
         Format numbers automatically or choose appropriate format (default True)
    format : str
         Decimal numer format. Please refer to https://docs.oracle.com/javase/tutorial/i18n/format/decimalFormat.html for a description(default '0.000')
    """

    def __init__(self , description="", autoFormat=True, format='0.000', **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.output = None
        self.path = None
        self.label = None
        self.tooltip = None
        self.autoFormat = autoFormat
        self.format = format
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SingleResultFieldBlueprint()


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
    def output(self) -> OutputNode:
        """"""
        return self.__output

    @output.setter
    def output(self, value: OutputNode):
        """Set output"""
        self.__output = value

    @property
    def path(self) -> str:
        """"""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = value

    @property
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = value

    @property
    def tooltip(self) -> str:
        """"""
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, value: str):
        """Set tooltip"""
        self.__tooltip = value

    @property
    def autoFormat(self) -> bool:
        """Format numbers automatically or choose appropriate format """
        return self.__autoFormat

    @autoFormat.setter
    def autoFormat(self, value: bool):
        """Set autoFormat"""
        self.__autoFormat = bool(value)

    @property
    def format(self) -> str:
        """Decimal numer format. Please refer to https://docs.oracle.com/javase/tutorial/i18n/format/decimalFormat.html for a description"""
        return self.__format

    @format.setter
    def format(self, value: str):
        """Set format"""
        self.__format = value