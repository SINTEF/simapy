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
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("baseFileName","string","",default='sima'))
        self.add_attribute(Attribute("alphaEpsilon","number","Spectrum scale parameter",default=0.0))
        self.add_attribute(Attribute("lengthScale","number","Length scale",default=0.0))
        self.add_attribute(Attribute("gamma","number","Shear distortion parameter",default=3.9))
        self.add_attribute(Attribute("seed","integer","Start seed for random number generator",default=0))
        self.add_attribute(Attribute("gridPointsX","integer","Grid points in X-direction (Power of 2)",default=0))
        self.add_attribute(Attribute("gridPointsY","integer","Grid points in Y-direction (Power of 2)",default=0))
        self.add_attribute(Attribute("gridPointsZ","integer","Grid points in Z-direction (Power of 2)",default=0))
        self.add_attribute(Attribute("pointDistanceX","number","Distance between grid points in X direction",default=0.0))
        self.add_attribute(Attribute("pointDistanceY","number","Distance between grid points in Y direction",default=0.0))
        self.add_attribute(Attribute("pointDistanceZ","number","Distance between grid points in Z direction",default=0.0))
        self.add_attribute(Attribute("hfCompensation","boolean","High Frequency Compensation",default=True))
        self.add_attribute(Attribute("turbulenceIntensity","number","Turbulence intensity",default=0.0))
        self.add_attribute(Attribute("meanWindSpeed","number","Mean wind speed",default=0.0))
        self.add_attribute(Attribute("transient","number","Starting point in simulation used for calculation of scaling factor",default=0.0))
        self.add_attribute(EnumAttribute("inputFormat","sima/windturbine/MannInputFormat",""))
        self.add_attribute(Attribute("windSeriesDuration","number","Length of simulation",default=0.0))
        self.add_attribute(Attribute("gridWidth","number","Domain size in Y-direction",default=0.0))
        self.add_attribute(Attribute("gridHeight","number","Domain size in Z-direction",default=0.0))
        self.add_attribute(Attribute("lengthFactor","number","",default=0.8))
        self.add_attribute(Attribute("longTurbScaleParam","number","Longitudenal Turbulence Scale Parameter",default=0.0))