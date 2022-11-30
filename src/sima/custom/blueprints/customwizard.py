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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("title","string",""))
        self.add_attribute(Attribute("selectionType","string","When an object of the given type is selected a popup menu will be enabled,"))
        self.add_attribute(Attribute("menuLabel","string","Menu label shown in the popup"))
        self.add_attribute(BlueprintAttribute("pages","sima/custom/CustomWizardPage","",True,Dimension("*")))
        self.add_attribute(Attribute("inline","boolean","Use inline script or external",default=True))
        self.add_attribute(Attribute("path","string","Path to the output file."))
        self.add_attribute(Attribute("finishScript","string","This script will be run when finishing the wizard. Use the variable selection to get hold of the object selected in the navigator"))