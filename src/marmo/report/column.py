# This an autogenerated file
# 
# Generated with Column
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.column import ColumnBlueprint
from typing import Dict
from marmo.report.font import Font

class Column(Entity):
    """
    
    
    Keyword arguments
    -----------------
    name : str 
         (default "")
    description : str 
         (default "")
    header : str 
         (default "")
    label : str 
         (default "")
    headerfont : Font 
         
    """

    def __init__(self , name:str="", description:str="", header:str="", label:str="", **kwargs):
        self.__name = name
        self.__description = description
        self.__header = header
        self.__label = label
        self.__headerfont = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ColumnBlueprint()


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
    def header(self) -> str:
        """"""
        return self.__header

    @header.setter
    def header(self, value: str):
        """Set header"""
        self.__header = str(value)

    @property
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = str(value)

    @property
    def headerfont(self) -> Font:
        """"""
        return self.__headerfont

    @headerfont.setter
    def headerfont(self, value: Font):
        """Set headerfont"""
        self.__headerfont = value
