# 
# Generated with StressJointSegmentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class StressJointSegmentBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="StressJointSegment", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("length","number","Length of the segment.",default=0.0))
        self.attributes.append(Attribute("numElements","integer","Number of elements",default=10))
        self.attributes.append(Attribute("extDiameterEnd2","number","External diameter at second end of actual segment.",default=0.0))
        self.attributes.append(Attribute("wallThicknessEnd2","number","Wall thickness at second end.",default=0.0))
        self.attributes.append(Attribute("elasticModulus","number","Elastic modulus.",default=0.0))
        self.attributes.append(Attribute("materialDensity","number","Density of pipe material.",default=0.0))