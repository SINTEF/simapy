# Generated with MotionSequenceType
# 
from enum import Enum
from enum import auto

class MotionSequenceType(Enum):
    """"""
    TSTOP = auto()
    DELTAPOS = auto()
    VSEQ = auto()

    def label(self):
        if self == MotionSequenceType.TSTOP:
            return "Compute stop time"
        if self == MotionSequenceType.DELTAPOS:
            return "Compute change in position during sequence"
        if self == MotionSequenceType.VSEQ:
            return "Compute sequence travelling speed"