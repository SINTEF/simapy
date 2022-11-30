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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("segment","integer","Segment on given line",default=1))
        self.add_attribute(Attribute("allSegments","boolean","All segments",default=False))
        self.add_attribute(Attribute("elementNumber","integer","Local element number on actual segment",default=1))
        self.add_attribute(Attribute("allElements","boolean","All elements",default=False))
        self.add_attribute(Attribute("nodeNumber","integer","Local node number on actual segment",default=1))
        self.add_attribute(Attribute("allNodes","boolean","All nodes",default=False))
        self.add_attribute(Attribute("allEnds","boolean","All ends",default=False))
        self.add_attribute(EnumAttribute("elementEnd","sima/riflex/End","End number 1 or 2"))
        self.add_attribute(Attribute("name","string","",default='connection'))
        self.add_attribute(EnumAttribute("location","sima/riflex/BodyLocation","If a supernode is used as location option and it is not part of a line, a dummy line will be created automatically."))
        self.add_attribute(BlueprintAttribute("superNode","sima/riflex/SuperNode","Line",False))
        self.add_attribute(Attribute("artificialStiffness","boolean","Artificial stiffness option",default=False))
        self.add_attribute(Attribute("stx","number","Stiffness in global X-direction",default=0.0))
        self.add_attribute(Attribute("sty","number","Stiffness in global Y-direction",default=0.0))
        self.add_attribute(Attribute("stz","number","Stiffness in global Z-direction",default=0.0))
        self.add_attribute(Attribute("srx","number","Stiffness around global X-direction",default=0.0))
        self.add_attribute(Attribute("sry","number","Stiffness around global Y-direction",default=0.0))
        self.add_attribute(Attribute("srz","number","Stiffness around global Z-direction",default=0.0))
        self.add_attribute(EnumAttribute("constraint","sima/riflex/NodeConstraint","Supernode type."))
        self.add_attribute(BlueprintAttribute("finalPosition","sima/sima/Position","",True))