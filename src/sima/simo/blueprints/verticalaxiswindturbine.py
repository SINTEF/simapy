# 
# Generated with VerticalAxisWindTurbineBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class VerticalAxisWindTurbineBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="VerticalAxisWindTurbine", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("controller","sima/windturbine/VerticalAxisWindTurbineController","",True))
        self.add_attribute(BlueprintAttribute("momentCoupling","sima/simo/MomentCoupling","",False))
        self.add_attribute(Attribute("referenceHeight","number","Reference height for calculation of wind",default=0.0))
        self.add_attribute(Attribute("windArea","number","Wind area admittance function",default=0.0))
        self.add_attribute(Attribute("radius","number","Blade radius at lowest node",default=0.0))
        self.add_attribute(Attribute("elevation","number","Elevation of the lowest node",default=0.0))
        self.add_attribute(Attribute("offset","number","Tangential offset of the first blade node",default=0.0))
        self.add_attribute(BlueprintAttribute("bladeItems","sima/simo/VerticalBladeItem","",True,Dimension("*")))
        self.add_attribute(Attribute("numBlades","integer","Number of blades",default=0))
        self.add_attribute(Attribute("numAzimuthalElements","integer","Number of azimuthal elements for aerodynamic calculation",default=0))
        self.add_attribute(Attribute("prandtlFactor","number","Prandtl factor",default=-1.0))