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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("lengthBetweenPerpendiculars","number","Length between perpendiculars",default=0.0))
        self.attributes.append(Attribute("maximumBeamAtWaterline","number","Maximum beam at the waterline",default=0.0))
        self.attributes.append(Attribute("draftAtAftPerpendicular","number","Draft at aft perpendicular",default=0.0))
        self.attributes.append(Attribute("draftAtForePerpendicular","number","Draft at fore perpendicular",default=0.0))
        self.attributes.append(Attribute("blockCoefficient","number","Block coefficient, Cb = displacement / (LWL * BWL * T)",default=0.0))
        self.attributes.append(Attribute("distanceAftPerpendicular","number","Distance from aft perpendicular to the body fixed origin",default=0.0))
        self.attributes.append(Attribute("distanceBaseline","number","Distance from baseline to the body fixed origin",default=0.0))
        self.attributes.append(Attribute("specifyWaterline","boolean","Should a waterline file be specified?",default=True))
        self.attributes.append(BlueprintAttribute("waterlinePoints","sima/simo/Point2","",True,Dimension("size","")))