# 
# Generated with FlexJointConnectorTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .nodalcomponenttype import NodalComponentTypeBlueprint

class FlexJointConnectorTypeBlueprint(NodalComponentTypeBlueprint):
    """"""

    def __init__(self, name="FlexJointConnectorType", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("mass","number","Mass",default=0.0))
        self.add_attribute(Attribute("volume","number","Displacement volume",default=0.0))
        self.add_attribute(Attribute("gyrationRadiusX","number","Radius of gyration around local x-axis",default=0.0))
        self.add_attribute(Attribute("gyrationRadiusY","number","Radius of gyration around local y-axis",default=0.0))
        self.add_attribute(Attribute("gyrationRadiusZ","number","Radius of gyration around local z-axis",default=0.0))
        self.add_attribute(Attribute("dampingRotX","number","Damping coeff. Rotational velocity around local x-axis",default=0.0))
        self.add_attribute(Attribute("dampingRotY","number","Damping coeff. Rotational velocity around local y-axis",default=0.0))
        self.add_attribute(Attribute("dampingRotZ","number","Damping coeff. Rotational velocity around local z-axis",default=0.0))
        self.add_attribute(Attribute("dragX","number","Drag force coefficient in X-direction",default=0.0))
        self.add_attribute(Attribute("dragY","number","Drag force coefficient in Y-direction",default=0.0))
        self.add_attribute(Attribute("dragZ","number","Drag force coefficient in Z-direction",default=0.0))
        self.add_attribute(Attribute("addedMassX","number","Added mass in X-direction",default=0.0))
        self.add_attribute(Attribute("addedMassY","number","Added mass in Y-direction",default=0.0))
        self.add_attribute(Attribute("addedMassZ","number","Added mass in Z-direction",default=0.0))
        self.add_attribute(Attribute("addedMassRotX","number","Added mass rotation around local x-axis",default=0.0))
        self.add_attribute(Attribute("addedMassRotY","number","Added mass rotation around local y-axis",default=0.0))
        self.add_attribute(Attribute("addedMassRotZ","number","Added mass rotation around local z-axis",default=0.0))
        self.add_attribute(EnumAttribute("stiffnessTypeRotX","sima/riflex/RotationalStiffnessType","Rotational stiffnes type - local x-axis."))
        self.add_attribute(EnumAttribute("stiffnessTypeRotY","sima/riflex/RotationalStiffnessType","Rotational stiffnes type - local z-axis."))
        self.add_attribute(EnumAttribute("stiffnessTypeRotZ","sima/riflex/RotationalStiffnessType","Rotational stiffnes type - local z-axis."))
        self.add_attribute(Attribute("stiffnessDampingCoeffX","number","Stiffness proportional damping coefficient.",default=0.0))
        self.add_attribute(Attribute("stiffnessDampingCoeffY","number","Stiffness proportional damping coefficient.",default=0.0))
        self.add_attribute(Attribute("stiffnessDampingCoeffZ","number","Stiffness proportional damping coefficient.",default=0.0))
        self.add_attribute(Attribute("linearStiffnessRotX","number","Stiffness with respect to x-axis rotation",default=0.0))
        self.add_attribute(Attribute("linearStiffnessRotY","number","Stiffness with respect to y-axis rotation",default=0.0))
        self.add_attribute(Attribute("linearStiffnessRotZ","number","Stiffness with respect to z-axis rotation",default=0.0))
        self.add_attribute(Attribute("yzStiffnessSymmetry","boolean","Same stiffnes for y and z axis?",default=False))
        self.add_attribute(BlueprintAttribute("stiffnessCharacteristicsRotX","sima/riflex/RotationalStiffnessItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stiffnessCharacteristicsRotY","sima/riflex/RotationalStiffnessItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stiffnessCharacteristicsRotZ","sima/riflex/RotationalStiffnessItem","",True,Dimension("*")))