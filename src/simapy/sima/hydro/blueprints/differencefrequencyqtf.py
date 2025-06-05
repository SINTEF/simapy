# 
# Generated with DifferenceFrequencyQTFBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class DifferenceFrequencyQTFBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DifferenceFrequencyQTF", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("nFreq","integer","",default=0))
        self.add_attribute(Attribute("nDir","integer","",default=0))
        self.add_attribute(Attribute("nValues","integer","",default=0))
        self.add_attribute(Attribute("bidirectional","boolean","",default=False))
        self.add_attribute(Attribute("bichromatic","boolean","",default=False))
        self.add_attribute(Attribute("directions","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("frequencies","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("di","integer","",Dimension("*"),default=0))
        self.add_attribute(Attribute("dj","integer","",Dimension("*"),default=0))
        self.add_attribute(Attribute("wi","integer","",Dimension("*"),default=0))
        self.add_attribute(Attribute("wj","integer","",Dimension("*"),default=0))
        self.add_attribute(BlueprintAttribute("surge","sima/hydro/QTFDof","",True))
        self.add_attribute(BlueprintAttribute("sway","sima/hydro/QTFDof","",True))
        self.add_attribute(BlueprintAttribute("heave","sima/hydro/QTFDof","",True))
        self.add_attribute(BlueprintAttribute("roll","sima/hydro/QTFDof","",True))
        self.add_attribute(BlueprintAttribute("pitch","sima/hydro/QTFDof","",True))
        self.add_attribute(BlueprintAttribute("yaw","sima/hydro/QTFDof","",True))
        self.add_attribute(EnumAttribute("symmetry","sima/hydro/DirectionSymmetry",""))
        self.add_attribute(Attribute("enableCurrentCorrection","boolean","Enable wave-current interaction using extended Aranha formula",default=False))
        self.add_attribute(EnumAttribute("input","sima/hydro/QtfInput",""))
        self.add_attribute(Attribute("file","string",""))
        self.add_attribute(Attribute("bodyNumber","integer","If file is multi-body, give the number within the file for this data",default=1))