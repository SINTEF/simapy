# 
# Generated with ScatterDimensionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ScatterDimensionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ScatterDimension", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("nValues","integer","",default=0))
        self.add_attribute(Attribute("values","number","Scatter values",Dimension("*"),default=0.0))