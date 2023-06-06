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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("directions","number","Number of wave directions",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("frequencies","number","Number of wave frequencies",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("values","number","",Dimension("*"),default=0.0))