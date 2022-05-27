# 
# Generated with PointFieldBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class PointFieldBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="PointField", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("xMin","number","x start coordinate ",default=0.0))
        self.attributes.append(Attribute("xMax","number","x end coordinate ",default=0.0))
        self.attributes.append(Attribute("yMin","number","y start coordinate ",default=0.0))
        self.attributes.append(Attribute("yMax","number","y end coordinate ",default=0.0))
        self.attributes.append(Attribute("zMin","number","z start coordinate ",default=0.0))
        self.attributes.append(Attribute("zMax","number","z end coordinate ",default=0.0))
        self.attributes.append(Attribute("xNumberOfPoints","integer","number of points in x direction",default=0))
        self.attributes.append(Attribute("yNumberOfPoints","integer","number of points in y direction",default=0))
        self.attributes.append(Attribute("zNumberOfPoints","integer","number of points in z direction",default=0))
        self.attributes.append(Attribute("visible","boolean","",default=True))