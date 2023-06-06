# Generated with FieldType
# 
from enum import Enum
from enum import auto

class FieldType(Enum):
    """"""
    TEXT = auto()
    CHECK = auto()
    FILE = auto()
    DROPDOWN = auto()

    def label(self):
        if self == FieldType.TEXT:
            return "Text"
        if self == FieldType.CHECK:
            return "Checkbox"
        if self == FieldType.FILE:
            return "File"
        if self == FieldType.DROPDOWN:
            return "Drop-down"