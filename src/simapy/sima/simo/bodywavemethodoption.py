# This an autogenerated file
# 
# Generated with BodyWaveMethodOption
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.bodywavemethodoption import BodyWaveMethodOptionBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .kinematicmethod import KinematicMethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .simobody import SIMOBody

class BodyWaveMethodOption(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    body : SIMOBody
    waveParticleMotions : KinematicMethod
         Options for wave particle motions
    waveParticleMotionDistributed : KinematicMethod
         Options for wave part. motions for distr. hydr. forces
    firstOrderWaveForce : KinematicMethod
         Options for first order wave forces
    firstOrderMotion : KinematicMethod
         Options for first order motion
    waveDriftForce : KinematicMethod
         Options for wave drift forces
    waveDriftDamping : KinematicMethod
         Options for wave drift damping
    qtf : KinematicMethod
         Options for forces from QTFs
    diffractedWave : KinematicMethod
         Options for diffracted wave
    """

    def __init__(self , description="", waveParticleMotions=KinematicMethod.FFT, waveParticleMotionDistributed=KinematicMethod.FFT, firstOrderWaveForce=KinematicMethod.FFT, firstOrderMotion=KinematicMethod.FFT, waveDriftForce=KinematicMethod.FFT, waveDriftDamping=KinematicMethod.FFT, qtf=KinematicMethod.FFT, diffractedWave=KinematicMethod.FFT, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.body = None
        self.waveParticleMotions = waveParticleMotions
        self.waveParticleMotionDistributed = waveParticleMotionDistributed
        self.firstOrderWaveForce = firstOrderWaveForce
        self.firstOrderMotion = firstOrderMotion
        self.waveDriftForce = waveDriftForce
        self.waveDriftDamping = waveDriftDamping
        self.qtf = qtf
        self.diffractedWave = diffractedWave
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BodyWaveMethodOptionBlueprint()


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
    def body(self) -> SIMOBody:
        """"""
        return self.__body

    @body.setter
    def body(self, value: SIMOBody):
        """Set body"""
        self.__body = value

    @property
    def waveParticleMotions(self) -> KinematicMethod:
        """Options for wave particle motions"""
        return self.__waveParticleMotions

    @waveParticleMotions.setter
    def waveParticleMotions(self, value: KinematicMethod):
        """Set waveParticleMotions"""
        self.__waveParticleMotions = value

    @property
    def waveParticleMotionDistributed(self) -> KinematicMethod:
        """Options for wave part. motions for distr. hydr. forces"""
        return self.__waveParticleMotionDistributed

    @waveParticleMotionDistributed.setter
    def waveParticleMotionDistributed(self, value: KinematicMethod):
        """Set waveParticleMotionDistributed"""
        self.__waveParticleMotionDistributed = value

    @property
    def firstOrderWaveForce(self) -> KinematicMethod:
        """Options for first order wave forces"""
        return self.__firstOrderWaveForce

    @firstOrderWaveForce.setter
    def firstOrderWaveForce(self, value: KinematicMethod):
        """Set firstOrderWaveForce"""
        self.__firstOrderWaveForce = value

    @property
    def firstOrderMotion(self) -> KinematicMethod:
        """Options for first order motion"""
        return self.__firstOrderMotion

    @firstOrderMotion.setter
    def firstOrderMotion(self, value: KinematicMethod):
        """Set firstOrderMotion"""
        self.__firstOrderMotion = value

    @property
    def waveDriftForce(self) -> KinematicMethod:
        """Options for wave drift forces"""
        return self.__waveDriftForce

    @waveDriftForce.setter
    def waveDriftForce(self, value: KinematicMethod):
        """Set waveDriftForce"""
        self.__waveDriftForce = value

    @property
    def waveDriftDamping(self) -> KinematicMethod:
        """Options for wave drift damping"""
        return self.__waveDriftDamping

    @waveDriftDamping.setter
    def waveDriftDamping(self, value: KinematicMethod):
        """Set waveDriftDamping"""
        self.__waveDriftDamping = value

    @property
    def qtf(self) -> KinematicMethod:
        """Options for forces from QTFs"""
        return self.__qtf

    @qtf.setter
    def qtf(self, value: KinematicMethod):
        """Set qtf"""
        self.__qtf = value

    @property
    def diffractedWave(self) -> KinematicMethod:
        """Options for diffracted wave"""
        return self.__diffractedWave

    @diffractedWave.setter
    def diffractedWave(self, value: KinematicMethod):
        """Set diffractedWave"""
        self.__diffractedWave = value
