# Generated with StorageTaskType
# 
from enum import Enum
from enum import auto

class StorageTaskType(Enum):
    """"""
    PRIVATE = auto()
    SHARED = auto()

    def label(self):
        if self == StorageTaskType.PRIVATE:
            return "Private"
        if self == StorageTaskType.SHARED:
            return "Shared"