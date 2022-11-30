# This an autogenerated file
# 
# Generated with BallJointConnectorType
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.balljointconnectortype import BallJointConnectorTypeBlueprint
from typing import Dict
from sima.riflex.boundarycondition import BoundaryCondition
from sima.riflex.nodalcomponenttype import NodalComponentType
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.referenceframetype import ReferenceFrameType

class BallJointConnectorType(NodalComponentType):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    mass : float
         Mass(default 0.0)
    volume : float
         Displacement volume(default 0.0)
    referenceFrame : ReferenceFrameType
         Reference frame
    dragX : float
         Drag force coefficient in X-direction(default 0.0)
    dragY : float
         Drag force coefficient in Y-direction(default 0.0)
    dragZ : float
         Drag force coefficient in Z-direction(default 0.0)
    addedMassX : float
         Added mass in X-direction(default 0.0)
    addedMassY : float
         Added mass in Y-direction(default 0.0)
    addedMassZ : float
         Added mass in Z-direction(default 0.0)
    boundaryRotX : BoundaryCondition
         Rotation freedom code, x-axis.
    boundaryRotY : BoundaryCondition
         Rotation freedom code, y-axis.
    boundaryRotZ : BoundaryCondition
         Rotation freedom code, z-axis.
    """

    def __init__(self , description="", mass=0.0, volume=0.0, referenceFrame=ReferenceFrameType.LOCAL, dragX=0.0, dragY=0.0, dragZ=0.0, addedMassX=0.0, addedMassY=0.0, addedMassZ=0.0, boundaryRotX=BoundaryCondition.FREE, boundaryRotY=BoundaryCondition.FREE, boundaryRotZ=BoundaryCondition.FREE, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.mass = mass
        self.volume = volume
        self.referenceFrame = referenceFrame
        self.dragX = dragX
        self.dragY = dragY
        self.dragZ = dragZ
        self.addedMassX = addedMassX
        self.addedMassY = addedMassY
        self.addedMassZ = addedMassZ
        self.boundaryRotX = boundaryRotX
        self.boundaryRotY = boundaryRotY
        self.boundaryRotZ = boundaryRotZ
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BallJointConnectorTypeBlueprint()


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
    def mass(self) -> float:
        """Mass"""
        return self.__mass

    @mass.setter
    def mass(self, value: float):
        """Set mass"""
        self.__mass = float(value)

    @property
    def volume(self) -> float:
        """Displacement volume"""
        return self.__volume

    @volume.setter
    def volume(self, value: float):
        """Set volume"""
        self.__volume = float(value)

    @property
    def referenceFrame(self) -> ReferenceFrameType:
        """Reference frame"""
        return self.__referenceFrame

    @referenceFrame.setter
    def referenceFrame(self, value: ReferenceFrameType):
        """Set referenceFrame"""
        self.__referenceFrame = value

    @property
    def dragX(self) -> float:
        """Drag force coefficient in X-direction"""
        return self.__dragX

    @dragX.setter
    def dragX(self, value: float):
        """Set dragX"""
        self.__dragX = float(value)

    @property
    def dragY(self) -> float:
        """Drag force coefficient in Y-direction"""
        return self.__dragY

    @dragY.setter
    def dragY(self, value: float):
        """Set dragY"""
        self.__dragY = float(value)

    @property
    def dragZ(self) -> float:
        """Drag force coefficient in Z-direction"""
        return self.__dragZ

    @dragZ.setter
    def dragZ(self, value: float):
        """Set dragZ"""
        self.__dragZ = float(value)

    @property
    def addedMassX(self) -> float:
        """Added mass in X-direction"""
        return self.__addedMassX

    @addedMassX.setter
    def addedMassX(self, value: float):
        """Set addedMassX"""
        self.__addedMassX = float(value)

    @property
    def addedMassY(self) -> float:
        """Added mass in Y-direction"""
        return self.__addedMassY

    @addedMassY.setter
    def addedMassY(self, value: float):
        """Set addedMassY"""
        self.__addedMassY = float(value)

    @property
    def addedMassZ(self) -> float:
        """Added mass in Z-direction"""
        return self.__addedMassZ

    @addedMassZ.setter
    def addedMassZ(self, value: float):
        """Set addedMassZ"""
        self.__addedMassZ = float(value)

    @property
    def boundaryRotX(self) -> BoundaryCondition:
        """Rotation freedom code, x-axis."""
        return self.__boundaryRotX

    @boundaryRotX.setter
    def boundaryRotX(self, value: BoundaryCondition):
        """Set boundaryRotX"""
        self.__boundaryRotX = value

    @property
    def boundaryRotY(self) -> BoundaryCondition:
        """Rotation freedom code, y-axis."""
        return self.__boundaryRotY

    @boundaryRotY.setter
    def boundaryRotY(self, value: BoundaryCondition):
        """Set boundaryRotY"""
        self.__boundaryRotY = value

    @property
    def boundaryRotZ(self) -> BoundaryCondition:
        """Rotation freedom code, z-axis."""
        return self.__boundaryRotZ

    @boundaryRotZ.setter
    def boundaryRotZ(self, value: BoundaryCondition):
        """Set boundaryRotZ"""
        self.__boundaryRotZ = value
