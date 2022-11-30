# 
# Generated with SeaSurfaceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SeaSurfaceBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SeaSurface", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("centerX","number","Center of surface in x",default=0.0))
        self.add_attribute(Attribute("centerY","number","Center of surface in y",default=0.0))
        self.add_attribute(Attribute("sizeX","number","Size of surface in x",default=500.0))
        self.add_attribute(Attribute("sizeY","number","Size of surface in y",default=500.0))
        self.add_attribute(BlueprintAttribute("color","sima/sima/SIMAColor","",True))
        self.add_attribute(Attribute("transparency","number","Transparency of surface",default=0.0))
        self.add_attribute(Attribute("meshGridSize","number","Size of grids in the mesh",default=100.0))
        self.add_attribute(Attribute("showMesh","boolean","Show mesh grid on surface",default=False))
        self.add_attribute(Attribute("z","number","Depth of surface",default=-100.0))