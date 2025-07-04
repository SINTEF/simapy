# 
# Generated with ExternalPythonForceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.namedobject import NamedObjectBlueprint

class ExternalPythonForceBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="ExternalPythonForce", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("file","string",""))
        self.add_attribute(Attribute("className","string","Python class name contained in the python file",default='0'))
        self.add_attribute(BlueprintAttribute("parameters","sima/sima/SingleValue","",True,Dimension("*")))