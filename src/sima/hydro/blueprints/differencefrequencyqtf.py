# 
# Generated with DifferenceFrequencyQTFBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .sparseqtf import SparseQTFBlueprint

class DifferenceFrequencyQTFBlueprint(SparseQTFBlueprint):
    """"""

    def __init__(self, name="DifferenceFrequencyQTF", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("nFreq","integer","",default=0))
        self.attributes.append(Attribute("nDir","integer","",default=0))
        self.attributes.append(Attribute("nValues","integer","",default=0))
        self.attributes.append(Attribute("bidirectional","boolean","",default=False))
        self.attributes.append(Attribute("bichromatic","boolean","",default=False))
        self.attributes.append(Attribute("directions","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("frequencies","number","",Dimension("*"),default=0.0))
        self.attributes.append(Attribute("di","integer","",Dimension("*"),default=0))
        self.attributes.append(Attribute("dj","integer","",Dimension("*"),default=0))
        self.attributes.append(Attribute("wi","integer","",Dimension("*"),default=0))
        self.attributes.append(Attribute("wj","integer","",Dimension("*"),default=0))
        self.attributes.append(BlueprintAttribute("surge","sima/hydro/QTFDof","",True))
        self.attributes.append(BlueprintAttribute("sway","sima/hydro/QTFDof","",True))
        self.attributes.append(BlueprintAttribute("heave","sima/hydro/QTFDof","",True))
        self.attributes.append(BlueprintAttribute("roll","sima/hydro/QTFDof","",True))
        self.attributes.append(BlueprintAttribute("pitch","sima/hydro/QTFDof","",True))
        self.attributes.append(BlueprintAttribute("yaw","sima/hydro/QTFDof","",True))