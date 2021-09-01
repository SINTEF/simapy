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

    def __init__(self, name="SeaSurface", package_path="sima/environment", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("centerX","number","Center of surface in x",default=0.0))
        self.attributes.append(Attribute("centerY","number","Center of surface in y",default=0.0))
        self.attributes.append(Attribute("sizeX","number","Size of surface in x",default=500.0))
        self.attributes.append(Attribute("sizeY","number","Size of surface in y",default=500.0))
        self.attributes.append(BlueprintAttribute("color","sima/sima/SIMAColor","",True))
        self.attributes.append(Attribute("transparency","number","Transparency of surface",default=0.0))
        self.attributes.append(Attribute("meshGridSize","number","Size of grids in the mesh",default=100.0))
        self.attributes.append(Attribute("showMesh","boolean","Show mesh grid on surface",default=True))
        self.attributes.append(Attribute("z","number","Depth of surface",default=-100.0))
        self.attributes.append(Attribute("lcWaveLength","number","Length of long-crested wave field",default=300.0))
        self.attributes.append(Attribute("lcWaveWidth","number","Width of long-crested wave field",default=100.0))
        self.attributes.append(Attribute("lcWaveNumPoints","integer","Number of points in long-crested wave field",default=61))