# 
# Generated with TensionerBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class TensionerBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="Tensioner", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("appliedLoad","number","Applied load during static analysis",default=0.0))
        self.add_attribute(Attribute("maxLoad","number","Maximum load transmitted from the tensioner",default=0.0))
        self.add_attribute(Attribute("minLoad","number","Minimum load transmitted from the tensioner",default=0.0))
        self.add_attribute(Attribute("pipelineDisplacement","number","Pipeline displacement through the tensioner for a load variation of: max load - min load",default=0.0))
        self.add_attribute(Attribute("direction","number","Direction of the applied load referreing to local X-axis of the element going through the tensioner (+1 = The load will act in local X-axis. -1 = The load will act opposite local X-axis).",default=1.0))