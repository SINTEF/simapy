# This an autogenerated file
# 
# Generated with HLADataTable
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hladatatable import HLADataTableBlueprint
from typing import Dict
from sima.hla.hlasignal import HLASignal
from sima.sima.named import Named
from sima.sima.scriptablevalue import ScriptableValue

class HLADataTable(Named):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    signals : List[HLASignal]
    showHorisontalTable : bool
         (default False)
    """

    def __init__(self , description="", showHorisontalTable=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.signals = list()
        self.showHorisontalTable = showHorisontalTable
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HLADataTableBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def signals(self) -> List[HLASignal]:
        """"""
        return self.__signals

    @signals.setter
    def signals(self, value: List[HLASignal]):
        """Set signals"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__signals = value

    @property
    def showHorisontalTable(self) -> bool:
        """"""
        return self.__showHorisontalTable

    @showHorisontalTable.setter
    def showHorisontalTable(self, value: bool):
        """Set showHorisontalTable"""
        self.__showHorisontalTable = bool(value)
