# This an autogenerated file
# 
# Generated with GuidePointSpecification
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.guidepointspecification import GuidePointSpecificationBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.guidepoint import GuidePoint

class GuidePointSpecification(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    guidePoint : GuidePoint
         Guide point
    enteredOnLine : bool
         Guide point entered on line(default True)
    """

    def __init__(self , description="", _id=None, enteredOnLine=True, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.guidePoint = None
        self.enteredOnLine = enteredOnLine
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GuidePointSpecificationBlueprint()


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
    def guidePoint(self) -> GuidePoint:
        """Guide point"""
        return self.__guidePoint

    @guidePoint.setter
    def guidePoint(self, value: GuidePoint):
        """Set guidePoint"""
        self.__guidePoint = value

    @property
    def enteredOnLine(self) -> bool:
        """Guide point entered on line"""
        return self.__enteredOnLine

    @enteredOnLine.setter
    def enteredOnLine(self, value: bool):
        """Set enteredOnLine"""
        self.__enteredOnLine = bool(value)
