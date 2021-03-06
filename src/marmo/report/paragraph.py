# This an autogenerated file
# 
# Generated with Paragraph
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.paragraph import ParagraphBlueprint
from typing import Dict
from marmo.report.reportitem import ReportItem

class Paragraph(ReportItem):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    text : str
         (default "")
    markup : bool
         (default False)
    """

    def __init__(self , name="", description="", text="", markup=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.text = text
        self.markup = markup
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ParagraphBlueprint()


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
    def text(self) -> str:
        """"""
        return self.__text

    @text.setter
    def text(self, value: str):
        """Set text"""
        self.__text = str(value)

    @property
    def markup(self) -> bool:
        """"""
        return self.__markup

    @markup.setter
    def markup(self, value: bool):
        """Set markup"""
        self.__markup = bool(value)
