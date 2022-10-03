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
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.attributes.append(Attribute("segment","integer","Segment on given line",default=1))
        self.attributes.append(Attribute("allSegments","boolean","All segments",default=False))
        self.attributes.append(Attribute("elementNumber","integer","Local element number on actual segment",default=1))
        self.attributes.append(Attribute("allElements","boolean","All elements",default=False))
        self.attributes.append(BlueprintAttribute("referenceFrame","sima/riflex/ReferenceFrame","Reference frame for local orientation. If no reference frame is given. Orientation is given in global frame of reference",False))
        self.attributes.append(Attribute("rnx","number","Reference vector x component",default=0.0))
        self.attributes.append(Attribute("rny","number","Reference vector y component",default=0.0))
        self.attributes.append(Attribute("rnz","number","Reference vector z component",default=1.0))