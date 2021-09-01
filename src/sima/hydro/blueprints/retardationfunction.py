# 
# Generated with RetardationFunctionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RetardationFunctionBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RetardationFunction", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("retardationElements","sima/hydro/RetardationElementData","",True,Dimension("size","")))
        self.attributes.append(Attribute("timeDelay","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("additionalDamping","sima/hydro/LinearDampingMatrix","",True))