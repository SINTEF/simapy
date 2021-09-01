# Generated with Logical
# 
from enum import Enum
from enum import auto

class Logical(Enum):
    """"""
    OR = auto()
    AND = auto()
    NOT = auto()

    def label(self):
        if self == Logical.OR:
            return "OR"
        if self == Logical.AND:
            return "AND"
        if self == Logical.NOT:
            return "NOT"