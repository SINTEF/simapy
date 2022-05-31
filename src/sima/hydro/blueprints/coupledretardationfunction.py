# 
# Generated with CoupledRetardationFunctionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .retardationfunction import RetardationFunctionBlueprint

class CoupledRetardationFunctionBlueprint(RetardationFunctionBlueprint):
    """"""

    def __init__(self, name="CoupledRetardationFunction", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("retardationElements","sima/hydro/RetardationElementData","",True,Dimension("*")))
        self.attributes.append(Attribute("timeDelay","number","",default=0.0))
        self.attributes.append(BlueprintAttribute("additionalDamping","sima/hydro/LinearDampingMatrix","",True))