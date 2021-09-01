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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("superNodes","sima/riflex/SuperNode","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("lines","sima/riflex/ARLine","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("lineTypes","sima/riflex/ARLineType","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("crossSections","sima/riflex/CrossSection","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("mainRiserLines","sima/riflex/MainRiserLine","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("externalWrappings","sima/riflex/ExternalWrappingType","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("ballJointConnectors","sima/riflex/BallJointConnectorType","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("flexJointConnectors","sima/riflex/FlexJointConnectorType","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("nodalBodies","sima/riflex/NodalBodyType","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("internalFluids","sima/riflex/InternalFluidType","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("pipeInPipeContacts","sima/riflex/PipeInPipeContact","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("winches","sima/riflex/ARWinch","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("elasticContactSurfaces","sima/riflex/ElasticContactSurface","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("tensioners","sima/riflex/Tensioner","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("rollerContacts","sima/riflex/RollerContact","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("tubularContacts","sima/riflex/TubularContact","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("globalSprings","sima/riflex/GlobalSpring","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("windTurbines","sima/riflex/WindTurbine","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("localElementAxes","sima/riflex/LocalElementAxis","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("dragChains","sima/riflex/DragChainType","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("geotechnicalSprings","sima/riflex/GeotechnicalSpring","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("seafloorContactComponents","sima/riflex/SeafloorContact","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("seafloorContactSpecification","sima/riflex/SeafloorContactSpecification","",True))
        self.attributes.append(BlueprintAttribute("materials","sima/riflex/Material","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("geotechnicals","sima/riflex/GeoTechnical","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("geotechnicalLineSpecification","sima/riflex/GeotechnicalLineSpecification","",True))
        self.attributes.append(BlueprintAttribute("marineGrowthItems","sima/riflex/MarineGrowth","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("soilLayerProfiles","sima/riflex/SoilLayerProfile","",True,Dimension("size","")))
        self.attributes.append(BlueprintAttribute("soilTypes","sima/riflex/SoilType","",True,Dimension("size","")))