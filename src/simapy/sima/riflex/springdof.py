# Generated with SpringDOF
# 
from enum import Enum
from enum import auto

class SpringDOF(Enum):
    """"""
    GLOBAL_X_DIRECTION = auto()
    GLOBAL_Y_DIRECTION = auto()
    GLOBAL_Z_DIRECTION = auto()
    ROTATION_AROUND_GLOBAL_X = auto()
    ROTATION_AROUND_GLOBAL_Y = auto()
    ROTATION_AROUND_GLOBAL_Z = auto()
    TRANSLATION_IN_GLOBAL_XY_PLANE = auto()
    TRANSLATION_IN_GLOBAL_XZ_PLANE = auto()
    TRANSLATION_IN_GLOBAL_YZ_PLANE = auto()

    def label(self):
        if self == SpringDOF.GLOBAL_X_DIRECTION:
            return "Global X-direction"
        if self == SpringDOF.GLOBAL_Y_DIRECTION:
            return "Global Y-direction"
        if self == SpringDOF.GLOBAL_Z_DIRECTION:
            return "Global Z-direction"
        if self == SpringDOF.ROTATION_AROUND_GLOBAL_X:
            return "Rotation around global X-axis"
        if self == SpringDOF.ROTATION_AROUND_GLOBAL_Y:
            return "Rotation around global Y-axis"
        if self == SpringDOF.ROTATION_AROUND_GLOBAL_Z:
            return "Rotation around global Z-axis"
        if self == SpringDOF.TRANSLATION_IN_GLOBAL_XY_PLANE:
            return "Translation in global XY-plane"
        if self == SpringDOF.TRANSLATION_IN_GLOBAL_XZ_PLANE:
            return "Translation in global XZ-plane"
        if self == SpringDOF.TRANSLATION_IN_GLOBAL_YZ_PLANE:
            return "Translation in global YZ-plane"