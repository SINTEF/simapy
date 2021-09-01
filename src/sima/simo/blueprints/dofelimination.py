# 
# Generated with DOFEliminationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DOFEliminationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DOFElimination", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("body","sima/simo/SIMOBody","",False))
        self.attributes.append(Attribute("x","boolean","Select to omit X degree of freedom",default=False))
        self.attributes.append(Attribute("y","boolean","Select to omit Y degree of freedom",default=False))
        self.attributes.append(Attribute("z","boolean","Select to omit Z degree of freedom",default=False))
        self.attributes.append(Attribute("rx","boolean","Select to omit RX degree of freedom",default=False))
        self.attributes.append(Attribute("ry","boolean","Select to omit RY degree of freedom",default=False))
        self.attributes.append(Attribute("rz","boolean","Select to omit RZ degree of freedom",default=False))