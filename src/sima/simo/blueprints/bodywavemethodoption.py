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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("body","sima/simo/SIMOBody","",False))
        self.attributes.append(EnumAttribute("waveParticleMotions","sima/simo/KinematicMethod","Options for wave particle motions"))
        self.attributes.append(EnumAttribute("waveParticleMotionDistributed","sima/simo/KinematicMethod","Options for wave part. motions for distr. hydr. forces"))
        self.attributes.append(EnumAttribute("firstOrderWaveForce","sima/simo/KinematicMethod","Options for first order wave forces"))
        self.attributes.append(EnumAttribute("firstOrderMotion","sima/simo/KinematicMethod","Options for first order motion"))
        self.attributes.append(EnumAttribute("waveDriftForce","sima/simo/KinematicMethod","Options for wave drift forces"))
        self.attributes.append(EnumAttribute("waveDriftDamping","sima/simo/KinematicMethod","Options for wave drift damping"))
        self.attributes.append(EnumAttribute("qtf","sima/simo/KinematicMethod","Options for forces from QTFs"))
        self.attributes.append(EnumAttribute("diffractedWave","sima/simo/KinematicMethod","Options for diffracted wave"))