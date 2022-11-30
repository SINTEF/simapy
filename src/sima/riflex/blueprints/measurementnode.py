# 
# Generated with MeasurementNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .nodereference import NodeReferenceBlueprint

class MeasurementNodeBlueprint(NodeReferenceBlueprint):
    """"""

    def __init__(self, name="MeasurementNode", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.add_attribute(Attribute("segment","integer","Segment on given line",default=1))
        self.add_attribute(Attribute("allSegments","boolean","All segments",default=False))
        self.add_attribute(Attribute("nodeNumber","integer","Local node number on actual segment",default=1))
        self.add_attribute(Attribute("allNodes","boolean","All nodes",default=False))
        self.add_attribute(EnumAttribute("system","sima/riflex/NodeSystem",""))