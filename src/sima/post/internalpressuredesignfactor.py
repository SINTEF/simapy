# Generated with InternalPressureDesignFactor
# 
from enum import Enum
from enum import auto

class InternalPressureDesignFactor(Enum):
    """"""
    DESIGN_PRESSURE = auto()
    INCIDENTAL_PRESSURE = auto()
    PRODUCTION_CASING_WITH_TUBING_LEAK = auto()
    DRILLING_RISER_WITH_EXTREME_PRESSURE = auto()
    HYDROSTATIC_TEST = auto()

    def label(self):
        if self == InternalPressureDesignFactor.DESIGN_PRESSURE:
            return "Design pressure (0.60)"
        if self == InternalPressureDesignFactor.INCIDENTAL_PRESSURE:
            return "Incidental pressure (0.67)"
        if self == InternalPressureDesignFactor.PRODUCTION_CASING_WITH_TUBING_LEAK:
            return "Production casing with tubing leak (0.81)"
        if self == InternalPressureDesignFactor.DRILLING_RISER_WITH_EXTREME_PRESSURE:
            return "Drilling riser with extreme pressure (0.81)"
        if self == InternalPressureDesignFactor.HYDROSTATIC_TEST:
            return "Hydrostatic test (0.9)"