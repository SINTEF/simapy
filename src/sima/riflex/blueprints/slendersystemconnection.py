# 
# Generated with SlenderSystemConnectionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .elementreference import ElementReferenceBlueprint
from .nodereference import NodeReferenceBlueprint
from sima.simo.blueprints.bodyslendersystemconnection import BodySlenderSystemConnectionBlueprint

class SlenderSystemConnectionBlueprint(ElementReferenceBlueprint,NodeReferenceBlueprint,BodySlenderSystemConnectionBlueprint):
    """"""

    def __init__(self, name="SlenderSystemConnection", package_path="sima/riflex", description=""):
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
        self.attributes.append(Attribute("nodeNumber","integer","Local node number on actual segment",default=1))
        self.attributes.append(Attribute("allNodes","boolean","All nodes",default=False))
        self.attributes.append(Attribute("allEnds","boolean","All ends",default=False))
        self.attributes.append(EnumAttribute("elementEnd","sima/riflex/End","End number 1 or 2"))
        self.attributes.append(EnumAttribute("location","sima/riflex/BodyLocation","If a supernode is used as location option and it is not part of a line, a dummy line will be created automatically."))
        self.attributes.append(BlueprintAttribute("superNode","sima/riflex/SuperNode","Line",False))
        self.attributes.append(Attribute("artificialStiffness","boolean","Artificial stiffness option",default=False))
        self.attributes.append(Attribute("stx","number","Stiffness in global X-direction",default=0.0))
        self.attributes.append(Attribute("sty","number","Stiffness in global Y-direction",default=0.0))
        self.attributes.append(Attribute("stz","number","Stiffness in global Z-direction",default=0.0))
        self.attributes.append(Attribute("srx","number","Stiffness around global X-direction",default=0.0))
        self.attributes.append(Attribute("sry","number","Stiffness around global Y-direction",default=0.0))
        self.attributes.append(Attribute("srz","number","Stiffness around global Z-direction",default=0.0))
        self.attributes.append(EnumAttribute("constraint","sima/riflex/NodeConstraint","Supernode type."))
        self.attributes.append(BlueprintAttribute("finalPosition","sima/sima/Position","",True))