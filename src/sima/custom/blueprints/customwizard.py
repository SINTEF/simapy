# 
# Generated with CustomWizardBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CustomWizardBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CustomWizard", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("title","string","",default=""))
        self.attributes.append(Attribute("selectionType","string","When an object of the given type is selected a popup menu will be enabled,",default=""))
        self.attributes.append(Attribute("menuLabel","string","Menu label shown in the popup",default=""))
        self.attributes.append(BlueprintAttribute("pages","sima/custom/CustomWizardPage","",True,Dimension("*")))
        self.attributes.append(Attribute("inline","boolean","Use inline script or external",default=True))
        self.attributes.append(Attribute("path","string","Path to the output file.",default=""))
        self.attributes.append(Attribute("finishScript","string","This script will be run when finishing the wizard. Use the variable selection to get hold of the object selected in the navigator",default=""))