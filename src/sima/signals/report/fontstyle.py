# Generated with FontStyle
# 
from enum import Enum
from enum import auto

class FontStyle(Enum):
    """"""
    NORMAL = auto()
    BOLD = auto()
    ITALIC = auto()
    BOLD_ITALIC = auto()

    def label(self):
        if self == FontStyle.NORMAL:
            return "Normal"
        if self == FontStyle.BOLD:
            return "Bold"
        if self == FontStyle.ITALIC:
            return "Italic"
        if self == FontStyle.BOLD_ITALIC:
            return "Bold Italic"