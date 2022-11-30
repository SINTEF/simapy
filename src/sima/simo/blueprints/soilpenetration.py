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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("frictionModel","sima/simo/SoilFriction","Soil force control parameter"))
        self.add_attribute(Attribute("zcont","number","Vertical coordinate of the lifted structure giving first\ncontact with the soil (landing)",default=0.0))
        self.add_attribute(Attribute("penetrationDepth","number","Depth at full penetration from first contact (positive upwards)",default=0.0))
        self.add_attribute(Attribute("barArea","number","Soil buoyancy cross section area",default=0.0))
        self.add_attribute(Attribute("sodens","number","Soil mass density",default=0.0))
        self.add_attribute(Attribute("cArea","number","Section area of cavity",default=0.0))
        self.add_attribute(EnumAttribute("seabedImport","sima/simo/HLA","Import of seabead depth values from HLA Depth value replaces ZCONT"))
        self.add_attribute(BlueprintAttribute("frictionElements","sima/simo/SoilFrictionElement","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("capacityElements","sima/simo/SoilCapacityElement","",True,Dimension("*")))
        self.add_attribute(Attribute("wstiff","number","Stiffness due to compressibility of water inside the cavity",default=0.0))
        self.add_attribute(Attribute("tsuct","number","Time for starting suction pumps",default=0.0))
        self.add_attribute(Attribute("cflow","number","Flow coefficient in/out of closed compartment",default=0.0))