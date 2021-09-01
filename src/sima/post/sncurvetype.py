# Generated with SNCurveType
# 
from enum import Enum
from enum import auto

class SNCurveType(Enum):
    """"""
    DNV_B1 = auto()
    DNV_B1_AIR = auto()
    DNV_B2 = auto()
    DNV_B2_AIR = auto()
    DNV_C = auto()
    DNV_C_AIR = auto()
    DNV_C1 = auto()
    DNV_C1_AIR = auto()
    DNV_C2 = auto()
    DNV_C2_AIR = auto()
    DNV_D = auto()
    DNV_D_AIR = auto()
    DNV_E = auto()
    DNV_E_AIR = auto()
    DNV_F = auto()
    DNV_F_AIR = auto()
    DNV_F1 = auto()
    DNV_F1_AIR = auto()
    DNV_F3 = auto()
    DNV_F3_AIR = auto()
    DNV_G = auto()
    DNV_G_AIR = auto()
    DNV_W1 = auto()
    DNV_W1_AIR = auto()
    DNV_W2 = auto()
    DNV_W2_AIR = auto()
    DNV_W3 = auto()
    DNV_W3_AIR = auto()
    DNV_STUD_CHAIN = auto()
    DNV_STUDLESS_CHAIN = auto()
    DNV_STRANDED_ROPE = auto()
    DNV_SPIRAL_ROPE = auto()
    DNV_HS = auto()

    def label(self):
        if self == SNCurveType.DNV_B1:
            return "DNV B1 seawater cathodic protection"
        if self == SNCurveType.DNV_B1_AIR:
            return "DNV B1 air"
        if self == SNCurveType.DNV_B2:
            return "DNV B2 seawater cathodic protection"
        if self == SNCurveType.DNV_B2_AIR:
            return "DNV B2 air"
        if self == SNCurveType.DNV_C:
            return "DNV C seawater cathodic protection"
        if self == SNCurveType.DNV_C_AIR:
            return "DNV C air"
        if self == SNCurveType.DNV_C1:
            return "DNV C1 seawater cathodic protection"
        if self == SNCurveType.DNV_C1_AIR:
            return "DNV C1 air"
        if self == SNCurveType.DNV_C2:
            return "DNV C2 seawater cathodic protection"
        if self == SNCurveType.DNV_C2_AIR:
            return "DNV C2 air"
        if self == SNCurveType.DNV_D:
            return "DNV D seawater cathodic protection"
        if self == SNCurveType.DNV_D_AIR:
            return "DNV D air"
        if self == SNCurveType.DNV_E:
            return "DNV E seawater cathodic protection"
        if self == SNCurveType.DNV_E_AIR:
            return "DNV E air"
        if self == SNCurveType.DNV_F:
            return "DNV F seawater cathodic protection"
        if self == SNCurveType.DNV_F_AIR:
            return "DNV F air"
        if self == SNCurveType.DNV_F1:
            return "DNV F1 seawater cathodic protection"
        if self == SNCurveType.DNV_F1_AIR:
            return "DNV F1 air"
        if self == SNCurveType.DNV_F3:
            return "DNV F3 seawater cathodic protection"
        if self == SNCurveType.DNV_F3_AIR:
            return "DNV F3 air"
        if self == SNCurveType.DNV_G:
            return "DNV G seawater cathodic protection"
        if self == SNCurveType.DNV_G_AIR:
            return "DNV G air"
        if self == SNCurveType.DNV_W1:
            return "DNV W1 seawater cathodic protection"
        if self == SNCurveType.DNV_W1_AIR:
            return "DNV W1 air"
        if self == SNCurveType.DNV_W2:
            return "DNV W2 seawater cathodic protection"
        if self == SNCurveType.DNV_W2_AIR:
            return "DNV W2 air"
        if self == SNCurveType.DNV_W3:
            return "DNV W3 seawater cathodic protection"
        if self == SNCurveType.DNV_W3_AIR:
            return "DNV W3 air"
        if self == SNCurveType.DNV_STUD_CHAIN:
            return "DNV Stud chain"
        if self == SNCurveType.DNV_STUDLESS_CHAIN:
            return "DNV Studless chain"
        if self == SNCurveType.DNV_STRANDED_ROPE:
            return "DNV Stranded rope"
        if self == SNCurveType.DNV_SPIRAL_ROPE:
            return "DNV Spiral rope"
        if self == SNCurveType.DNV_HS:
            return "DNV High strength steel"