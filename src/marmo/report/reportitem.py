# This an autogenerated file
# 
# Generated with ReportItem
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.reportitem import ReportItemBlueprint
from typing import Dict

class ReportItem(Entity):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    """

    def __init__(self , name="", description="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ReportItemBlueprint()


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
