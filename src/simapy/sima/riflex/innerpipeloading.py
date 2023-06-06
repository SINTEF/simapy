# Generated with InnerPipeLoading
# 
from enum import Enum
from enum import auto

class InnerPipeLoading(Enum):
    """"""
    EXPOSED = auto()
    SHELTERED_CLOSED = auto()

    def label(self):
        if self == InnerPipeLoading.EXPOSED:
            return "Exposed"
        if self == InnerPipeLoading.SHELTERED_CLOSED:
            return "Sheltered Closed"