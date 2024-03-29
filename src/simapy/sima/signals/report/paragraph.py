# This an autogenerated file
# 
# Generated with Paragraph
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.paragraph import ParagraphBlueprint
from typing import Dict
from .reportitem import ReportItem

class Paragraph(ReportItem):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    text : str
         (default None)
    markup : bool
         (default False)
    """

    def __init__(self , description="", markup=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.text = None
        self.markup = markup
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ParagraphBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def text(self) -> str:
        """"""
        return self.__text

    @text.setter
    def text(self, value: str):
        """Set text"""
        self.__text = value

    @property
    def markup(self) -> bool:
        """"""
        return self.__markup

    @markup.setter
    def markup(self, value: bool):
        """Set markup"""
        self.__markup = bool(value)
