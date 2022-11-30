# This an autogenerated file
# 
# Generated with ConditionSpace
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.conditionspace import ConditionSpaceBlueprint
from typing import Dict
from sima.condition.conditiontaskcondition import ConditionTaskCondition
from sima.condition.variableitemset import VariableItemSet
from sima.sima.namedobject import NamedObject
from sima.sima.resultcontainer import ResultContainer
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.variableitem import VariableItem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima.conditionselectable import ConditionSelectable

class ConditionSpace(ConditionTaskCondition,NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    changeNumber : int
         (default 0)
    resultContainer : ResultContainer
    selection : ConditionSelectable
    variableItems : List[VariableItem]
    variableItemSets : List[VariableItemSet]
    inputFromFile : bool
         Specify variable values from file.(default False)
    path : str
         Import variable values from file. Expected file format:\n' any comment specified with '\n'Hs    Tp     seed : values specified in rows ( Need to match the variables specified)  \n1.0      2.0    3\n4.0      5.0    4\n'any comment\n           (default None)
    """

    def __init__(self , description="", changeNumber=0, inputFromFile=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.changeNumber = changeNumber
        self.resultContainer = None
        self.selection = None
        self.variableItems = list()
        self.variableItemSets = list()
        self.inputFromFile = inputFromFile
        self.path = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ConditionSpaceBlueprint()


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
    def changeNumber(self) -> int:
        """"""
        return self.__changeNumber

    @changeNumber.setter
    def changeNumber(self, value: int):
        """Set changeNumber"""
        self.__changeNumber = int(value)

    @property
    def resultContainer(self) -> ResultContainer:
        """"""
        return self.__resultContainer

    @resultContainer.setter
    def resultContainer(self, value: ResultContainer):
        """Set resultContainer"""
        self.__resultContainer = value

    @property
    def selection(self) -> ConditionSelectable:
        """"""
        return self.__selection

    @selection.setter
    def selection(self, value: ConditionSelectable):
        """Set selection"""
        self.__selection = value

    @property
    def variableItems(self) -> List[VariableItem]:
        """"""
        return self.__variableItems

    @variableItems.setter
    def variableItems(self, value: List[VariableItem]):
        """Set variableItems"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__variableItems = value

    @property
    def variableItemSets(self) -> List[VariableItemSet]:
        """"""
        return self.__variableItemSets

    @variableItemSets.setter
    def variableItemSets(self, value: List[VariableItemSet]):
        """Set variableItemSets"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__variableItemSets = value

    @property
    def inputFromFile(self) -> bool:
        """Specify variable values from file."""
        return self.__inputFromFile

    @inputFromFile.setter
    def inputFromFile(self, value: bool):
        """Set inputFromFile"""
        self.__inputFromFile = bool(value)

    @property
    def path(self) -> str:
        """Import variable values from file. Expected file format:
' any comment specified with '
'Hs    Tp     seed : values specified in rows ( Need to match the variables specified)  
1.0      2.0    3
4.0      5.0    4
'any comment
           """
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = value
