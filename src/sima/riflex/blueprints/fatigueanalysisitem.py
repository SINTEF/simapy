# 
# Generated with FatigueAnalysisItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .elementreference import ElementReferenceBlueprint

class FatigueAnalysisItemBlueprint(ElementReferenceBlueprint):
    """"""

    def __init__(self, name="FatigueAnalysisItem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("segment","integer","Segment on given line",default=1))
        self.add_attribute(Attribute("allSegments","boolean","All segments",default=False))
        self.add_attribute(Attribute("elementNumber","integer","Local element number on actual segment",default=1))
        self.add_attribute(Attribute("allElements","boolean","All elements",default=False))
        self.add_attribute(Attribute("allEnds","boolean","All ends",default=False))
        self.add_attribute(EnumAttribute("elementEnd","sima/riflex/End","End number 1 or 2"))
        self.add_attribute(Attribute("stressConcentrationFactor","number","Stress consentration factor",default=1.0))
        self.add_attribute(BlueprintAttribute("snCurve","sima/riflex/SNCurve","",False))
        self.add_attribute(Attribute("effectiveThickness","number","Thickness used in thickness correction of the SN curves. Default value is the same as the wall thickness",default=0.0))
        self.add_attribute(Attribute("crossSectionalArea","number","Optional cross sectional area",default=0.0))
        self.add_attribute(Attribute("sectionModulus","number","Optional section modulus",default=0.0))