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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("body","sima/simo/SIMOBody","",False))
        self.add_attribute(Attribute("x","boolean","Select to omit X degree of freedom",default=False))
        self.add_attribute(Attribute("y","boolean","Select to omit Y degree of freedom",default=False))
        self.add_attribute(Attribute("z","boolean","Select to omit Z degree of freedom",default=False))
        self.add_attribute(Attribute("rx","boolean","Select to omit RX degree of freedom",default=False))
        self.add_attribute(Attribute("ry","boolean","Select to omit RY degree of freedom",default=False))
        self.add_attribute(Attribute("rz","boolean","Select to omit RZ degree of freedom",default=False))