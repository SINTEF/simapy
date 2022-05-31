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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("x","integer","",default=0))
        self.attributes.append(Attribute("y","integer","",default=0))
        self.attributes.append(Attribute("h","integer","",default=0))
        self.attributes.append(Attribute("w","integer","",default=0))
        self.attributes.append(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.attributes.append(Attribute("nomOD","number","Nominal outside diameter",default=0.0))
        self.attributes.append(Attribute("pipeThickness","number","Thickness of pipe",default=0.0))
        self.attributes.append(Attribute("yieldStrength","number","Specified minimum yield strength of the pipe",default=500000000.0))
        self.attributes.append(Attribute("youngsFactor","number","Young's modulus",default=210000000000.0))
        self.attributes.append(Attribute("poissonsRatio","number","Poisson's ratio for pipe wall material",default=0.3))
        self.attributes.append(EnumAttribute("fabricationFactor","sima/post/FabricationFactor","Absolute value of the negative tolerance taken from the material standard/specification of the pipe"))
        self.attributes.append(Attribute("ultimateStrength","number","Specified minimum ultimate strength of the pipe",default=700000000.0))
        self.attributes.append(Attribute("ovality","number","Ovality",default=0.0025))
        self.attributes.append(Attribute("pipeVariability","number","Parameter to account for variability in pipe mechanical properties and wall thickness",default=0.45))
        self.attributes.append(Attribute("minInternalPressure","number","Minimum internal presssure used in collapse check",default=0.0))
        self.attributes.append(Attribute("maxInternalPressure","number","Maximum internal presssure used in burst check",default=5000000.0))
        self.attributes.append(EnumAttribute("pipeType","sima/post/PipeType","Load factor for accidental loads"))
        self.attributes.append(Attribute("extFluidDensity","number","External fluid density",default=1024.0))
        self.attributes.append(Attribute("accelerationOfGravity","number","Acceleration of gravity",default=9.81))
        self.attributes.append(EnumAttribute("limitStateCategory","sima/post/LimitStateCategory",""))
        self.attributes.append(EnumAttribute("internalPressureDesignFactor","sima/post/InternalPressureDesignFactor","Internal pressure design factor"))