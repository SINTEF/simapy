# This an autogenerated file
# 
# Generated with WamitTask
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wamittask import WamitTaskBlueprint
from typing import Dict
from .wamitmodel import WamitModel
from sima.condition import ConditionTask
from sima.condition import ConditionTaskCondition
from sima.condition import InitialCondition
from sima.condition import ModelVariation
from sima.sima import DoubleVariable
from sima.sima import IntegerVariable
from sima.sima import ModelReferenceVariable
from sima.sima import SIMAScript
from sima.sima import ScriptableValue
from sima.sima import StringVariable

class WamitTask(ConditionTask):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    doubleVariables : List[DoubleVariable]
    integerVariables : List[IntegerVariable]
    stringVariables : List[StringVariable]
    runNumber : int
         (default 0)
    scripts : List[SIMAScript]
    variations : List[ModelVariation]
    referenceVariables : List[ModelReferenceVariable]
    initialCondition : InitialCondition
    conditions : List[ConditionTaskCondition]
    model : WamitModel
    """

    def __init__(self , description="", runNumber=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.doubleVariables = list()
        self.integerVariables = list()
        self.stringVariables = list()
        self.runNumber = runNumber
        self.scripts = list()
        self.variations = list()
        self.referenceVariables = list()
        self.initialCondition = None
        self.conditions = list()
        self.model = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WamitTaskBlueprint()


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
    def doubleVariables(self) -> List[DoubleVariable]:
        """"""
        return self.__doubleVariables

    @doubleVariables.setter
    def doubleVariables(self, value: List[DoubleVariable]):
        """Set doubleVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__doubleVariables = value

    @property
    def integerVariables(self) -> List[IntegerVariable]:
        """"""
        return self.__integerVariables

    @integerVariables.setter
    def integerVariables(self, value: List[IntegerVariable]):
        """Set integerVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__integerVariables = value

    @property
    def stringVariables(self) -> List[StringVariable]:
        """"""
        return self.__stringVariables

    @stringVariables.setter
    def stringVariables(self, value: List[StringVariable]):
        """Set stringVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__stringVariables = value

    @property
    def runNumber(self) -> int:
        """"""
        return self.__runNumber

    @runNumber.setter
    def runNumber(self, value: int):
        """Set runNumber"""
        self.__runNumber = int(value)

    @property
    def scripts(self) -> List[SIMAScript]:
        """"""
        return self.__scripts

    @scripts.setter
    def scripts(self, value: List[SIMAScript]):
        """Set scripts"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scripts = value

    @property
    def variations(self) -> List[ModelVariation]:
        """"""
        return self.__variations

    @variations.setter
    def variations(self, value: List[ModelVariation]):
        """Set variations"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__variations = value

    @property
    def referenceVariables(self) -> List[ModelReferenceVariable]:
        """"""
        return self.__referenceVariables

    @referenceVariables.setter
    def referenceVariables(self, value: List[ModelReferenceVariable]):
        """Set referenceVariables"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__referenceVariables = value

    @property
    def initialCondition(self) -> InitialCondition:
        """"""
        return self.__initialCondition

    @initialCondition.setter
    def initialCondition(self, value: InitialCondition):
        """Set initialCondition"""
        self.__initialCondition = value

    @property
    def conditions(self) -> List[ConditionTaskCondition]:
        """"""
        return self.__conditions

    @conditions.setter
    def conditions(self, value: List[ConditionTaskCondition]):
        """Set conditions"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__conditions = value

    @property
    def model(self) -> WamitModel:
        """"""
        return self.__model

    @model.setter
    def model(self, value: WamitModel):
        """Set model"""
        self.__model = value
