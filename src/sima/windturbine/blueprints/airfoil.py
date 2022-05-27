# 
# Generated with AirfoilBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class AirfoilBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="Airfoil", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("deepstallRegime","boolean","Whether or not a deep stall regime is to be used",default=False))
        self.attributes.append(Attribute("inputStallPoints","boolean","",default=False))
        self.attributes.append(Attribute("upperTailAngle","number","Tail angle between a line perpendicular to the flow and the line from the tip of the wedge, low (negative) angles of attack",default=0.0))
        self.attributes.append(Attribute("lowerTailAngle","number","As upper tail angle, but for high (positive) angles of attack",default=0.0))
        self.attributes.append(Attribute("upperNoseAngle","number","Nose angle between a line perpendicular to the flow and the line from the tip of the wedge, low (negative) angles of attack",default=0.0))
        self.attributes.append(Attribute("lowerNoseAngle","number","As upper nose angle, but for high (positive) angles of attack",default=0.0))
        self.attributes.append(Attribute("noseRadiusRatio","number","The ratio of the nose radius to the chord of the airfoil.",default=0.0))
        self.attributes.append(BlueprintAttribute("reynoldItems","sima/windturbine/ReynoldItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("points","sima/windturbine/FoilPoint","",True,Dimension("*")))