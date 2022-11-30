# 
# Generated with RegularWaveLoadingBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RegularWaveLoadingBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RegularWaveLoading", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("waveTheory","sima/riflex/WaveTheory","Wave theory:\n - Airy linear wave theory\n - Stoke 5th order wave theory"))
        self.add_attribute(EnumAttribute("seaSurfaceDefinition","sima/riflex/KinematicsInWaveZone","Kinematics In Wave Zone:\n - Integration of wave forces to mean water level\n - Integration of wave forces to wave surface by stretching and compression of the wave potential\n - Integration of wave forces to wave surface by moving the potential to actual surface\n - Integration of wave forces to wave surface by keeping the potential constant from mean water level to water surface"))
        self.add_attribute(EnumAttribute("riserPosition","sima/riflex/RiserPosition","Kinematics Position:\n - Wave induced velocities and accelerations calculated at static riser position, but the riser is kept fixed in static position for computation of surface penetrating element\n - Wave induced velocities and accelerations calculated at static riser position\n - Wave induced velocities and accelerations calculated at updated (dynamic) positions"))