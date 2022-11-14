# This an autogenerated file
# 
# Generated with FontDescription
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fontdescription import FontDescriptionBlueprint
from typing import Dict
from sima.sima.fontstyle import FontStyle
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.simacolor import SIMAColor

class FontDescription(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    font : str
         (default None)
    size : int
         (default 0)
    style : FontStyle
    color : SIMAColor
    """

    def __init__(self , description="", _id=None, font=None, size=0, style=FontStyle.NORMAL, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.font = font
        self.size = size
        self.style = style
        self.color = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FontDescriptionBlueprint()


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
    def font(self) -> str:
        """"""
        return self.__font

    @font.setter
    def font(self, value: str):
        """Set font"""
        self.__font = str(value)

    @property
    def size(self) -> int:
        """"""
        return self.__size

    @size.setter
    def size(self, value: int):
        """Set size"""
        self.__size = int(value)

    @property
    def style(self) -> FontStyle:
        """"""
        return self.__style

    @style.setter
    def style(self, value: FontStyle):
        """Set style"""
        self.__style = value

    @property
    def color(self) -> SIMAColor:
        """"""
        return self.__color

    @color.setter
    def color(self, value: SIMAColor):
        """Set color"""
        self.__color = value
