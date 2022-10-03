# This an autogenerated file
# 
# Generated with Appendix
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.appendix import AppendixBlueprint
from typing import Dict
from marmo.report.reportitem import ReportItem
from marmo.report.section import Section

class Appendix(Section):
    """
    Keyword arguments
    -----------------
    items : List[ReportItem]
    title : str
         (default "")
    landscape : bool
         (default False)
    """

    def __init__(self , title="", landscape=False, **kwargs):
        super().__init__(**kwargs)
        self.items = list()
        self.title = title
        self.landscape = landscape
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AppendixBlueprint()


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
