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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("mass","number","Mass",default=0.0))
        self.attributes.append(Attribute("volume","number","Displacement volume",default=0.0))
        self.attributes.append(Attribute("gyrationRadiusX","number","Radius of gyration around local x-axis",default=0.0))
        self.attributes.append(Attribute("gyrationRadiusY","number","Radius of gyration around local y-axis",default=0.0))
        self.attributes.append(Attribute("gyrationRadiusZ","number","Radius of gyration around local z-axis",default=0.0))
        self.attributes.append(Attribute("dampingRotX","number","Damping coeff. Rotational velocity around local x-axis",default=0.0))
        self.attributes.append(Attribute("dampingRotY","number","Damping coeff. Rotational velocity around local y-axis",default=0.0))
        self.attributes.append(Attribute("dampingRotZ","number","Damping coeff. Rotational velocity around local z-axis",default=0.0))
        self.attributes.append(Attribute("dragX","number","Drag force coefficient in X-direction",default=0.0))
        self.attributes.append(Attribute("dragY","number","Drag force coefficient in Y-direction",default=0.0))
        self.attributes.append(Attribute("dragZ","number","Drag force coefficient in Z-direction",default=0.0))
        self.attributes.append(Attribute("addedMassX","number","Added mass in X-direction",default=0.0))
        self.attributes.append(Attribute("addedMassY","number","Added mass in Y-direction",default=0.0))
        self.attributes.append(Attribute("addedMassZ","number","Added mass in Z-direction",default=0.0))
        self.attributes.append(Attribute("addedMassRotX","number","Added mass rotation around local x-axis",default=0.0))
        self.attributes.append(Attribute("addedMassRotY","number","Added mass rotation around local y-axis",default=0.0))
        self.attributes.append(Attribute("addedMassRotZ","number","Added mass rotation around local z-axis",default=0.0))
        self.attributes.append(EnumAttribute("stiffnessTypeRotX","sima/riflex/RotationalStiffnessType","Rotational stiffnes type - local x-axis."))
        self.attributes.append(EnumAttribute("stiffnessTypeRotY","sima/riflex/RotationalStiffnessType","Rotational stiffnes type - local z-axis."))
        self.attributes.append(EnumAttribute("stiffnessTypeRotZ","sima/riflex/RotationalStiffnessType","Rotational stiffnes type - local z-axis."))
        self.attributes.append(Attribute("stiffnessDampingCoeffX","number","Stiffness proportional damping coefficient.",default=0.0))
        self.attributes.append(Attribute("stiffnessDampingCoeffY","number","Stiffness proportional damping coefficient.",default=0.0))
        self.attributes.append(Attribute("stiffnessDampingCoeffZ","number","Stiffness proportional damping coefficient.",default=0.0))
        self.attributes.append(Attribute("linearStiffnessRotX","number","Stiffness with respect to x-axis rotation",default=0.0))
        self.attributes.append(Attribute("linearStiffnessRotY","number","Stiffness with respect to y-axis rotation",default=0.0))
        self.attributes.append(Attribute("linearStiffnessRotZ","number","Stiffness with respect to z-axis rotation",default=0.0))
        self.attributes.append(Attribute("yzStiffnessSymmetry","boolean","Same stiffnes for y and z axis?",default=False))
        self.attributes.append(BlueprintAttribute("stiffnessCharacteristicsRotX","sima/riflex/RotationalStiffnessItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("stiffnessCharacteristicsRotY","sima/riflex/RotationalStiffnessItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("stiffnessCharacteristicsRotZ","sima/riflex/RotationalStiffnessItem","",True,Dimension("*")))