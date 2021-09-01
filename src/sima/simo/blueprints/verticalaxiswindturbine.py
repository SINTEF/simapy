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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("controller","sima/windturbine/VerticalAxisWindTurbineController","",True))
        self.attributes.append(BlueprintAttribute("momentCoupling","sima/simo/MomentCoupling","",False))
        self.attributes.append(Attribute("referenceHeight","number","Reference height for calculation of wind",default=0.0))
        self.attributes.append(Attribute("windArea","number","Wind area admittance function",default=0.0))
        self.attributes.append(Attribute("radius","number","Blade radius at lowest node",default=0.0))
        self.attributes.append(Attribute("elevation","number","Elevation of the lowest node",default=0.0))
        self.attributes.append(Attribute("offset","number","Tangential offset of the first blade node",default=0.0))
        self.attributes.append(BlueprintAttribute("bladeItems","sima/simo/VerticalBladeItem","",True,Dimension("size","")))
        self.attributes.append(Attribute("numBlades","integer","Number of blades",default=0))
        self.attributes.append(Attribute("numAzimuthalElements","integer","Number of azimuthal elements for aerodynamic calculation",default=0))
        self.attributes.append(Attribute("prandtlFactor","number","Prandtl factor",default=-1.0))