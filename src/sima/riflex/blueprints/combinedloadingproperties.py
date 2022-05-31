# 
# Generated with CombinedLoadingPropertiesBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .elementreference import ElementReferenceBlueprint

class CombinedLoadingPropertiesBlueprint(ElementReferenceBlueprint):
    """"""

    def __init__(self, name="CombinedLoadingProperties", package_path="sima/riflex", description=""):
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
        self.attributes.append(Attribute("youngsFactor","number","Young's modulus",default=210000000000.0))
        self.attributes.append(Attribute("poissonsRatio","number","Poisson's ratio for pipe wall material",default=0.3))
        self.attributes.append(Attribute("yieldStrength","number","Yield strength to be used in design",default=400000000.0))
        self.attributes.append(Attribute("tensileStrength","number","Tensile strength to be used in design",default=700000000.0))
        self.attributes.append(Attribute("ovality","number","Ovality",default=0.005))
        self.attributes.append(Attribute("internalCorrosion","number","Internal corrosion allowance",default=0.001))
        self.attributes.append(Attribute("externalCorrosion","number","External corrosion allowance",default=0.002))
        self.attributes.append(Attribute("nominalDiameter","number","Nominal outer diameter (D). If not set the value will be taken from the model",default=0.0))
        self.attributes.append(Attribute("nominalThickness","number","Nominal wall thickness (t_nom) of pipe (uncorroded), as specified on the drawing/specification ",default=0.0))