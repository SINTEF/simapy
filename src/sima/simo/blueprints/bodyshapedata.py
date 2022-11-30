# 
# Generated with BodyShapeDataBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class BodyShapeDataBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="BodyShapeData", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("lengthBetweenPerpendiculars","number","Length between perpendiculars",default=0.0))
        self.add_attribute(Attribute("maximumBeamAtWaterline","number","Maximum beam at the waterline",default=0.0))
        self.add_attribute(Attribute("draftAtAftPerpendicular","number","Draft at aft perpendicular",default=0.0))
        self.add_attribute(Attribute("draftAtForePerpendicular","number","Draft at fore perpendicular",default=0.0))
        self.add_attribute(Attribute("blockCoefficient","number","Block coefficient, Cb = displacement / (LWL * BWL * T)",default=0.0))
        self.add_attribute(Attribute("distanceAftPerpendicular","number","Distance from aft perpendicular to the body fixed origin",default=0.0))
        self.add_attribute(Attribute("distanceBaseline","number","Distance from baseline to the body fixed origin",default=0.0))
        self.add_attribute(Attribute("specifyWaterline","boolean","Should a waterline file be specified?",default=False))
        self.add_attribute(BlueprintAttribute("waterlinePoints","sima/simo/Point2","",True,Dimension("*")))