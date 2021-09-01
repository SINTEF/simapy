# 
# Generated with NumericalWaveBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .wave import WaveBlueprint

class NumericalWaveBlueprint(WaveBlueprint):
    """"""

    def __init__(self, name="NumericalWave", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("directions","number","Number of wave directions",Dimension("size",""),default=0.0))
        self.attributes.append(Attribute("frequencies","number","Number of wave frequencies",Dimension("size",""),default=0.0))
        self.attributes.append(Attribute("values","number","",Dimension("size",""),default=0.0))