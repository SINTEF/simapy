# Generated with ISO19901_7_analysis
# 
from enum import Enum
from enum import auto

class ISO19901_7_analysis(Enum):
    """"""
    INTACT_CONDITION = auto()
    ONE_FAILURE = auto()
    ONE_FAILURE_TRANSIENT = auto()
    TWO_FAILURES = auto()
    TWO_FAILURES_TRANSIENT = auto()

    def label(self):
        if self == ISO19901_7_analysis.INTACT_CONDITION:
            return "Intact condition"
        if self == ISO19901_7_analysis.ONE_FAILURE:
            return "One failure"
        if self == ISO19901_7_analysis.ONE_FAILURE_TRANSIENT:
            return "One failure, transient"
        if self == ISO19901_7_analysis.TWO_FAILURES:
            return "Two failures"
        if self == ISO19901_7_analysis.TWO_FAILURES_TRANSIENT:
            return "Two failures, transient"