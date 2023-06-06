# 
# Generated with API_RP2DFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class API_RP2DFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="API_RP2DFilter", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("nomOD","number","Nominal outside diameter",default=0.0))
        self.add_attribute(Attribute("pipeThickness","number","Thickness of pipe",default=0.0))
        self.add_attribute(Attribute("yieldStrength","number","Specified minimum yield strength of the pipe",default=500000000.0))
        self.add_attribute(Attribute("youngsFactor","number","Young's modulus",default=210000000000.0))
        self.add_attribute(Attribute("poissonsRatio","number","Poisson's ratio for pipe wall material",default=0.3))
        self.add_attribute(EnumAttribute("fabricationFactor","sima/post/FabricationFactor","Absolute value of the negative tolerance taken from the material standard/specification of the pipe"))
        self.add_attribute(Attribute("ultimateStrength","number","Specified minimum ultimate strength of the pipe",default=700000000.0))
        self.add_attribute(Attribute("ovality","number","Ovality",default=0.0025))
        self.add_attribute(Attribute("pipeVariability","number","Parameter to account for variability in pipe mechanical properties and wall thickness",default=0.45))
        self.add_attribute(Attribute("minInternalPressure","number","Minimum internal presssure used in collapse check",default=0.0))
        self.add_attribute(Attribute("maxInternalPressure","number","Maximum internal presssure used in burst check",default=5000000.0))
        self.add_attribute(EnumAttribute("pipeType","sima/post/PipeType","Load factor for accidental loads"))
        self.add_attribute(Attribute("extFluidDensity","number","External fluid density",default=1024.0))
        self.add_attribute(Attribute("accelerationOfGravity","number","Acceleration of gravity",default=9.81))
        self.add_attribute(EnumAttribute("limitStateCategory","sima/post/LimitStateCategory",""))
        self.add_attribute(EnumAttribute("internalPressureDesignFactor","sima/post/InternalPressureDesignFactor","Internal pressure design factor"))