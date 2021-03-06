# This an autogenerated file
# 
# Generated with Formula
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.formula import FormulaBlueprint
from typing import Dict
from sima.report.reportitem import ReportItem
from sima.sima.scriptablevalue import ScriptableValue

class Formula(ReportItem):
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
    latex : str
         (default "")
    caption : str
         Caption(default "")
    """

    def __init__(self , name="", description="", _id="", latex="", caption="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.latex = latex
        self.caption = caption
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FormulaBlueprint()


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
    def latex(self) -> str:
        """"""
        return self.__latex

    @latex.setter
    def latex(self, value: str):
        """Set latex"""
        self.__latex = str(value)

    @property
    def caption(self) -> str:
        """Caption"""
        return self.__caption

    @caption.setter
    def caption(self, value: str):
        """Set caption"""
        self.__caption = str(value)
