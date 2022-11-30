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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("soilItems","sima/riflex/SoilItem","",True,Dimension("*")))
        self.add_attribute(Attribute("scourDepth","number","Length from mudline to actual contact point between mud and coductor",default=0.0))
        self.add_attribute(Attribute("diameter","number","Used for calculation of geotechnical spring properties",default=0.0))
        self.add_attribute(EnumAttribute("_type","sima/riflex/SoilStiffnessType",""))
        self.add_attribute(Attribute("calculateDiameter","boolean","Calculate diameter from cross-sections",default=True))
        self.add_attribute(Attribute("calculateAxialPileResistance","boolean","Calculate axial pile resistance",default=False))
        self.add_attribute(EnumAttribute("pileType","sima/riflex/GeotechnicalPileType",""))
        self.add_attribute(Attribute("zoneOfInfluence","number","Zone of influence",default=0.0))
        self.add_attribute(Attribute("curveFittingFactor","number","Curve fitting factor",default=0.0))