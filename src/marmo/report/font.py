# This an autogenerated file
# 
# Generated with Font
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.font import FontBlueprint
from typing import Dict
from dmt.entity import Entity
from marmo.report.fontstyle import FontStyle

class Font(Entity):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    size : int
         (default 10)
    font : str
         (default None)
    style : FontStyle
    """

    def __init__(self , description="", size=10, font=None, style=FontStyle.NORMAL, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.size = size
        self.font = font
        self.style = style
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FontBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def size(self) -> int:
        """"""
        return self.__size

    @size.setter
    def size(self, value: int):
        """Set size"""
        self.__size = int(value)

    @property
    def font(self) -> str:
        """"""
        return self.__font

    @font.setter
    def font(self, value: str):
        """Set font"""
        self.__font = str(value)

    @property
    def style(self) -> FontStyle:
        """"""
        return self.__style

    @style.setter
    def style(self, value: FontStyle):
        """Set style"""
        self.__style = value
