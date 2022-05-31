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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("inputSlot","sima/post/InputSlot","",True))
        self.attributes.append(Attribute("columnVariable","string","the values of this variable will create the columns of the table",default=""))
        self.attributes.append(Attribute("rowVariable","string","the values of this variable will create the rows of the table",default=""))
        self.attributes.append(Attribute("dataSeries","string","the values of this signal will be shown in the field matching the related variable values",default=""))