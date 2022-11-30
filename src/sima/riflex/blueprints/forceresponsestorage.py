# 
# Generated with ForceResponseStorageBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ForceResponseStorageBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ForceResponseStorage", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("storageStep","integer","Code for storage of internal forces. Storage for every <storage step> given.",default=1))
        self.add_attribute(EnumAttribute("format","sima/riflex/FileFormatCode","Format code for additional output of time series"))
        self.add_attribute(BlueprintAttribute("elements","sima/riflex/ElementReference","Specification of nodes for displacement storage",True,Dimension("*")))
        self.add_attribute(EnumAttribute("matrixFormat","sima/riflex/AdditionalFileFormatCode","Format code for additional output of element transformation matrices"))
        self.add_attribute(Attribute("readTransformationMatrices","boolean","Make transformation matrices available in the post processor",default=False))
        self.add_attribute(BlueprintAttribute("relativeElementAngles","sima/riflex/RelativeElementAngle","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("elementAngles","sima/riflex/ElementAngle","",True,Dimension("*")))
        self.add_attribute(Attribute("storeBottomContactForces","boolean","Store results for seafloor contact elements and / or soil layer profile (SLP) contact elements",default=False))