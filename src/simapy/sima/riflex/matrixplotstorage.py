# Generated with MatrixPlotStorage
# 
from enum import Enum
from enum import auto

class MatrixPlotStorage(Enum):
    """"""
    LOAD_GROUP = auto()
    LOAD_STEP = auto()
    END = auto()
    NONE = auto()

    def label(self):
        if self == MatrixPlotStorage.LOAD_GROUP:
            return "After each static load group"
        if self == MatrixPlotStorage.LOAD_STEP:
            return "After each static load step"
        if self == MatrixPlotStorage.END:
            return "At end of static analysis"
        if self == MatrixPlotStorage.NONE:
            return "No storage"