# 
# Generated with RegularSegmentBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class RegularSegmentBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="RegularSegment", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("length","number","Length of the segment.",default=0.0))
        self.add_attribute(Attribute("numElements","integer","Number of elements",default=10))
        self.add_attribute(BlueprintAttribute("crossSection","sima/riflex/CrossSection","Cross-sectional component type.",False))
        self.add_attribute(BlueprintAttribute("nodalComponent","sima/riflex/NodalComponentType","Nodal component (body or connector) attached at end 1 of the segment.",False))
        self.add_attribute(BlueprintAttribute("externalWrapping","sima/riflex/ExternalWrappingType","External wrapping (distributed weight or buoyancy) component.",False))
        self.add_attribute(Attribute("numSubElementsStatic","integer","Number of subelements each element is divided into for hydrodynamic calculation; static analysis.",default=3))
        self.add_attribute(Attribute("numSubElementsDynamic","integer","Number of subelements each element is divided into for hydrodynamic load calculation; dynamic analysis.",default=5))
        self.add_attribute(Attribute("stressfreeLength","number","Actual stressfree segment length.",default=0.0))
        self.add_attribute(Attribute("twistEnd1","number","Relative twist segment end 1",default=0.0))
        self.add_attribute(Attribute("twistEnd2","number","Relative twist segment end 2",default=0.0))
        self.add_attribute(Attribute("offsetY","number","Offset in line local Y-axis segment end 2",default=0.0))
        self.add_attribute(Attribute("offsetZ","number","Offset in line local Z-axis segment end 2",default=0.0))