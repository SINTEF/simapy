# Generated with MatrixStorage
# 
from enum import Enum
from enum import auto

class MatrixStorage(Enum):
    """"""
    SKYLINE = auto()
    SPARSE = auto()

    def label(self):
        if self == MatrixStorage.SKYLINE:
            return "Skyline"
        if self == MatrixStorage.SPARSE:
            return "Sparse"