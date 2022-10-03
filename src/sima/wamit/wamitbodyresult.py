# This an autogenerated file
# 
# Generated with WamitBodyResult
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wamitbodyresult import WamitBodyResultBlueprint
from typing import Dict
from sima.hydro.externalstiffnessmatrix import ExternalStiffnessMatrix
from sima.hydro.firstordermotiontransferfunction import FirstOrderMotionTransferFunction
from sima.hydro.hydrostaticstiffnessdata import HydrostaticStiffnessData
from sima.hydro.lineardampingmatrix import LinearDampingMatrix
from sima.hydro.radiationdatagroup import RadiationDataGroup
from sima.hydro.structuralmass import StructuralMass
from sima.sima.named import Named
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.wamit.wamitfirstorderwaveforcetransferfunction import WamitFirstOrderWaveForceTransferFunction
from sima.wamit.wamitwavedriftforce import WamitWaveDriftForce

class WamitBodyResult(Named):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    firstOrderMotionTransferFunction : FirstOrderMotionTransferFunction
    firstOrderWaveForceTransferFunctionDiffraction : WamitFirstOrderWaveForceTransferFunction
    firstOrderWaveForceTransferFunctionHaskind : WamitFirstOrderWaveForceTransferFunction
    characteristicLength : float
         Characteristic Length (ULEN)(default 0.0)
    x : float
         x position coordinate (default 0.0)
    y : float
         y position coordinate (default 0.0)
    z : float
         z position coordinate (default 0.0)
    rz : float
         rotation about z-axis(default 0.0)
    symmetryAboutX : bool
         (default False)
    symmetryAboutY : bool
         (default False)
    gravity : float
         (default 0.0)
    waterDensity : float
         (default 0.0)
    volumes : Point3
    centreOfGravity : Point3
    centreOfBuoyancy : Point3
    radiationData : RadiationDataGroup
    waveDriftForceMomentum : WamitWaveDriftForce
    waveDriftForceControlSurface : WamitWaveDriftForce
    waveDriftForcePressure : WamitWaveDriftForce
    waterDepth : float
         Depth at global origin(default 0.0)
    externalStiffness : ExternalStiffnessMatrix
    structuralMass : StructuralMass
    linearDamping : LinearDampingMatrix
    hydrostaticStiffness : HydrostaticStiffnessData
    """

    def __init__(self , _id="", name="", characteristicLength=0.0, x=0.0, y=0.0, z=0.0, rz=0.0, symmetryAboutX=False, symmetryAboutY=False, gravity=0.0, waterDensity=0.0, waterDepth=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.firstOrderMotionTransferFunction = None
        self.firstOrderWaveForceTransferFunctionDiffraction = None
        self.firstOrderWaveForceTransferFunctionHaskind = None
        self.characteristicLength = characteristicLength
        self.x = x
        self.y = y
        self.z = z
        self.rz = rz
        self.symmetryAboutX = symmetryAboutX
        self.symmetryAboutY = symmetryAboutY
        self.gravity = gravity
        self.waterDensity = waterDensity
        self.volumes = None
        self.centreOfGravity = None
        self.centreOfBuoyancy = None
        self.radiationData = None
        self.waveDriftForceMomentum = None
        self.waveDriftForceControlSurface = None
        self.waveDriftForcePressure = None
        self.waterDepth = waterDepth
        self.externalStiffness = None
        self.structuralMass = None
        self.linearDamping = None
        self.hydrostaticStiffness = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WamitBodyResultBlueprint()


    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

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
        self.__name = str(value)

    @property
    def firstOrderMotionTransferFunction(self) -> FirstOrderMotionTransferFunction:
        """"""
        return self.__firstOrderMotionTransferFunction

    @firstOrderMotionTransferFunction.setter
    def firstOrderMotionTransferFunction(self, value: FirstOrderMotionTransferFunction):
        """Set firstOrderMotionTransferFunction"""
        self.__firstOrderMotionTransferFunction = value

    @property
    def firstOrderWaveForceTransferFunctionDiffraction(self) -> WamitFirstOrderWaveForceTransferFunction:
        """"""
        return self.__firstOrderWaveForceTransferFunctionDiffraction

    @firstOrderWaveForceTransferFunctionDiffraction.setter
    def firstOrderWaveForceTransferFunctionDiffraction(self, value: WamitFirstOrderWaveForceTransferFunction):
        """Set firstOrderWaveForceTransferFunctionDiffraction"""
        self.__firstOrderWaveForceTransferFunctionDiffraction = value

    @property
    def firstOrderWaveForceTransferFunctionHaskind(self) -> WamitFirstOrderWaveForceTransferFunction:
        """"""
        return self.__firstOrderWaveForceTransferFunctionHaskind

    @firstOrderWaveForceTransferFunctionHaskind.setter
    def firstOrderWaveForceTransferFunctionHaskind(self, value: WamitFirstOrderWaveForceTransferFunction):
        """Set firstOrderWaveForceTransferFunctionHaskind"""
        self.__firstOrderWaveForceTransferFunctionHaskind = value

    @property
    def characteristicLength(self) -> float:
        """Characteristic Length (ULEN)"""
        return self.__characteristicLength

    @characteristicLength.setter
    def characteristicLength(self, value: float):
        """Set characteristicLength"""
        self.__characteristicLength = float(value)

    @property
    def x(self) -> float:
        """x position coordinate """
        return self.__x

    @x.setter
    def x(self, value: float):
        """Set x"""
        self.__x = float(value)

    @property
    def y(self) -> float:
        """y position coordinate """
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set y"""
        self.__y = float(value)

    @property
    def z(self) -> float:
        """z position coordinate """
        return self.__z

    @z.setter
    def z(self, value: float):
        """Set z"""
        self.__z = float(value)

    @property
    def rz(self) -> float:
        """rotation about z-axis"""
        return self.__rz

    @rz.setter
    def rz(self, value: float):
        """Set rz"""
        self.__rz = float(value)

    @property
    def symmetryAboutX(self) -> bool:
        """"""
        return self.__symmetryAboutX

    @symmetryAboutX.setter
    def symmetryAboutX(self, value: bool):
        """Set symmetryAboutX"""
        self.__symmetryAboutX = bool(value)

    @property
    def symmetryAboutY(self) -> bool:
        """"""
        return self.__symmetryAboutY

    @symmetryAboutY.setter
    def symmetryAboutY(self, value: bool):
        """Set symmetryAboutY"""
        self.__symmetryAboutY = bool(value)

    @property
    def gravity(self) -> float:
        """"""
        return self.__gravity

    @gravity.setter
    def gravity(self, value: float):
        """Set gravity"""
        self.__gravity = float(value)

    @property
    def waterDensity(self) -> float:
        """"""
        return self.__waterDensity

    @waterDensity.setter
    def waterDensity(self, value: float):
        """Set waterDensity"""
        self.__waterDensity = float(value)

    @property
    def volumes(self) -> Point3:
        """"""
        return self.__volumes

    @volumes.setter
    def volumes(self, value: Point3):
        """Set volumes"""
        self.__volumes = value

    @property
    def centreOfGravity(self) -> Point3:
        """"""
        return self.__centreOfGravity

    @centreOfGravity.setter
    def centreOfGravity(self, value: Point3):
        """Set centreOfGravity"""
        self.__centreOfGravity = value

    @property
    def centreOfBuoyancy(self) -> Point3:
        """"""
        return self.__centreOfBuoyancy

    @centreOfBuoyancy.setter
    def centreOfBuoyancy(self, value: Point3):
        """Set centreOfBuoyancy"""
        self.__centreOfBuoyancy = value

    @property
    def radiationData(self) -> RadiationDataGroup:
        """"""
        return self.__radiationData

    @radiationData.setter
    def radiationData(self, value: RadiationDataGroup):
        """Set radiationData"""
        self.__radiationData = value

    @property
    def waveDriftForceMomentum(self) -> WamitWaveDriftForce:
        """"""
        return self.__waveDriftForceMomentum

    @waveDriftForceMomentum.setter
    def waveDriftForceMomentum(self, value: WamitWaveDriftForce):
        """Set waveDriftForceMomentum"""
        self.__waveDriftForceMomentum = value

    @property
    def waveDriftForceControlSurface(self) -> WamitWaveDriftForce:
        """"""
        return self.__waveDriftForceControlSurface

    @waveDriftForceControlSurface.setter
    def waveDriftForceControlSurface(self, value: WamitWaveDriftForce):
        """Set waveDriftForceControlSurface"""
        self.__waveDriftForceControlSurface = value

    @property
    def waveDriftForcePressure(self) -> WamitWaveDriftForce:
        """"""
        return self.__waveDriftForcePressure

    @waveDriftForcePressure.setter
    def waveDriftForcePressure(self, value: WamitWaveDriftForce):
        """Set waveDriftForcePressure"""
        self.__waveDriftForcePressure = value

    @property
    def waterDepth(self) -> float:
        """Depth at global origin"""
        return self.__waterDepth

    @waterDepth.setter
    def waterDepth(self, value: float):
        """Set waterDepth"""
        self.__waterDepth = float(value)

    @property
    def externalStiffness(self) -> ExternalStiffnessMatrix:
        """"""
        return self.__externalStiffness

    @externalStiffness.setter
    def externalStiffness(self, value: ExternalStiffnessMatrix):
        """Set externalStiffness"""
        self.__externalStiffness = value

    @property
    def structuralMass(self) -> StructuralMass:
        """"""
        return self.__structuralMass

    @structuralMass.setter
    def structuralMass(self, value: StructuralMass):
        """Set structuralMass"""
        self.__structuralMass = value

    @property
    def linearDamping(self) -> LinearDampingMatrix:
        """"""
        return self.__linearDamping

    @linearDamping.setter
    def linearDamping(self, value: LinearDampingMatrix):
        """Set linearDamping"""
        self.__linearDamping = value

    @property
    def hydrostaticStiffness(self) -> HydrostaticStiffnessData:
        """"""
        return self.__hydrostaticStiffness

    @hydrostaticStiffness.setter
    def hydrostaticStiffness(self, value: HydrostaticStiffnessData):
        """Set hydrostaticStiffness"""
        self.__hydrostaticStiffness = value
