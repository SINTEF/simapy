# 
# Generated with WasimResultExportBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class WasimResultExportBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="WasimResultExport", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("floaterBody","sima/simo/SIMOBody","",False))
        self.attributes.append(BlueprintAttribute("pointForces","sima/simo/BodyForceComponentReference","",True,Dimension("*")))
        self.attributes.append(Attribute("maxNumberOfWaveComponents","integer","Limit the number of wave components exported to file",default=0))