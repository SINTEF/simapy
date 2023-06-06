# Generated with SortDirection
# 
from enum import Enum
from enum import auto

class SortDirection(Enum):
    """"""
    ASCENDING = auto()
    DESCENDING = auto()

    def label(self):
        if self == SortDirection.ASCENDING:
            return "Ascending"
        if self == SortDirection.DESCENDING:
            return "Descending"