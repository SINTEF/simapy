# 
# Generated with GlobalSpringBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .nodereference import NodeReferenceBlueprint
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class GlobalSpringBlueprint(NodeReferenceBlueprint,NamedObjectBlueprint):
    """"""

    def __init__(self, name="GlobalSpring", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("line","sima/riflex/ARLine","Line",False))
        self.attributes.append(Attribute("segment","integer","Segment on given line",default=1))
        self.attributes.append(Attribute("allSegments","boolean","All segments",default=False))
        self.attributes.append(Attribute("nodeNumber","integer","Local node number on actual segment",default=1))
        self.attributes.append(Attribute("allNodes","boolean","All nodes",default=False))
        self.attributes.append(EnumAttribute("dof","sima/riflex/SpringDOF","Local degree of freedom."))
        self.attributes.append(Attribute("constantStiffness","boolean","Constant stiffness",default=False))
        self.attributes.append(Attribute("stiffness","number","Constant spring stiffness.",default=0.0))
        self.attributes.append(Attribute("dampingCoefficient","number","Linear damping coefficient.",default=0.0))
        self.attributes.append(Attribute("stiffnessDampingFactor","number","Stiffness proportional damping factor.",default=0.0))
        self.attributes.append(BlueprintAttribute("stiffnessItems","sima/riflex/GlobalSpringStiffnessItem","",True,Dimension("size","")))