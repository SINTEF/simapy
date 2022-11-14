# This an autogenerated file
# 
# Generated with TableCellStyle
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.tablecellstyle import TableCellStyleBlueprint
from typing import Dict
from sima.report.horizontalalignment import HorizontalAlignment
from sima.report.verticalalignment import VerticalAlignment
from sima.sima.fontdescription import FontDescription
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class TableCellStyle(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    font : FontDescription
    horizontalTextAlignment : HorizontalAlignment
    verticalTextAlignment : VerticalAlignment
    """

    def __init__(self , description="", _id=None, horizontalTextAlignment=HorizontalAlignment.LEFT, verticalTextAlignment=VerticalAlignment.TOP, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.font = None
        self.horizontalTextAlignment = horizontalTextAlignment
        self.verticalTextAlignment = verticalTextAlignment
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TableCellStyleBlueprint()


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
    def font(self) -> FontDescription:
        """"""
        return self.__font

    @font.setter
    def font(self, value: FontDescription):
        """Set font"""
        self.__font = value

    @property
    def horizontalTextAlignment(self) -> HorizontalAlignment:
        """"""
        return self.__horizontalTextAlignment

    @horizontalTextAlignment.setter
    def horizontalTextAlignment(self, value: HorizontalAlignment):
        """Set horizontalTextAlignment"""
        self.__horizontalTextAlignment = value

    @property
    def verticalTextAlignment(self) -> VerticalAlignment:
        """"""
        return self.__verticalTextAlignment

    @verticalTextAlignment.setter
    def verticalTextAlignment(self, value: VerticalAlignment):
        """Set verticalTextAlignment"""
        self.__verticalTextAlignment = value
