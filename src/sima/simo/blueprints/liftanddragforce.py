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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("point","sima/sima/Point3","",True))
        self.attributes.append(Attribute("maxAngle","number","Maximum rudder angle",default=0.0))
        self.attributes.append(Attribute("maxAngleVelocity","number","Maximum velocity of rudder angle",default=0.0))
        self.attributes.append(Attribute("lengthZ","number","Length in z-direction",default=0.0))
        self.attributes.append(Attribute("lengthX","number","Length in x-direction",default=0.0))
        self.attributes.append(BlueprintAttribute("vectorZ","sima/sima/Vector3","",True))
        self.attributes.append(BlueprintAttribute("vectorXZ","sima/sima/Vector3","",True))
        self.attributes.append(Attribute("angle","number","Rudder angle",default=0.0))
        self.attributes.append(Attribute("currentFactor","number","Factor that current velocity is multiplied with",default=0.0))
        self.attributes.append(Attribute("vesselFactor","number","Factor that vessel velocity is multiplied with",default=0.0))
        self.attributes.append(Attribute("thrusterFactor","number","Factor that thruster induced velocity is multiplied with",default=0.0))
        self.attributes.append(Attribute("dragZ","number","Quadratic force coefficient in rudder z-direction",default=0.0))
        self.attributes.append(BlueprintAttribute("items","sima/simo/LiftAndDragForceCharacteristicItem","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("interpolation","sima/simo/LiftAndDragInterpolation","Interpolation method"))
        self.attributes.append(Attribute("symmetric","boolean","Symmetry about x-axis",default=False))