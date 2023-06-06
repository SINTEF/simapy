# Generated with ControllerType
# 
from enum import Enum
from enum import auto

class ControllerType(Enum):
    """"""
    JAR_FILE_CONTROLLER = auto()
    BLADED_CONTROLLER = auto()

    def label(self):
        if self == ControllerType.JAR_FILE_CONTROLLER:
            return "Java based controller"
        if self == ControllerType.BLADED_CONTROLLER:
            return "Bladed style controller"