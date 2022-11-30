# 
# Generated with RetardationFunctionCalculationNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.runnode import RunNodeBlueprint

class RetardationFunctionCalculationNodeBlueprint(RunNodeBlueprint):
    """"""

    def __init__(self, name="RetardationFunctionCalculationNode", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("radiationData","sima/post/InputSlot","",True))
        self.add_attribute(BlueprintAttribute("structuralMass","sima/post/InputSlot","",True))
        self.add_attribute(BlueprintAttribute("extraDamping","sima/post/InputSlot","",True))
        self.add_attribute(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.add_attribute(Attribute("timeStep","number","Retardation function timeStep",default=0.5))
        self.add_attribute(Attribute("powerOfTwo","integer","Length of array used for fft/ifft. Default 2**13.",default=13))
        self.add_attribute(Attribute("cutFactor","number","factor for cut of fft. Default 200",default=200.0))
        self.add_attribute(Attribute("useStructuralMass","boolean","Use structural mass together with a cut factor for removing certain degrees of freedom",default=True))
        self.add_attribute(Attribute("massCutFactor","number","Factor used together with structural mass to cut a degree of freedom.  Small factor means larger chance of cutting",default=100000.0))