# This an autogenerated file
# 
# Generated with FixedBodyElement
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fixedbodyelement import FixedBodyElementBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.depthdependenthydrodynamiccoefficient import DepthDependenthydrodynamicCoefficient
from sima.simo.fixedbodywaveparticlemethod import FixedBodyWaveParticleMethod
from sima.simo.loadtype import LoadType
from sima.simo.waveintegrationmethod import WaveIntegrationMethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.hydro.diffractedwave import DiffractedWave

class FixedBodyElement(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    volume : float
         Volume of element(default 0.0)
    mass : float
         Mass of element(default 0.0)
    waveIntegrationMethod : WaveIntegrationMethod
         Parameter defining wave force integration method
    loadType : LoadType
         Include gravity and buoyancy forces?
    waveParticleMethod : FixedBodyWaveParticleMethod
         Include wave particle velocity and acceleration?
    position : Point3
    refPointXAxis : Point3
    refPointXYPlane : Point3
    zcoef : float
         Vertical position used as reference for depth dependency(default 0.0)
    depthDependentHydrodynamicCoefficients : List[DepthDependenthydrodynamicCoefficient]
    diffractedWave : DiffractedWave
    c2x : float
         Quadratic drag x(default 0.0)
    c2y : float
         Quadratic drag y(default 0.0)
    c2z : float
         Quadratic drag z(default 0.0)
    c1x : float
         Linear drag x(default 0.0)
    c1y : float
         Linear drag y(default 0.0)
    c1z : float
         Linear drag z(default 0.0)
    amx : float
         Added mass x(default 0.0)
    amy : float
         Added mass y(default 0.0)
    amz : float
         Added mass z(default 0.0)
    """

    def __init__(self , description="", _id=None, name=None, volume=0.0, mass=0.0, waveIntegrationMethod=WaveIntegrationMethod.ACTUAL_WAVE_ELEVATION, loadType=LoadType.GRAVITY_AND_BUOYANCY_INCLUDED, waveParticleMethod=FixedBodyWaveParticleMethod.VELOCITY_AND_ACCELERATION, zcoef=0.0, c2x=0.0, c2y=0.0, c2z=0.0, c1x=0.0, c1y=0.0, c1z=0.0, amx=0.0, amy=0.0, amz=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.volume = volume
        self.mass = mass
        self.waveIntegrationMethod = waveIntegrationMethod
        self.loadType = loadType
        self.waveParticleMethod = waveParticleMethod
        self.position = None
        self.refPointXAxis = None
        self.refPointXYPlane = None
        self.zcoef = zcoef
        self.depthDependentHydrodynamicCoefficients = list()
        self.diffractedWave = None
        self.c2x = c2x
        self.c2y = c2y
        self.c2z = c2z
        self.c1x = c1x
        self.c1y = c1y
        self.c1z = c1z
        self.amx = amx
        self.amy = amy
        self.amz = amz
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FixedBodyElementBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

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
    def volume(self) -> float:
        """Volume of element"""
        return self.__volume

    @volume.setter
    def volume(self, value: float):
        """Set volume"""
        self.__volume = float(value)

    @property
    def mass(self) -> float:
        """Mass of element"""
        return self.__mass

    @mass.setter
    def mass(self, value: float):
        """Set mass"""
        self.__mass = float(value)

    @property
    def waveIntegrationMethod(self) -> WaveIntegrationMethod:
        """Parameter defining wave force integration method"""
        return self.__waveIntegrationMethod

    @waveIntegrationMethod.setter
    def waveIntegrationMethod(self, value: WaveIntegrationMethod):
        """Set waveIntegrationMethod"""
        self.__waveIntegrationMethod = value

    @property
    def loadType(self) -> LoadType:
        """Include gravity and buoyancy forces?"""
        return self.__loadType

    @loadType.setter
    def loadType(self, value: LoadType):
        """Set loadType"""
        self.__loadType = value

    @property
    def waveParticleMethod(self) -> FixedBodyWaveParticleMethod:
        """Include wave particle velocity and acceleration?"""
        return self.__waveParticleMethod

    @waveParticleMethod.setter
    def waveParticleMethod(self, value: FixedBodyWaveParticleMethod):
        """Set waveParticleMethod"""
        self.__waveParticleMethod = value

    @property
    def position(self) -> Point3:
        """"""
        return self.__position

    @position.setter
    def position(self, value: Point3):
        """Set position"""
        self.__position = value

    @property
    def refPointXAxis(self) -> Point3:
        """"""
        return self.__refPointXAxis

    @refPointXAxis.setter
    def refPointXAxis(self, value: Point3):
        """Set refPointXAxis"""
        self.__refPointXAxis = value

    @property
    def refPointXYPlane(self) -> Point3:
        """"""
        return self.__refPointXYPlane

    @refPointXYPlane.setter
    def refPointXYPlane(self, value: Point3):
        """Set refPointXYPlane"""
        self.__refPointXYPlane = value

    @property
    def zcoef(self) -> float:
        """Vertical position used as reference for depth dependency"""
        return self.__zcoef

    @zcoef.setter
    def zcoef(self, value: float):
        """Set zcoef"""
        self.__zcoef = float(value)

    @property
    def depthDependentHydrodynamicCoefficients(self) -> List[DepthDependenthydrodynamicCoefficient]:
        """"""
        return self.__depthDependentHydrodynamicCoefficients

    @depthDependentHydrodynamicCoefficients.setter
    def depthDependentHydrodynamicCoefficients(self, value: List[DepthDependenthydrodynamicCoefficient]):
        """Set depthDependentHydrodynamicCoefficients"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__depthDependentHydrodynamicCoefficients = value

    @property
    def diffractedWave(self) -> DiffractedWave:
        """"""
        return self.__diffractedWave

    @diffractedWave.setter
    def diffractedWave(self, value: DiffractedWave):
        """Set diffractedWave"""
        self.__diffractedWave = value

    @property
    def c2x(self) -> float:
        """Quadratic drag x"""
        return self.__c2x

    @c2x.setter
    def c2x(self, value: float):
        """Set c2x"""
        self.__c2x = float(value)

    @property
    def c2y(self) -> float:
        """Quadratic drag y"""
        return self.__c2y

    @c2y.setter
    def c2y(self, value: float):
        """Set c2y"""
        self.__c2y = float(value)

    @property
    def c2z(self) -> float:
        """Quadratic drag z"""
        return self.__c2z

    @c2z.setter
    def c2z(self, value: float):
        """Set c2z"""
        self.__c2z = float(value)

    @property
    def c1x(self) -> float:
        """Linear drag x"""
        return self.__c1x

    @c1x.setter
    def c1x(self, value: float):
        """Set c1x"""
        self.__c1x = float(value)

    @property
    def c1y(self) -> float:
        """Linear drag y"""
        return self.__c1y

    @c1y.setter
    def c1y(self, value: float):
        """Set c1y"""
        self.__c1y = float(value)

    @property
    def c1z(self) -> float:
        """Linear drag z"""
        return self.__c1z

    @c1z.setter
    def c1z(self, value: float):
        """Set c1z"""
        self.__c1z = float(value)

    @property
    def amx(self) -> float:
        """Added mass x"""
        return self.__amx

    @amx.setter
    def amx(self, value: float):
        """Set amx"""
        self.__amx = float(value)

    @property
    def amy(self) -> float:
        """Added mass y"""
        return self.__amy

    @amy.setter
    def amy(self, value: float):
        """Set amy"""
        self.__amy = float(value)

    @property
    def amz(self) -> float:
        """Added mass z"""
        return self.__amz

    @amz.setter
    def amz(self, value: float):
        """Set amz"""
        self.__amz = float(value)
