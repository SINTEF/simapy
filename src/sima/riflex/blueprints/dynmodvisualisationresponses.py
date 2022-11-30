# 
# Generated with DynmodVisualisationResponsesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class DynmodVisualisationResponsesBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DynmodVisualisationResponses", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("startTime","number","Start time for export",default=0.0))
        self.add_attribute(Attribute("endTime","number","End time for export",default=512.0))
        self.add_attribute(Attribute("timeIncrement","number","Time increment for export",default=0.5))
        self.add_attribute(Attribute("storeVisualisationResponses","boolean","Visualisation responses indicator",default=False))
        self.add_attribute(Attribute("storeVTF","boolean","Visualisation responses indicator",default=False))