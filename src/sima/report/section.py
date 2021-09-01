# This an autogenerated file
# 
# Generated with Section
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.section import SectionBlueprint
from sima.report.linkable import Linkable
from sima.report.orientation import Orientation
from sima.report.reportitem import ReportItem
from sima.sima.scriptablevalue import ScriptableValue

class Section(ReportItem,Linkable):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    identifier : str
         (default "")
    items : List[ReportItem]
    title : str
         The title of the section.(default "")
    pageBreakBefore : bool
         (default False)
    orientation : Orientation
    """

    def __init__(self , name:str="", description:str="", _id:str="", identifier:str="", title:str="", pageBreakBefore:bool=False, orientation:Orientation=Orientation.PORTRAIT, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.___id = _id
        self.__scriptableValues = list()
        self.__identifier = identifier
        self.__items = list()
        self.__title = title
        self.__pageBreakBefore = pageBreakBefore
        self.__orientation = orientation
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SectionBlueprint()


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
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

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
    def identifier(self) -> str:
        """"""
        return self.__identifier

    @identifier.setter
    def identifier(self, value: str):
        """Set identifier"""
        self.__identifier = str(value)

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
        """The title of the section."""
        return self.__title

    @title.setter
    def title(self, value: str):
        """Set title"""
        self.__title = str(value)

    @property
    def pageBreakBefore(self) -> bool:
        """"""
        return self.__pageBreakBefore

    @pageBreakBefore.setter
    def pageBreakBefore(self, value: bool):
        """Set pageBreakBefore"""
        self.__pageBreakBefore = bool(value)

    @property
    def orientation(self) -> Orientation:
        """"""
        return self.__orientation

    @orientation.setter
    def orientation(self, value: Orientation):
        """Set orientation"""
        self.__orientation = value
