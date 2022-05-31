# 
# Generated with LiftAndDragForceCharacteristicItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class LiftAndDragForceCharacteristicItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="LiftAndDragForceCharacteristicItem", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("velocityDirection","number","Velocity direction relative to rudder x-axis",default=0.0))
        self.attributes.append(Attribute("forceX","number","Quadratic force coefficient in rudder x-direction",default=0.0))
        self.attributes.append(Attribute("forceY","number","Quadratic force coefficient in rudder y-direction",default=0.0))
        self.attributes.append(Attribute("momentZ","number","Quadratic moment coefficient about rudder z-axis",default=0.0))