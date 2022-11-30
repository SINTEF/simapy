# 
# Generated with LocalElementAxisBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .elementreference import ElementReferenceBlueprint

class LocalElementAxisBlueprint(ElementReferenceBlueprint):
    """"""

    def __init__(self, name="LocalElementAxis", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("segment","integer","Segment on given line",default=1))
        self.add_attribute(Attribute("allSegments","boolean","All segments",default=False))
        self.add_attribute(Attribute("elementNumber","integer","Local element number on actual segment",default=1))
        self.add_attribute(Attribute("allElements","boolean","All elements",default=False))
        self.add_attribute(BlueprintAttribute("referenceFrame","sima/riflex/ReferenceFrame","Reference frame for local orientation. If no reference frame is given. Orientation is given in global frame of reference",False))
        self.add_attribute(Attribute("rnx","number","Reference vector x component",default=0.0))
        self.add_attribute(Attribute("rny","number","Reference vector y component",default=0.0))
        self.add_attribute(Attribute("rnz","number","Reference vector z component",default=1.0))