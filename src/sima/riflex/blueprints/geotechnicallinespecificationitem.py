# 
# Generated with GeotechnicalLineSpecificationItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class GeotechnicalLineSpecificationItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="GeotechnicalLineSpecificationItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("geotechnical","sima/riflex/GeoTechnical","",False))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","",False))
        self.attributes.append(Attribute("seabedZCoordinate","number","Global Z coordinate of seafloor",default=0.0))