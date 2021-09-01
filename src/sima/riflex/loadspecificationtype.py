# Generated with LoadSpecificationType
# 
from enum import Enum
from enum import auto

class LoadSpecificationType(Enum):
    """"""
    NOFILE = auto()
    FILE = auto()

    def label(self):
        if self == LoadSpecificationType.NOFILE:
            return "No file"
        if self == LoadSpecificationType.FILE:
            return "File"