# 
# Generated with SIMOModelBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.environment.blueprints.environmentscontainer import EnvironmentsContainerBlueprint

class SIMOModelBlueprint(EnvironmentsContainerBlueprint):
    """"""

    def __init__(self, name="SIMOModel", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("environments","sima/environment/Environment","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("airfoils","sima/windturbine/Airfoil","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("location","sima/simo/SIMOLocation","",True))
        self.add_attribute(BlueprintAttribute("bodies","sima/simo/SIMOBody","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("hydrodynamicCouplings","sima/simo/HydrodynamicCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("simpleWireCouplings","sima/simo/SimpleWireCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("fixedElongationCouplings","sima/simo/FixedElongationCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("dockingCones","sima/simo/DockingCone","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("pointFenders","sima/simo/PointFender","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("rollerFenders","sima/simo/RollerFender","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("ratchets","sima/simo/RatchetCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("multipleWireCouplings","sima/simo/MultipleWireCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("bumperGroups","sima/simo/BumperGroup","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("advancedBumpers","sima/simo/AdvancedBumper","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("liftLineCouplings","sima/simo/LiftLineCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("momentCouplings","sima/simo/MomentCoupling","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("sIMOStaticCalculationParameters","sima/simo/SIMOStaticCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("sIMODynamicCalculationParameters","sima/simo/SIMODynamicCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("stabilityCalculationParameters","sima/simo/StabilityCalculationParameters","",True))
        self.add_attribute(BlueprintAttribute("simoFrequencyDomainCalculation","sima/simo/SIMOFrequencyDomainCalculation","",True))
        self.add_attribute(BlueprintAttribute("fibreRopeModels","sima/simo/FibreRopeModel","",True,Dimension("*")))