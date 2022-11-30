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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("tag","string",""))
        self.add_attribute(Attribute("x","number","x position in body local coordinate system",default=0.0))
        self.add_attribute(Attribute("y","number","y position in body local coordinate system",default=0.0))
        self.add_attribute(Attribute("z","number","z position in body local coordinate system",default=0.0))
        self.add_attribute(Attribute("volumeTolerance","number","Precision that should be reached by volume computation",default=0.001))
        self.add_attribute(Attribute("permeabilityFactor","number","Fraction of the tank volume that can be used to fill it with ballast fluid",default=1.0))
        self.add_attribute(Attribute("initialBallastQuantity","number","Initial ballast quantity.",default=0.0))
        self.add_attribute(EnumAttribute("quantityType","sima/simo/BallastQuantityType",""))
        self.add_attribute(Attribute("ballastFluidDensity","number","Density of the fluid used as ballast",default=1025.0))
        self.add_attribute(BlueprintAttribute("geometryPosition","sima/sima/Position","",True))
        self.add_attribute(Attribute("geometryFile","string","Geometry definition file ( STL or GDF)"))
        self.add_attribute(EnumAttribute("state","sima/simo/BallastTankState","State of ballast tank"))