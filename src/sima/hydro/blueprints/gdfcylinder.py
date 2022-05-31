# 
# Generated with GDFCylinderBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class GDFCylinderBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="GDFCylinder", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("dimensionalLength","number","Dimensional length",default=1.0))
        self.attributes.append(Attribute("centerX","number","Global x-coordinate",default=0.0))
        self.attributes.append(Attribute("centerY","number","Global y-coordinate",default=0.0))
        self.attributes.append(Attribute("radius","number","Radius of cyllinder",default=40.0))
        self.attributes.append(Attribute("numberOfRadialPanels","integer","Number of panels around the circumference",default=20))
        self.attributes.append(Attribute("depth","number","Depth of cylinder (1 means equidistant)",default=20.0))
        self.attributes.append(Attribute("numberOfVerticalPanels","integer","Number of depth levels",default=10))
        self.attributes.append(Attribute("exponent","number","Exponent in depth distribution",default=2.0))