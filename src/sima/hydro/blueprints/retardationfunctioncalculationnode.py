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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("radiationData","sima/post/InputSlot","",True))
        self.attributes.append(BlueprintAttribute("structuralMass","sima/post/InputSlot","",True))
        self.attributes.append(BlueprintAttribute("extraDamping","sima/post/InputSlot","",True))
        self.attributes.append(BlueprintAttribute("outputSlot","sima/post/OutputSlot","",True))
        self.attributes.append(Attribute("timeStep","number","Retardation function timeStep",default=0.5))
        self.attributes.append(Attribute("powerOfTwo","integer","Length of array used for fft/ifft. Default 2**13.",default=13))
        self.attributes.append(Attribute("cutFactor","number","factor for cut of fft. Default 200",default=200.0))
        self.attributes.append(Attribute("useStructuralMass","boolean","Use structural mass together with a cut factor for removing certain degrees of freedom",default=True))
        self.attributes.append(Attribute("massCutFactor","number","Factor used together with structural mass to cut a degree of freedom.  Small factor means larger chance of cutting",default=100000.0))