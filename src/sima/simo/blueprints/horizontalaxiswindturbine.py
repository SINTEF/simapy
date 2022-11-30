# 
# Generated with HorizontalAxisWindTurbineBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class HorizontalAxisWindTurbineBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="HorizontalAxisWindTurbine", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("controller","sima/windturbine/HorizontalAxisWindTurbineController","",True))
        self.add_attribute(BlueprintAttribute("momentCoupling","sima/simo/MomentCoupling","",False))
        self.add_attribute(Attribute("referenceHeight","number","Reference height for calculation of wind",default=0.0))
        self.add_attribute(Attribute("windArea","number","Wind area admittance function",default=0.0))
        self.add_attribute(Attribute("outerAirfoilRadius","number","Outer airfoil radius",default=0.0))
        self.add_attribute(Attribute("coneAngle","number","Cone angle",default=0.0))
        self.add_attribute(BlueprintAttribute("bladeItems","sima/simo/BladeItem","",True,Dimension("*")))
        self.add_attribute(Attribute("numBlades","integer","Number of blades",default=0))