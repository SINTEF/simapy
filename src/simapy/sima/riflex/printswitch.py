# Generated with PrintSwitch
# 
from enum import Enum
from enum import auto

class PrintSwitch(Enum):
    """"""
    FINAL_RESULTS = auto()
    FINAL_RESULTS_FINAL_ITERATION = auto()
    FINAL_RESULTS_ALL_ITERATIONS = auto()

    def label(self):
        if self == PrintSwitch.FINAL_RESULTS:
            return "Final results only"
        if self == PrintSwitch.FINAL_RESULTS_FINAL_ITERATION:
            return "Final results and final interation"
        if self == PrintSwitch.FINAL_RESULTS_ALL_ITERATIONS:
            return "Final results and all iterations"