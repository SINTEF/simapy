# 
# Generated with SoilPenetrationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SoilPenetrationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SoilPenetration", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("frictionModel","sima/simo/SoilFriction","Soil force control parameter"))
        self.attributes.append(Attribute("zcont","number","Vertical coordinate of the lifted structure giving first\ncontact with the soil (landing)",default=0.0))
        self.attributes.append(Attribute("penetrationDepth","number","Depth at full penetration from first contact (positive upwards)",default=0.0))
        self.attributes.append(Attribute("barArea","number","Soil buoyancy cross section area",default=0.0))
        self.attributes.append(Attribute("sodens","number","Soil mass density",default=0.0))
        self.attributes.append(Attribute("cArea","number","Section area of cavity",default=0.0))
        self.attributes.append(EnumAttribute("seabedImport","sima/simo/HLA","Import of seabead depth values from HLA Depth value replaces ZCONT"))
        self.attributes.append(BlueprintAttribute("frictionElements","sima/simo/SoilFrictionElement","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("capacityElements","sima/simo/SoilCapacityElement","",True,Dimension("*")))
        self.attributes.append(Attribute("wstiff","number","Stiffness due to compressibility of water inside the cavity",default=0.0))
        self.attributes.append(Attribute("tsuct","number","Time for starting suction pumps",default=0.0))
        self.attributes.append(Attribute("cflow","number","Flow coefficient in/out of closed compartment",default=0.0))