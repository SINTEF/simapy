# This an autogenerated file
# 
# Generated with ConditionTest
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.conditiontest import ConditionTestBlueprint
from typing import Dict
from .comparisonassertion import ComparisonAssertion
from .duration import Duration
from .outputnodevalueassertion import OutputNodeValueAssertion
from .test import Test
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima import Condition

class ConditionTest(Test):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    disabled : bool
         If disabled, the test will not be run in a continuous integration environment(default False)
    duration : Duration
    assertions : List[OutputNodeValueAssertion]
    comparisons : List[ComparisonAssertion]
    condition : Condition
    analysis : str
         (default None)
    """

    def __init__(self , description="", disabled=False, duration=Duration.MEDIUM, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.disabled = disabled
        self.duration = duration
        self.assertions = list()
        self.comparisons = list()
        self.condition = None
        self.analysis = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ConditionTestBlueprint()


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
    def disabled(self) -> bool:
        """If disabled, the test will not be run in a continuous integration environment"""
        return self.__disabled

    @disabled.setter
    def disabled(self, value: bool):
        """Set disabled"""
        self.__disabled = bool(value)

    @property
    def duration(self) -> Duration:
        """"""
        return self.__duration

    @duration.setter
    def duration(self, value: Duration):
        """Set duration"""
        self.__duration = value

    @property
    def assertions(self) -> List[OutputNodeValueAssertion]:
        """"""
        return self.__assertions

    @assertions.setter
    def assertions(self, value: List[OutputNodeValueAssertion]):
        """Set assertions"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__assertions = value

    @property
    def comparisons(self) -> List[ComparisonAssertion]:
        """"""
        return self.__comparisons

    @comparisons.setter
    def comparisons(self, value: List[ComparisonAssertion]):
        """Set comparisons"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__comparisons = value

    @property
    def condition(self) -> Condition:
        """"""
        return self.__condition

    @condition.setter
    def condition(self, value: Condition):
        """Set condition"""
        self.__condition = value

    @property
    def analysis(self) -> str:
        """"""
        return self.__analysis

    @analysis.setter
    def analysis(self, value: str):
        """Set analysis"""
        self.__analysis = value
