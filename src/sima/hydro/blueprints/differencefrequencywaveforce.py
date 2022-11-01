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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("nFreq","integer","",default=0))
        self.attributes.append(Attribute("nDir","integer","",default=0))
        self.attributes.append(Attribute("bichromatic","boolean","",default=False))
        self.attributes.append(Attribute("bidirectional","boolean","",default=False))
        self.attributes.append(Attribute("frequencies","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("directions","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("onFile","boolean","",default=False))
        self.attributes.append(Attribute("file","string","",default=""))
        self.attributes.append(BlueprintAttribute("surge","sima/hydro/QTFDofItem","",True))
        self.attributes.append(BlueprintAttribute("sway","sima/hydro/QTFDofItem","",True))
        self.attributes.append(BlueprintAttribute("heave","sima/hydro/QTFDofItem","",True))
        self.attributes.append(BlueprintAttribute("roll","sima/hydro/QTFDofItem","",True))
        self.attributes.append(BlueprintAttribute("pitch","sima/hydro/QTFDofItem","",True))
        self.attributes.append(BlueprintAttribute("yaw","sima/hydro/QTFDofItem","",True))