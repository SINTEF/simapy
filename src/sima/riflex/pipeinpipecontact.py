# This an autogenerated file
# 
# Generated with PipeInPipeContact
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.pipeinpipecontact import PipeInPipeContactBlueprint
from typing import Dict
from sima.riflex.contactspringstiffnessitem import ContactSpringStiffnessItem
from sima.riflex.innerouter import InnerOuter
from sima.riflex.innerpipeloading import InnerPipeLoading
from sima.riflex.stiffnesstype import StiffnessType
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine
    from sima.riflex.mainriserline import MainRiserLine

class PipeInPipeContact(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    masterLine : ARLine
         Identification of master pipe.
    slaveLine : ARLine
         Identification of slave pipe.
    firstMasterSegment : int
         First local segment in line for master pipe.(default 0)
    lastMasterSegment : int
         Last local segment in line for master pipe.(default 0)
    firstSlaveSegment : int
         First local segment in line for slave pipe.(default 0)
    lastSlaveSegment : int
         Last local segment in line for slave pipe.(default 0)
    masterPipePosition : InnerOuter
         Position of master pipe.
    stiffnessType : StiffnessType
         Stiffness code for contact force.
    relativeDamping : float
         Desired relative damping level at estimated eigen period in the\npipe, pipe and contact spring system.(default 0.0)
    damping : float
         Dash pot damping coefficient per unit length of master pipe(default 0.0)
    frictionStiffness : float
         Spring stiffness associated with static friction coefficient(default 0.0)
    staticFriction : float
         Static friction coefficient.(default 0.0)
    dynamicFriction : float
         Dynamic (sliding) friction coefficient.(default 0.0)
    axialFrictionEnabled : bool
         Axial (sliding) friction enabled.(default False)
    rotationalFrictionEnabled : bool
         Rotational (sliding) friction enabled.(default False)
    velocityLimitFriction : float
         Velocity limit to change from sliding status (dynamic friction) to static\ndisplacement status (static friction)(default 0.0)
    linearStiffness : float
         Spring compression stiffness per unit length(default 0.0)
    stiffnessCharacteristics : List[ContactSpringStiffnessItem]
    masterAsMainRiser : bool
         (default False)
    slaveAsMainRiser : bool
         (default False)
    masterMainRiser : MainRiserLine
         Identification of master main riser
    slaveMainRiser : MainRiserLine
         Identification of slave main riser
    innerPipeLoading : InnerPipeLoading
    """

    def __init__(self , description="", firstMasterSegment=0, lastMasterSegment=0, firstSlaveSegment=0, lastSlaveSegment=0, masterPipePosition=InnerOuter.INNER, stiffnessType=StiffnessType.LINEAR, relativeDamping=0.0, damping=0.0, frictionStiffness=0.0, staticFriction=0.0, dynamicFriction=0.0, axialFrictionEnabled=False, rotationalFrictionEnabled=False, velocityLimitFriction=0.0, linearStiffness=0.0, masterAsMainRiser=False, slaveAsMainRiser=False, innerPipeLoading=InnerPipeLoading.EXPOSED, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.masterLine = None
        self.slaveLine = None
        self.firstMasterSegment = firstMasterSegment
        self.lastMasterSegment = lastMasterSegment
        self.firstSlaveSegment = firstSlaveSegment
        self.lastSlaveSegment = lastSlaveSegment
        self.masterPipePosition = masterPipePosition
        self.stiffnessType = stiffnessType
        self.relativeDamping = relativeDamping
        self.damping = damping
        self.frictionStiffness = frictionStiffness
        self.staticFriction = staticFriction
        self.dynamicFriction = dynamicFriction
        self.axialFrictionEnabled = axialFrictionEnabled
        self.rotationalFrictionEnabled = rotationalFrictionEnabled
        self.velocityLimitFriction = velocityLimitFriction
        self.linearStiffness = linearStiffness
        self.stiffnessCharacteristics = list()
        self.masterAsMainRiser = masterAsMainRiser
        self.slaveAsMainRiser = slaveAsMainRiser
        self.masterMainRiser = None
        self.slaveMainRiser = None
        self.innerPipeLoading = innerPipeLoading
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PipeInPipeContactBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
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
    def masterLine(self) -> ARLine:
        """Identification of master pipe."""
        return self.__masterLine

    @masterLine.setter
    def masterLine(self, value: ARLine):
        """Set masterLine"""
        self.__masterLine = value

    @property
    def slaveLine(self) -> ARLine:
        """Identification of slave pipe."""
        return self.__slaveLine

    @slaveLine.setter
    def slaveLine(self, value: ARLine):
        """Set slaveLine"""
        self.__slaveLine = value

    @property
    def firstMasterSegment(self) -> int:
        """First local segment in line for master pipe."""
        return self.__firstMasterSegment

    @firstMasterSegment.setter
    def firstMasterSegment(self, value: int):
        """Set firstMasterSegment"""
        self.__firstMasterSegment = int(value)

    @property
    def lastMasterSegment(self) -> int:
        """Last local segment in line for master pipe."""
        return self.__lastMasterSegment

    @lastMasterSegment.setter
    def lastMasterSegment(self, value: int):
        """Set lastMasterSegment"""
        self.__lastMasterSegment = int(value)

    @property
    def firstSlaveSegment(self) -> int:
        """First local segment in line for slave pipe."""
        return self.__firstSlaveSegment

    @firstSlaveSegment.setter
    def firstSlaveSegment(self, value: int):
        """Set firstSlaveSegment"""
        self.__firstSlaveSegment = int(value)

    @property
    def lastSlaveSegment(self) -> int:
        """Last local segment in line for slave pipe."""
        return self.__lastSlaveSegment

    @lastSlaveSegment.setter
    def lastSlaveSegment(self, value: int):
        """Set lastSlaveSegment"""
        self.__lastSlaveSegment = int(value)

    @property
    def masterPipePosition(self) -> InnerOuter:
        """Position of master pipe."""
        return self.__masterPipePosition

    @masterPipePosition.setter
    def masterPipePosition(self, value: InnerOuter):
        """Set masterPipePosition"""
        self.__masterPipePosition = value

    @property
    def stiffnessType(self) -> StiffnessType:
        """Stiffness code for contact force."""
        return self.__stiffnessType

    @stiffnessType.setter
    def stiffnessType(self, value: StiffnessType):
        """Set stiffnessType"""
        self.__stiffnessType = value

    @property
    def relativeDamping(self) -> float:
        """Desired relative damping level at estimated eigen period in the
pipe, pipe and contact spring system."""
        return self.__relativeDamping

    @relativeDamping.setter
    def relativeDamping(self, value: float):
        """Set relativeDamping"""
        self.__relativeDamping = float(value)

    @property
    def damping(self) -> float:
        """Dash pot damping coefficient per unit length of master pipe"""
        return self.__damping

    @damping.setter
    def damping(self, value: float):
        """Set damping"""
        self.__damping = float(value)

    @property
    def frictionStiffness(self) -> float:
        """Spring stiffness associated with static friction coefficient"""
        return self.__frictionStiffness

    @frictionStiffness.setter
    def frictionStiffness(self, value: float):
        """Set frictionStiffness"""
        self.__frictionStiffness = float(value)

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
    def axialFrictionEnabled(self) -> bool:
        """Axial (sliding) friction enabled."""
        return self.__axialFrictionEnabled

    @axialFrictionEnabled.setter
    def axialFrictionEnabled(self, value: bool):
        """Set axialFrictionEnabled"""
        self.__axialFrictionEnabled = bool(value)

    @property
    def rotationalFrictionEnabled(self) -> bool:
        """Rotational (sliding) friction enabled."""
        return self.__rotationalFrictionEnabled

    @rotationalFrictionEnabled.setter
    def rotationalFrictionEnabled(self, value: bool):
        """Set rotationalFrictionEnabled"""
        self.__rotationalFrictionEnabled = bool(value)

    @property
    def velocityLimitFriction(self) -> float:
        """Velocity limit to change from sliding status (dynamic friction) to static
displacement status (static friction)"""
        return self.__velocityLimitFriction

    @velocityLimitFriction.setter
    def velocityLimitFriction(self, value: float):
        """Set velocityLimitFriction"""
        self.__velocityLimitFriction = float(value)

    @property
    def linearStiffness(self) -> float:
        """Spring compression stiffness per unit length"""
        return self.__linearStiffness

    @linearStiffness.setter
    def linearStiffness(self, value: float):
        """Set linearStiffness"""
        self.__linearStiffness = float(value)

    @property
    def stiffnessCharacteristics(self) -> List[ContactSpringStiffnessItem]:
        """"""
        return self.__stiffnessCharacteristics

    @stiffnessCharacteristics.setter
    def stiffnessCharacteristics(self, value: List[ContactSpringStiffnessItem]):
        """Set stiffnessCharacteristics"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__stiffnessCharacteristics = value

    @property
    def masterAsMainRiser(self) -> bool:
        """"""
        return self.__masterAsMainRiser

    @masterAsMainRiser.setter
    def masterAsMainRiser(self, value: bool):
        """Set masterAsMainRiser"""
        self.__masterAsMainRiser = bool(value)

    @property
    def slaveAsMainRiser(self) -> bool:
        """"""
        return self.__slaveAsMainRiser

    @slaveAsMainRiser.setter
    def slaveAsMainRiser(self, value: bool):
        """Set slaveAsMainRiser"""
        self.__slaveAsMainRiser = bool(value)

    @property
    def masterMainRiser(self) -> MainRiserLine:
        """Identification of master main riser"""
        return self.__masterMainRiser

    @masterMainRiser.setter
    def masterMainRiser(self, value: MainRiserLine):
        """Set masterMainRiser"""
        self.__masterMainRiser = value

    @property
    def slaveMainRiser(self) -> MainRiserLine:
        """Identification of slave main riser"""
        return self.__slaveMainRiser

    @slaveMainRiser.setter
    def slaveMainRiser(self, value: MainRiserLine):
        """Set slaveMainRiser"""
        self.__slaveMainRiser = value

    @property
    def innerPipeLoading(self) -> InnerPipeLoading:
        """"""
        return self.__innerPipeLoading

    @innerPipeLoading.setter
    def innerPipeLoading(self, value: InnerPipeLoading):
        """Set innerPipeLoading"""
        self.__innerPipeLoading = value
