# 
# Generated with PositioningElementBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class PositioningElementBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="PositioningElement", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("localPoint","sima/sima/Point3","",True))
        self.attributes.append(BlueprintAttribute("globalPoint","sima/sima/Point3","",True))
        self.attributes.append(EnumAttribute("failureMode","sima/simo/ActivationFailureMode","Failure mode:\n - No failure\n - Failure by exceeding the breaking strength after specified time\n - Activation of element after specified time if absolute value of force is below breaking strength"))
        self.attributes.append(Attribute("failureTime","number","Earliest possible time of failure",default=0.0))
        self.attributes.append(Attribute("breakingStrength","number","Breaking strength",default=0.0))