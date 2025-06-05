# 
# Generated with LinearHydrostaticsBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .hydrostaticstiffnessdata import HydrostaticStiffnessDataBlueprint

class LinearHydrostaticsBlueprint(HydrostaticStiffnessDataBlueprint):
    """"""

    def __init__(self, name="LinearHydrostatics", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("xcob","number","Center of buoyancy - x",default=0.0))
        self.add_attribute(Attribute("ycob","number","Center of buoyancy - y",default=0.0))
        self.add_attribute(Attribute("zcob","number","Center of buoyancy - z",default=0.0))
        self.add_attribute(Attribute("displacedVolume","number","",default=0.0))
        self.add_attribute(Attribute("k33norm","number","",default=0.0))
        self.add_attribute(Attribute("k34norm","number","",default=0.0))
        self.add_attribute(Attribute("k35norm","number","",default=0.0))
        self.add_attribute(Attribute("k44norm","number","",default=0.0))
        self.add_attribute(Attribute("k45norm","number","",default=0.0))
        self.add_attribute(Attribute("k55norm","number","",default=0.0))