# 
# Generated with BallastTankBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class BallastTankBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="BallastTank", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("tag","string","",default=""))
        self.attributes.append(Attribute("x","number","x position in body local coordinate system",default=0.0))
        self.attributes.append(Attribute("y","number","y position in body local coordinate system",default=0.0))
        self.attributes.append(Attribute("z","number","z position in body local coordinate system",default=0.0))
        self.attributes.append(Attribute("volumeTolerance","number","Precision that should be reached by volume computation",default=0.001))
        self.attributes.append(Attribute("permeabilityFactor","number","Fraction of the tank volume that can be used to fill it with ballast fluid",default=1.0))
        self.attributes.append(Attribute("initialBallastQuantity","number","Initial ballast quantity.",default=0.0))
        self.attributes.append(EnumAttribute("quantityType","sima/simo/BallastQuantityType",""))
        self.attributes.append(Attribute("ballastFluidDensity","number","Density of the fluid used as ballast",default=1025.0))
        self.attributes.append(BlueprintAttribute("geometryPosition","sima/sima/Position","",True))
        self.attributes.append(Attribute("geometryFile","string","Geometry definition file ( STL or GDF)",default=""))
        self.attributes.append(EnumAttribute("state","sima/simo/BallastTankState","State of ballast tank"))