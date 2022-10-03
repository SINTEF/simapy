# 
# Generated with BallJointConnectorTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .nodalcomponenttype import NodalComponentTypeBlueprint

class BallJointConnectorTypeBlueprint(NodalComponentTypeBlueprint):
    """"""

    def __init__(self, name="BallJointConnectorType", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("mass","number","Mass",default=0.0))
        self.attributes.append(Attribute("volume","number","Displacement volume",default=0.0))
        self.attributes.append(EnumAttribute("referenceFrame","sima/simo/ReferenceFrameType","Reference frame"))
        self.attributes.append(Attribute("dragX","number","Drag force coefficient in X-direction",default=0.0))
        self.attributes.append(Attribute("dragY","number","Drag force coefficient in Y-direction",default=0.0))
        self.attributes.append(Attribute("dragZ","number","Drag force coefficient in Z-direction",default=0.0))
        self.attributes.append(Attribute("addedMassX","number","Added mass in X-direction",default=0.0))
        self.attributes.append(Attribute("addedMassY","number","Added mass in Y-direction",default=0.0))
        self.attributes.append(Attribute("addedMassZ","number","Added mass in Z-direction",default=0.0))
        self.attributes.append(EnumAttribute("boundaryRotX","sima/riflex/BoundaryCondition","Rotation freedom code, x-axis."))
        self.attributes.append(EnumAttribute("boundaryRotY","sima/riflex/BoundaryCondition","Rotation freedom code, y-axis."))
        self.attributes.append(EnumAttribute("boundaryRotZ","sima/riflex/BoundaryCondition","Rotation freedom code, z-axis."))