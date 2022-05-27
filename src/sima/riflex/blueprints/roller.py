# 
# Generated with RollerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class RollerBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="Roller", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("direction","number","Direction of roller axis (Clockwise around the local X-axis of the actual surface plane).",default=0.0))
        self.attributes.append(Attribute("y","number","Y-coordinate of roller origin",default=0.0))
        self.attributes.append(Attribute("z","number","Z-coordinate of roller origin",default=0.0))
        self.attributes.append(Attribute("length","number","Length of roller (0 means infinite length)",default=0.0))
        self.attributes.append(Attribute("constantStiffness","boolean","Constant spring compression stiffness.",default=False))
        self.attributes.append(Attribute("damping","number","Dash pot damping coefficient",default=0.0))
        self.attributes.append(Attribute("stiffness","number","Spring compression stiffness",default=0.0))
        self.attributes.append(Attribute("radius","number","Radius of roller",default=0.0))
        self.attributes.append(BlueprintAttribute("stiffnessItems","sima/riflex/SpringStiffnessItem","",True,Dimension("*")))