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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("enterTime","number","Time when slug enters first end of main riser line",default=0.0))
        self.attributes.append(EnumAttribute("interruption","sima/riflex/SlugForceInterruption","Interruption parameter"))
        self.attributes.append(Attribute("length","number","Initial slug length",default=0.0))
        self.attributes.append(Attribute("mass","number","Slug mass",default=0.0))
        self.attributes.append(Attribute("velocity","number","Initial slug velocity",default=0.0))
        self.attributes.append(EnumAttribute("densityControl","sima/riflex/SlugForceDensityControl","Control parameter density"))
        self.attributes.append(EnumAttribute("velocityControl","sima/riflex/SlugForceVelocityControl","Control parameter velocity"))
        self.attributes.append(Attribute("cycles","integer","Number of slug cycles",default=1))
        self.attributes.append(Attribute("cycleTime","number","Slug cycle time",default=0.0))
        self.attributes.append(Attribute("secondPosition","number","Second vertical position for the slug unit mass",default=0.0))
        self.attributes.append(Attribute("massAtSecondPosition","number","Slug unit mass at second vertical position",default=0.0))
        self.attributes.append(Attribute("referenceDepth","number","Reference depth",default=0.0))
        self.attributes.append(Attribute("velocitySpecification","number","Velocity specification",default=0.0))
        self.attributes.append(Attribute("velocityExponent","number","Exponent for velocity",default=0.0))
        self.attributes.append(Attribute("importFlow","boolean","Import internal flow data from file",default=False))
        self.attributes.append(Attribute("flowFile","string","Internal flow data specification",default=""))
        self.attributes.append(Attribute("addedFlow","boolean","Specified flow is in addition to that given on main riser line (default is replacement)",default=False))