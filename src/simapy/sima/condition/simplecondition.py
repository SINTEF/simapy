# This an autogenerated file
# 
# Generated with SimpleCondition
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.simplecondition import SimpleConditionBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import ResultContainer
from ..sima import ScriptableValue
from ..sima import VariableItem
from .conditiontaskcondition import ConditionTaskCondition
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..sima import ConditionSelectable
    from ..sima import DoubleVariable
    from .modelvariation import ModelVariation

class SimpleCondition(ConditionTaskCondition,NamedObject):
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
    probabilityVariable : DoubleVariable
         Used to set a probability for single runs
    variation : ModelVariation
    """

    def __init__(self , description="", changeNumber=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.changeNumber = changeNumber
        self.resultContainer = None
        self.selection = None
        self.variableItems = list()
        self.probabilityVariable = None
        self.variation = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SimpleConditionBlueprint()


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
            raise ValueError("Expected sequense, but was " , type(value))
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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__variableItems = value

    @property
    def probabilityVariable(self) -> DoubleVariable:
        """Used to set a probability for single runs"""
        return self.__probabilityVariable

    @probabilityVariable.setter
    def probabilityVariable(self, value: DoubleVariable):
        """Set probabilityVariable"""
        self.__probabilityVariable = value

    @property
    def variation(self) -> ModelVariation:
        """"""
        return self.__variation

    @variation.setter
    def variation(self, value: ModelVariation):
        """Set variation"""
        self.__variation = value
