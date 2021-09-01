# 
# Generated with ThrusterDynamicsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ThrusterDynamicsBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ThrusterDynamics", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("minTimeChange","number","Minimum time to change from 10% to 90% of maximum thrust",default=0.0))
        self.attributes.append(Attribute("tcThrust","number","Time constant of thrust",default=0.0))
        self.attributes.append(Attribute("maxRevolvingSpeed","number","Maximum revolving speed",default=10.0))
        self.attributes.append(Attribute("tcAzimuth","number","Time constant of azimuth change",default=0.0))