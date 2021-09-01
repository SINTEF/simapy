# Generated with GeomRepresentationType
# 
from enum import Enum
from enum import auto

class GeomRepresentationType(Enum):
    """"""
    DEFAULT_BOX = auto()
    FILE = auto()
    BOX = auto()
    SPHERE = auto()
    CYLINDER_X = auto()
    CYLINDER_Y = auto()
    CYLINDER_Z = auto()
    NONE = auto()

    def label(self):
        if self == GeomRepresentationType.DEFAULT_BOX:
            return "Default arrow box"
        if self == GeomRepresentationType.FILE:
            return "Geometry file"
        if self == GeomRepresentationType.BOX:
            return "Box"
        if self == GeomRepresentationType.SPHERE:
            return "Sphere"
        if self == GeomRepresentationType.CYLINDER_X:
            return "Cylinder X"
        if self == GeomRepresentationType.CYLINDER_Y:
            return "Cylinder Y"
        if self == GeomRepresentationType.CYLINDER_Z:
            return "Cylinder Z"
        if self == GeomRepresentationType.NONE:
            return "No graphical representation"