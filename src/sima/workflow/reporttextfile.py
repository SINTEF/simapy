# This an autogenerated file
# 
# Generated with ReportTextFile
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.reporttextfile import ReportTextFileBlueprint
from typing import Dict
from sima.sima.scriptablevalue import ScriptableValue
from sima.workflow.reportfragmentitem import ReportFragmentItem

class ReportTextFile(ReportFragmentItem):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    path : str
         (default None)
    plainText : bool
         (default False)
    """

    def __init__(self , description="", plainText=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.path = None
        self.plainText = plainText
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ReportTextFileBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

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
    def path(self) -> str:
        """"""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = value

    @property
    def plainText(self) -> bool:
        """"""
        return self.__plainText

    @plainText.setter
    def plainText(self, value: bool):
        """Set plainText"""
        self.__plainText = bool(value)
