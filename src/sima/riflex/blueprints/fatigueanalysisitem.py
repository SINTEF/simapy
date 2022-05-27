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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.attributes.append(Attribute("segment","integer","Segment on given line",default=1))
        self.attributes.append(Attribute("allSegments","boolean","All segments",default=False))
        self.attributes.append(Attribute("elementNumber","integer","Local element number on actual segment",default=1))
        self.attributes.append(Attribute("allElements","boolean","All elements",default=False))
        self.attributes.append(Attribute("allEnds","boolean","All ends",default=False))
        self.attributes.append(EnumAttribute("elementEnd","sima/riflex/End","End number 1 or 2"))
        self.attributes.append(Attribute("stressConcentrationFactor","number","Stress consentration factor",default=1.0))
        self.attributes.append(BlueprintAttribute("snCurve","sima/riflex/SNCurve","",False))
        self.attributes.append(Attribute("effectiveThickness","number","Thickness used in thickness correction of the SN curves. Default value is the same as the wall thickness",default=0.0))
        self.attributes.append(Attribute("crossSectionalArea","number","Optional cross sectional area",default=0.0))
        self.attributes.append(Attribute("sectionModulus","number","Optional section modulus",default=0.0))