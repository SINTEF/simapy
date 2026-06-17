# 
# Generated with GeometricShapeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .shape import ShapeBlueprint

class GeometricShapeBlueprint(ShapeBlueprint):
    """"""

    def __init__(self, name="GeometricShape", package_path="sima/sima", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","number","",default=0.0))
        self.add_attribute(Attribute("y","number","",default=0.0))
        self.add_attribute(Attribute("z","number","",default=0.0))
        self.add_attribute(Attribute("rotX","number","",default=0.0))
        self.add_attribute(Attribute("rotY","number","",default=0.0))
        self.add_attribute(Attribute("rotZ","number","",default=0.0))
        self.add_attribute(Attribute("length","number","Length",default=10.0))
        self.add_attribute(Attribute("width","number","Width",default=5.0))
        self.add_attribute(Attribute("height","number","Height",default=5.0))
        self.add_attribute(BlueprintAttribute("appearance","sima/sima/Appearance","",True))