# 
# Generated with SlugForceSpecificationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SlugForceSpecificationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SlugForceSpecification", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("enterTime","number","Time when slug enters first end of main riser line",default=0.0))
        self.add_attribute(EnumAttribute("interruption","sima/riflex/SlugForceInterruption","Interruption parameter"))
        self.add_attribute(Attribute("length","number","Initial slug length",default=0.0))
        self.add_attribute(Attribute("mass","number","Slug mass",default=0.0))
        self.add_attribute(Attribute("velocity","number","Initial slug velocity",default=0.0))
        self.add_attribute(EnumAttribute("densityControl","sima/riflex/SlugForceDensityControl","Control parameter density"))
        self.add_attribute(EnumAttribute("velocityControl","sima/riflex/SlugForceVelocityControl","Control parameter velocity"))
        self.add_attribute(Attribute("cycles","integer","Number of slug cycles",default=1))
        self.add_attribute(Attribute("cycleTime","number","Slug cycle time",default=0.0))
        self.add_attribute(Attribute("secondPosition","number","Second vertical position for the slug unit mass",default=0.0))
        self.add_attribute(Attribute("massAtSecondPosition","number","Slug unit mass at second vertical position",default=0.0))
        self.add_attribute(Attribute("referenceDepth","number","Reference depth",default=0.0))
        self.add_attribute(Attribute("velocitySpecification","number","Velocity specification",default=0.0))
        self.add_attribute(Attribute("velocityExponent","number","Exponent for velocity",default=0.0))
        self.add_attribute(Attribute("importFlow","boolean","Import internal flow data from file",default=False))
        self.add_attribute(Attribute("flowFile","string","Internal flow data specification"))
        self.add_attribute(Attribute("addedFlow","boolean","Specified flow is in addition to that given on main riser line (default is replacement)",default=False))