# 
# Generated with BodyWaveMethodOptionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BodyWaveMethodOptionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BodyWaveMethodOption", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("body","sima/simo/SIMOBody","",False))
        self.add_attribute(EnumAttribute("waveParticleMotions","sima/simo/KinematicMethod","Options for wave particle motions"))
        self.add_attribute(EnumAttribute("waveParticleMotionDistributed","sima/simo/KinematicMethod","Options for wave part. motions for distr. hydr. forces"))
        self.add_attribute(EnumAttribute("firstOrderWaveForce","sima/simo/KinematicMethod","Options for first order wave forces"))
        self.add_attribute(EnumAttribute("firstOrderMotion","sima/simo/KinematicMethod","Options for first order motion"))
        self.add_attribute(EnumAttribute("waveDriftForce","sima/simo/KinematicMethod","Options for wave drift forces"))
        self.add_attribute(EnumAttribute("waveDriftDamping","sima/simo/KinematicMethod","Options for wave drift damping"))
        self.add_attribute(EnumAttribute("qtf","sima/simo/KinematicMethod","Options for forces from QTFs"))
        self.add_attribute(EnumAttribute("diffractedWave","sima/simo/KinematicMethod","Options for diffracted wave"))