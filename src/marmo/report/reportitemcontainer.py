# This an autogenerated file
# 
# Generated with ReportItemContainer
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.reportitemcontainer import ReportItemContainerBlueprint
from typing import Dict
from marmo.report.reportitem import ReportItem

class ReportItemContainer(Entity):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    items : List[ReportItem]
    """

    def __init__(self , name="", description="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.items = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ReportItemContainerBlueprint()


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
