# 
# Generated with ScatterDiagramBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.named import NamedBlueprint

class ScatterDiagramBlueprint(NamedBlueprint):
    """"""

    def __init__(self, name="ScatterDiagram", package_path="sima/metocean", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("hsUpperLimits","sima/metocean/ScatterDimension","",True))
        self.add_attribute(BlueprintAttribute("tpUpperLimits","sima/metocean/ScatterDimension","",True))
        self.add_attribute(Attribute("values","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("unit","string",""))