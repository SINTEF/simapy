# 
# Generated with LiftAndDragForceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class LiftAndDragForceBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="LiftAndDragForce", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("point","sima/sima/Point3","",True))
        self.add_attribute(Attribute("maxAngle","number","Maximum rudder angle",default=0.0))
        self.add_attribute(Attribute("maxAngleVelocity","number","Maximum velocity of rudder angle",default=0.0))
        self.add_attribute(Attribute("lengthZ","number","Length in z-direction",default=0.0))
        self.add_attribute(Attribute("lengthX","number","Length in x-direction",default=0.0))
        self.add_attribute(BlueprintAttribute("vectorZ","sima/sima/Vector3","",True))
        self.add_attribute(BlueprintAttribute("vectorXZ","sima/sima/Vector3","",True))
        self.add_attribute(Attribute("angle","number","Rudder angle",default=0.0))
        self.add_attribute(Attribute("currentFactor","number","Factor that current velocity is multiplied with",default=0.0))
        self.add_attribute(Attribute("vesselFactor","number","Factor that vessel velocity is multiplied with",default=0.0))
        self.add_attribute(Attribute("thrusterFactor","number","Factor that thruster induced velocity is multiplied with",default=0.0))
        self.add_attribute(Attribute("dragZ","number","Quadratic force coefficient in rudder z-direction",default=0.0))
        self.add_attribute(BlueprintAttribute("items","sima/simo/LiftAndDragForceCharacteristicItem","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("interpolation","sima/simo/LiftAndDragInterpolation","Interpolation method"))
        self.add_attribute(Attribute("symmetric","boolean","Symmetry about x-axis",default=False))