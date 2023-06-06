# Generated with SurfacesToIncludeFromMs2FileOption
# 
from enum import Enum
from enum import auto

class SurfacesToIncludeFromMs2FileOption(Enum):
    """"""
    ALLVISIBLESURFACES = auto()
    SELECTEDENTITYLIST = auto()

    def label(self):
        if self == SurfacesToIncludeFromMs2FileOption.ALLVISIBLESURFACES:
            return "All visible surfaces"
        if self == SurfacesToIncludeFromMs2FileOption.SELECTEDENTITYLIST:
            return "Selected entity list"