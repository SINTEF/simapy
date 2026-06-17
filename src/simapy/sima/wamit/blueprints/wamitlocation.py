# 
# Generated with WamitLocationBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.namedobject import NamedObjectBlueprint

class WamitLocationBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="WamitLocation", package_path="sima/wamit", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(BlueprintAttribute("initialViewpoint","sima/sima/InitialViewpoint","",True))
        self.add_attribute(BlueprintAttribute("viewpoints","sima/sima/NamedViewpoint","",True,Dimension("*")))
        self.add_attribute(Attribute("relativeCompassAngle","number","This is the relative angle measured from the global x-axis to the compass North, measured counter-clockwise",default=0.0))
        self.add_attribute(BlueprintAttribute("infrastructureBodies","sima/sima/InfrastructureBody","",True,Dimension("*")))
        self.add_attribute(Attribute("waterDepth","number","Water depth for kinematics",default=1000.0))
        self.add_attribute(BlueprintAttribute("seaSurface","sima/wamit/SeaSurface","",True))
        self.add_attribute(BlueprintAttribute("physicalConstants","sima/wamit/PhysicalConstants","",True))