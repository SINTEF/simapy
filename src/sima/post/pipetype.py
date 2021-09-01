# Generated with PipeType
# 
from enum import Enum
from enum import auto

class PipeType(Enum):
    """"""
    COLD_EXPANDED = auto()
    SEAMLESS = auto()

    def label(self):
        if self == PipeType.COLD_EXPANDED:
            return "ColdExpanded/DSAW"
        if self == PipeType.SEAMLESS:
            return "Seamless/ERW"