# 
# Generated with DifferenceFrequencyWaveForceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .quadratictransferfunction import QuadraticTransferFunctionBlueprint

class DifferenceFrequencyWaveForceBlueprint(QuadraticTransferFunctionBlueprint):
    """"""

    def __init__(self, name="DifferenceFrequencyWaveForce", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("nFreq","integer","",default=0))
        self.add_attribute(Attribute("nDir","integer","",default=0))
        self.add_attribute(Attribute("bichromatic","boolean","",default=False))
        self.add_attribute(Attribute("bidirectional","boolean","",default=False))
        self.add_attribute(Attribute("frequencies","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("directions","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("onFile","boolean","",default=False))
        self.add_attribute(Attribute("file","string",""))
        self.add_attribute(BlueprintAttribute("surge","sima/hydro/QTFDofItem","",True))
        self.add_attribute(BlueprintAttribute("sway","sima/hydro/QTFDofItem","",True))
        self.add_attribute(BlueprintAttribute("heave","sima/hydro/QTFDofItem","",True))
        self.add_attribute(BlueprintAttribute("roll","sima/hydro/QTFDofItem","",True))
        self.add_attribute(BlueprintAttribute("pitch","sima/hydro/QTFDofItem","",True))
        self.add_attribute(BlueprintAttribute("yaw","sima/hydro/QTFDofItem","",True))