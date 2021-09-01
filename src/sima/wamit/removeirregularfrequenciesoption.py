# Generated with RemoveIrregularFrequenciesOption
# 
from enum import Enum
from enum import auto

class RemoveIrregularFrequenciesOption(Enum):
    """"""
    NO = auto()
    USEGDF = auto()
    AUTOMATICDISCRETIZATION = auto()

    def label(self):
        if self == RemoveIrregularFrequenciesOption.NO:
            return "No"
        if self == RemoveIrregularFrequenciesOption.USEGDF:
            return "Use GDF"
        if self == RemoveIrregularFrequenciesOption.AUTOMATICDISCRETIZATION:
            return "Automatic Discretization"