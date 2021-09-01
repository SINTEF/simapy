# 
# Generated with ExternalWrappingTypeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ExternalWrappingTypeBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="ExternalWrappingType", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("mass","number","Mass per unit length",default=0.0))
        self.attributes.append(Attribute("buoyancy","number","Buoyancy volume/length",default=0.0))
        self.attributes.append(Attribute("gyrationRadius","number","Radius of gyration around x-axis",default=0.0))
        self.attributes.append(Attribute("coveredFraction","number","Fraction of the segment that is covered. 0 < FRAC < 1.0.",default=0.0))
        self.attributes.append(Attribute("wrappingItemLength","number","Length of wrapping item. Only used for graphics.",default=1.0))
        self.attributes.append(Attribute("tangentialDrag","number","Drag force coefficient in tangential direction",default=0.0))
        self.attributes.append(Attribute("normalDrag","number","Drag force coefficient in normal direction",default=0.0))
        self.attributes.append(Attribute("tangentialAddedMass","number","Added mass per length in tangential direction",default=0.0))
        self.attributes.append(Attribute("normalAddedMass","number","Added mass per length in normal direction",default=0.0))
        self.attributes.append(Attribute("tangentialLinearDrag","number","Linear drag force coefficients in tangential direction",default=0.0))
        self.attributes.append(Attribute("normalLinearDrag","number","Linear drag force coefficients in tangential direction",default=0.0))