# 
# Generated with CustomEditorBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class CustomEditorBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="CustomEditor", package_path="sima/custom", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("children","sima/custom/CustomComponent","",True,Dimension("*")))
        self.add_attribute(Attribute("title","string",""))
        self.add_attribute(Attribute("editMode","boolean","When checked the custom editor will always be opened in edit mode and child elements will be added to the navigator ",default=False))
        self.add_attribute(Attribute("showDescription","boolean","",default=False))