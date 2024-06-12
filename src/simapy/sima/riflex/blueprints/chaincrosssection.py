# 
# Generated with ChainCrossSectionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .crosssection import CrossSectionBlueprint

class ChainCrossSectionBlueprint(CrossSectionBlueprint):
    """"""

    def __init__(self, name="ChainCrossSection", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("diameter","number","Nominal chain diameter",default=0.0))
        self.add_attribute(EnumAttribute("steelGrade","sima/riflex/SteelGrade",""))
        self.add_attribute(EnumAttribute("constructionType","sima/riflex/ConstructionType",""))