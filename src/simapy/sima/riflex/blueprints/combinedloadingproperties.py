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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("segment","integer","Segment on given line",default=1))
        self.add_attribute(Attribute("allSegments","boolean","All segments",default=False))
        self.add_attribute(Attribute("elementNumber","integer","Local element number on actual segment",default=1))
        self.add_attribute(Attribute("allElements","boolean","All elements",default=False))
        self.add_attribute(Attribute("youngsFactor","number","Young's modulus",default=210000000000.0))
        self.add_attribute(Attribute("poissonsRatio","number","Poisson's ratio for pipe wall material",default=0.3))
        self.add_attribute(Attribute("yieldStrength","number","Yield strength to be used in design",default=400000000.0))
        self.add_attribute(Attribute("tensileStrength","number","Tensile strength to be used in design",default=700000000.0))
        self.add_attribute(Attribute("ovality","number","Ovality",default=0.005))
        self.add_attribute(Attribute("internalCorrosion","number","Internal corrosion allowance",default=0.001))
        self.add_attribute(Attribute("externalCorrosion","number","External corrosion allowance",default=0.002))
        self.add_attribute(Attribute("nominalDiameter","number","Nominal outer diameter (D). If not set the value will be taken from the model",default=0.0))
        self.add_attribute(Attribute("nominalThickness","number","Nominal wall thickness (t_nom) of pipe (uncorroded), as specified on the drawing/specification ",default=0.0))