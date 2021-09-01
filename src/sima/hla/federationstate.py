# Generated with FederationState
# 
from enum import Enum
from enum import auto

class FederationState(Enum):
    """"""
    IDLE = auto()
    STARTING = auto()
    RUNNING = auto()
    PAUSED = auto()
    STOPPING = auto()
    ERROR = auto()

    def label(self):
        if self == FederationState.IDLE:
            return "Idle"
        if self == FederationState.STARTING:
            return "Starting"
        if self == FederationState.RUNNING:
            return "Running"
        if self == FederationState.PAUSED:
            return "Paused"
        if self == FederationState.STOPPING:
            return "Stopping"
        if self == FederationState.ERROR:
            return "Error"