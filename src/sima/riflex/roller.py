# This an autogenerated file
# 
# Generated with Roller
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.roller import RollerBlueprint
from typing import Dict
from .springstiffnessitem import SpringStiffnessItem
from sima.sima import NamedObject
from sima.sima import ScriptableValue

class Roller(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    direction : float
         Direction of roller axis (Clockwise around the local X-axis of the actual surface plane).(default 0.0)
    y : float
         Y-coordinate of roller origin(default 0.0)
    z : float
         Z-coordinate of roller origin(default 0.0)
    length : float
         Length of roller (0 means infinite length)(default 0.0)
    constantStiffness : bool
         Constant spring compression stiffness.(default False)
    damping : float
         Dash pot damping coefficient(default 0.0)
    stiffness : float
         Spring compression stiffness(default 0.0)
    radius : float
         Radius of roller(default 0.0)
    stiffnessItems : List[SpringStiffnessItem]
    """

    def __init__(self , description="", direction=0.0, y=0.0, z=0.0, length=0.0, constantStiffness=False, damping=0.0, stiffness=0.0, radius=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.direction = direction
        self.y = y
        self.z = z
        self.length = length
        self.constantStiffness = constantStiffness
        self.damping = damping
        self.stiffness = stiffness
        self.radius = radius
        self.stiffnessItems = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RollerBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def direction(self) -> float:
        """Direction of roller axis (Clockwise around the local X-axis of the actual surface plane)."""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def y(self) -> float:
        """Y-coordinate of roller origin"""
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set y"""
        self.__y = float(value)

    @property
    def z(self) -> float:
        """Z-coordinate of roller origin"""
        return self.__z

    @z.setter
    def z(self, value: float):
        """Set z"""
        self.__z = float(value)

    @property
    def length(self) -> float:
        """Length of roller (0 means infinite length)"""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def constantStiffness(self) -> bool:
        """Constant spring compression stiffness."""
        return self.__constantStiffness

    @constantStiffness.setter
    def constantStiffness(self, value: bool):
        """Set constantStiffness"""
        self.__constantStiffness = bool(value)

    @property
    def damping(self) -> float:
        """Dash pot damping coefficient"""
        return self.__damping

    @damping.setter
    def damping(self, value: float):
        """Set damping"""
        self.__damping = float(value)

    @property
    def stiffness(self) -> float:
        """Spring compression stiffness"""
        return self.__stiffness

    @stiffness.setter
    def stiffness(self, value: float):
        """Set stiffness"""
        self.__stiffness = float(value)

    @property
    def radius(self) -> float:
        """Radius of roller"""
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        """Set radius"""
        self.__radius = float(value)

    @property
    def stiffnessItems(self) -> List[SpringStiffnessItem]:
        """"""
        return self.__stiffnessItems

    @stiffnessItems.setter
    def stiffnessItems(self, value: List[SpringStiffnessItem]):
        """Set stiffnessItems"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__stiffnessItems = value
