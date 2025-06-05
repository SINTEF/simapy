# 
# Generated with EnvelopeCurveSpecificationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class EnvelopeCurveSpecificationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="EnvelopeCurveSpecification", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("storeDisplacement","boolean","Store displacement envelopes",default=False))
        self.add_attribute(Attribute("storeForce","boolean","Store force envelopes",default=False))
        self.add_attribute(Attribute("storeCurvature","boolean","Store curvature envelopes",default=False))
        self.add_attribute(Attribute("startTime","number","Simulation start time for computing envelopes",default=0.0))
        self.add_attribute(Attribute("endTime","number","Simulation end time for computing envelopes",default=10000000.0))
        self.add_attribute(EnumAttribute("plotOption","sima/riflex/MatrixPlotFileOption",""))