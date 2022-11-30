# 
# Generated with EnvelopeCurveSpecificationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class EnvelopeCurveSpecificationBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="EnvelopeCurveSpecification", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("compDisplacement","boolean","Compute displacement envelopes?",default=False))
        self.add_attribute(Attribute("compForce","boolean","Compute force envelopes?",default=False))
        self.add_attribute(Attribute("compCurvature","boolean","Compute curvature envelopes?",default=False))
        self.add_attribute(Attribute("startTime","number","Simulation start time for computing envelopes",default=0.0))
        self.add_attribute(Attribute("endTime","number","Simulation end time for computing envelopes",default=10000000.0))
        self.add_attribute(Attribute("printDisplacement","boolean","Print displacement envelopes?",default=False))
        self.add_attribute(Attribute("printForce","boolean","Print force envelopes?",default=False))
        self.add_attribute(Attribute("printCurvature","boolean","Print curvature envelopes?",default=False))
        self.add_attribute(EnumAttribute("plotOption","sima/riflex/MatrixPlotFileOption",""))