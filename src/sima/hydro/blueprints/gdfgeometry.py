# 
# Generated with GDFGeometryBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class GDFGeometryBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="GDFGeometry", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("xSymmetry","integer","",default=0))
        self.attributes.append(Attribute("ySymmetry","integer","",default=0))
        self.attributes.append(Attribute("nValues","integer","",default=0))
        self.attributes.append(Attribute("values","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("dimensionalLength","number","",default=1.0))
        self.attributes.append(Attribute("gravitationalAcceleration","number","",default=9.81))