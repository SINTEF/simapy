# 
# Generated with GDFGeometryBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class GDFGeometryBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="GDFGeometry", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("xSymmetry","integer","",default=0))
        self.add_attribute(Attribute("ySymmetry","integer","",default=0))
        self.add_attribute(Attribute("nValues","integer","",default=0))
        self.add_attribute(Attribute("values","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("dimensionalLength","number","",default=1.0))
        self.add_attribute(Attribute("gravitationalAcceleration","number","",default=9.81))