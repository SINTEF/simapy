# 
# Generated with XYTableNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.post.blueprints.outputnode import OutputNodeBlueprint

class XYTableNodeBlueprint(OutputNodeBlueprint):
    """"""

    def __init__(self, name="XYTableNode", package_path="sima/workflow", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("inputSlot","sima/post/InputSlot","",True))
        self.add_attribute(Attribute("columnVariable","string","the values of this variable will create the columns of the table"))
        self.add_attribute(Attribute("rowVariable","string","the values of this variable will create the rows of the table"))
        self.add_attribute(Attribute("dataSeries","string","the values of this signal will be shown in the field matching the related variable values"))