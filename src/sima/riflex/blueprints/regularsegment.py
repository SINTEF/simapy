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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("length","number","Length of the segment.",default=0.0))
        self.attributes.append(Attribute("numElements","integer","Number of elements",default=10))
        self.attributes.append(BlueprintAttribute("crossSection","sima/riflex/CrossSection","Cross-sectional component type.",False))
        self.attributes.append(BlueprintAttribute("nodalComponent","sima/riflex/NodalComponentType","Nodal component (body or connector) attached at end 1 of the segment.",False))
        self.attributes.append(BlueprintAttribute("externalWrapping","sima/riflex/ExternalWrappingType","External wrapping (distributed weight or buoyancy) component.",False))
        self.attributes.append(Attribute("numSubElementsStatic","integer","Number of subelements each element is divided into for hydrodynamic calculation; static analysis.",default=3))
        self.attributes.append(Attribute("numSubElementsDynamic","integer","Number of subelements each element is divided into for hydrodynamic load calculation; dynamic analysis.",default=5))
        self.attributes.append(Attribute("stressfreeLength","number","Actual stressfree segment length.",default=0.0))
        self.attributes.append(Attribute("twistEnd1","number","Relative twist segment end 1",default=0.0))
        self.attributes.append(Attribute("twistEnd2","number","Relative twist segment end 2",default=0.0))
        self.attributes.append(Attribute("offsetY","number","Offset in line local Y-axis segment end 2",default=0.0))
        self.attributes.append(Attribute("offsetZ","number","Offset in line local Z-axis segment end 2",default=0.0))