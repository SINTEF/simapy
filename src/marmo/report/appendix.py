# This an autogenerated file
# 
# Generated with Appendix
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.appendix import AppendixBlueprint
from typing import Dict,Sequence,List
from marmo.report.reportitem import ReportItem

class Appendix(Entity):
    """
    
    
    Keyword arguments
    -----------------
    name : str 
         (default "")
    description : str 
         (default "")
    items : List[ReportItem] 
         
    title : str 
         (default "")
    landscape : bool 
         (default False)
    """

    def __init__(self , name:str="", description:str="", title:str="", landscape:bool=False, **kwargs):
        self.__name = name
        self.__description = description
        self.__items = list()
        self.__title = title
        self.__landscape = landscape
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AppendixBlueprint()


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
    def items(self) -> List[ReportItem]:
        """"""
        return self.__items

    @items.setter
    def items(self, value: List[ReportItem]):
        """Set items"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__items = value

    @property
    def title(self) -> str:
        """"""
        return self.__title

    @title.setter
    def title(self, value: str):
        """Set title"""
        self.__title = str(value)

    @property
    def landscape(self) -> bool:
        """"""
        return self.__landscape

    @landscape.setter
    def landscape(self, value: bool):
        """Set landscape"""
        self.__landscape = bool(value)
