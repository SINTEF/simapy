# 
# Generated with GeoTechnicalBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class GeoTechnicalBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="GeoTechnical", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("soilItems","sima/riflex/SoilItem","",True,Dimension("*")))
        self.attributes.append(Attribute("scourDepth","number","Length from mudline to actual contact point between mud and coductor",default=0.0))
        self.attributes.append(Attribute("diameter","number","Used for calculation of geotechnical spring properties",default=0.0))
        self.attributes.append(EnumAttribute("_type","sima/riflex/SoilStiffnessType",""))
        self.attributes.append(Attribute("calculateDiameter","boolean","Calculate diameter from cross-sections",default=True))
        self.attributes.append(Attribute("calculateAxialPileResistance","boolean","Calculate axial pile resistance",default=True))
        self.attributes.append(EnumAttribute("pileType","sima/riflex/GeotechnicalPileType",""))
        self.attributes.append(Attribute("zoneOfInfluence","number","Zone of influence",default=0.0))
        self.attributes.append(Attribute("curveFittingFactor","number","Curve fitting factor",default=0.0))