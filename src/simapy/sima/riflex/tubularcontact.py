# This an autogenerated file
# 
# Generated with TubularContact
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.tubularcontact import TubularContactBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import ScriptableValue
from .contactdirection import ContactDirection
from .controlparameter import ControlParameter
from .springstiffnessitem import SpringStiffnessItem

class TubularContact(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    radius : float
         Contact radius(default 0.0)
    direction : ContactDirection
         Contact direction.
    constantStiffness : bool
         Stiffness code for contact force.(default False)
    desiredDamping : float
         Desired relative damping level at estimated eigen period in the pipe and contact spring system.(default 0.0)
    dampingCoefficient : float
         Dash pot damping coefficient(default 0.0)
    stiffness : float
         Spring stiffness associated with static friction coefficient(default 0.0)
    staticFriction : float
         Static friction coefficient.(default 0.0)
    dynamicFriction : float
         Dynamic (sliding) friction coefficient.(default 0.0)
    slidingFriction : ControlParameter
         Control parameter for axial sliding friction.
    rotationFriction : ControlParameter
         Control parameter for friction caused by rotation.
    velocityLimit : float
         Velocity limit to change from sliding status (dynamic friction) to static displacement status (static friction)(default 0.0)
    compressionStiffness : float
         Spring compression stiffness(default 0.0)
    stiffnessItems : List[SpringStiffnessItem]
    """

    def __init__(self , description="", radius=0.0, direction=ContactDirection.INWARDS, constantStiffness=False, desiredDamping=0.0, dampingCoefficient=0.0, stiffness=0.0, staticFriction=0.0, dynamicFriction=0.0, slidingFriction=ControlParameter.ON, rotationFriction=ControlParameter.ON, velocityLimit=0.0, compressionStiffness=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.radius = radius
        self.direction = direction
        self.constantStiffness = constantStiffness
        self.desiredDamping = desiredDamping
        self.dampingCoefficient = dampingCoefficient
        self.stiffness = stiffness
        self.staticFriction = staticFriction
        self.dynamicFriction = dynamicFriction
        self.slidingFriction = slidingFriction
        self.rotationFriction = rotationFriction
        self.velocityLimit = velocityLimit
        self.compressionStiffness = compressionStiffness
        self.stiffnessItems = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TubularContactBlueprint()


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
    def radius(self) -> float:
        """Contact radius"""
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        """Set radius"""
        self.__radius = float(value)

    @property
    def direction(self) -> ContactDirection:
        """Contact direction."""
        return self.__direction

    @direction.setter
    def direction(self, value: ContactDirection):
        """Set direction"""
        self.__direction = value

    @property
    def constantStiffness(self) -> bool:
        """Stiffness code for contact force."""
        return self.__constantStiffness

    @constantStiffness.setter
    def constantStiffness(self, value: bool):
        """Set constantStiffness"""
        self.__constantStiffness = bool(value)

    @property
    def desiredDamping(self) -> float:
        """Desired relative damping level at estimated eigen period in the pipe and contact spring system."""
        return self.__desiredDamping

    @desiredDamping.setter
    def desiredDamping(self, value: float):
        """Set desiredDamping"""
        self.__desiredDamping = float(value)

    @property
    def dampingCoefficient(self) -> float:
        """Dash pot damping coefficient"""
        return self.__dampingCoefficient

    @dampingCoefficient.setter
    def dampingCoefficient(self, value: float):
        """Set dampingCoefficient"""
        self.__dampingCoefficient = float(value)

    @property
    def stiffness(self) -> float:
        """Spring stiffness associated with static friction coefficient"""
        return self.__stiffness

    @stiffness.setter
    def stiffness(self, value: float):
        """Set stiffness"""
        self.__stiffness = float(value)

    @property
    def staticFriction(self) -> float:
        """Static friction coefficient."""
        return self.__staticFriction

    @staticFriction.setter
    def staticFriction(self, value: float):
        """Set staticFriction"""
        self.__staticFriction = float(value)

    @property
    def dynamicFriction(self) -> float:
        """Dynamic (sliding) friction coefficient."""
        return self.__dynamicFriction

    @dynamicFriction.setter
    def dynamicFriction(self, value: float):
        """Set dynamicFriction"""
        self.__dynamicFriction = float(value)

    @property
    def slidingFriction(self) -> ControlParameter:
        """Control parameter for axial sliding friction."""
        return self.__slidingFriction

    @slidingFriction.setter
    def slidingFriction(self, value: ControlParameter):
        """Set slidingFriction"""
        self.__slidingFriction = value

    @property
    def rotationFriction(self) -> ControlParameter:
        """Control parameter for friction caused by rotation."""
        return self.__rotationFriction

    @rotationFriction.setter
    def rotationFriction(self, value: ControlParameter):
        """Set rotationFriction"""
        self.__rotationFriction = value

    @property
    def velocityLimit(self) -> float:
        """Velocity limit to change from sliding status (dynamic friction) to static displacement status (static friction)"""
        return self.__velocityLimit

    @velocityLimit.setter
    def velocityLimit(self, value: float):
        """Set velocityLimit"""
        self.__velocityLimit = float(value)

    @property
    def compressionStiffness(self) -> float:
        """Spring compression stiffness"""
        return self.__compressionStiffness

    @compressionStiffness.setter
    def compressionStiffness(self, value: float):
        """Set compressionStiffness"""
        self.__compressionStiffness = float(value)

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
