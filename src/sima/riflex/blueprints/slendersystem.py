# 
# Generated with SlenderSystemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class SlenderSystemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="SlenderSystem", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("superNodes","sima/riflex/SuperNode","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("lines","sima/riflex/ARLine","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("lineTypes","sima/riflex/ARLineType","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("crossSections","sima/riflex/CrossSection","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("mainRiserLines","sima/riflex/MainRiserLine","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("externalWrappings","sima/riflex/ExternalWrappingType","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("ballJointConnectors","sima/riflex/BallJointConnectorType","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("flexJointConnectors","sima/riflex/FlexJointConnectorType","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("nodalBodies","sima/riflex/NodalBodyType","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("internalFluids","sima/riflex/InternalFluidType","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("pipeInPipeContacts","sima/riflex/PipeInPipeContact","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("winches","sima/riflex/ARWinch","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("elasticContactSurfaces","sima/riflex/ElasticContactSurface","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("tensioners","sima/riflex/Tensioner","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("rollerContacts","sima/riflex/RollerContact","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("tubularContacts","sima/riflex/TubularContact","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("globalSprings","sima/riflex/GlobalSpring","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("windTurbines","sima/riflex/WindTurbine","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("localElementAxes","sima/riflex/LocalElementAxis","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("dragChains","sima/riflex/DragChainType","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("geotechnicalSprings","sima/riflex/GeotechnicalSpring","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("seafloorContactComponents","sima/riflex/SeafloorContact","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("seafloorContactSpecification","sima/riflex/SeafloorContactSpecification","",True))
        self.add_attribute(BlueprintAttribute("materials","sima/riflex/Material","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("geotechnicals","sima/riflex/GeoTechnical","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("geotechnicalLineSpecification","sima/riflex/GeotechnicalLineSpecification","",True))
        self.add_attribute(BlueprintAttribute("marineGrowthItems","sima/riflex/MarineGrowth","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("soilLayerProfiles","sima/riflex/SoilLayerProfile","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("soilTypes","sima/riflex/SoilType","",True,Dimension("*")))