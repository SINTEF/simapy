# 
# Generated with MannWindGeneratorBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint
from sima.sima.blueprints.conditionselectable import ConditionSelectableBlueprint

class MannWindGeneratorBlueprint(NamedObjectBlueprint,ConditionSelectableBlueprint):
    """"""

    def __init__(self, name="MannWindGenerator", package_path="sima/windturbine", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(Attribute("baseFileName","string","",default='sima'))
        self.attributes.append(Attribute("alphaEpsilon","number","Spectrum scale parameter",default=0.0))
        self.attributes.append(Attribute("lengthScale","number","Length scale",default=0.0))
        self.attributes.append(Attribute("gamma","number","Shear distortion parameter",default=3.9))
        self.attributes.append(Attribute("seed","integer","Start seed for random number generator",default=0))
        self.attributes.append(Attribute("gridPointsX","integer","Grid points in X-direction (Power of 2)",default=0))
        self.attributes.append(Attribute("gridPointsY","integer","Grid points in Y-direction (Power of 2)",default=0))
        self.attributes.append(Attribute("gridPointsZ","integer","Grid points in Z-direction (Power of 2)",default=0))
        self.attributes.append(Attribute("pointDistanceX","number","Distance between grid points in X direction",default=0.0))
        self.attributes.append(Attribute("pointDistanceY","number","Distance between grid points in Y direction",default=0.0))
        self.attributes.append(Attribute("pointDistanceZ","number","Distance between grid points in Z direction",default=0.0))
        self.attributes.append(Attribute("hfCompensation","boolean","High Frequency Compensation",default=True))
        self.attributes.append(Attribute("turbulenceIntensity","number","Turbulence intensity",default=0.0))
        self.attributes.append(Attribute("meanWindSpeed","number","Mean wind speed",default=0.0))
        self.attributes.append(Attribute("transient","number","Starting point in simulation used for calculation of scaling factor",default=0.0))
        self.attributes.append(EnumAttribute("inputFormat","sima/windturbine/MannInputFormat",""))
        self.attributes.append(Attribute("windSeriesDuration","number","Length of simulation",default=0.0))
        self.attributes.append(Attribute("gridWidth","number","Domain size in Y-direction",default=0.0))
        self.attributes.append(Attribute("gridHeight","number","Domain size in Z-direction",default=0.0))
        self.attributes.append(Attribute("lengthFactor","number","",default=0.8))
        self.attributes.append(Attribute("longTurbScaleParam","number","Longitudenal Turbulence Scale Parameter",default=0.0))