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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(BlueprintAttribute("hsUpperLimits","sima/metocean/ScatterDimension","",True))
        self.attributes.append(BlueprintAttribute("tpUpperLimits","sima/metocean/ScatterDimension","",True))
        self.attributes.append(Attribute("values","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("unit","string","",default=""))