# This an autogenerated file
# 
# Generated with SlenderSystem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.slendersystem import SlenderSystemBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .arline import ARLine
from .arlinetype import ARLineType
from .arwinch import ARWinch
from .balljointconnectortype import BallJointConnectorType
from .crosssection import CrossSection
from .dragchaintype import DragChainType
from .elasticcontactsurface import ElasticContactSurface
from .externalwrappingtype import ExternalWrappingType
from .flexjointconnectortype import FlexJointConnectorType
from .geotechnical import GeoTechnical
from .geotechnicallinespecification import GeotechnicalLineSpecification
from .geotechnicalspring import GeotechnicalSpring
from .globalspring import GlobalSpring
from .internalfluidtype import InternalFluidType
from .localelementaxis import LocalElementAxis
from .mainriserline import MainRiserLine
from .marinegrowth import MarineGrowth
from .material import Material
from .nodalbodytype import NodalBodyType
from .pipeinpipecontact import PipeInPipeContact
from .rollercontact import RollerContact
from .seafloorcontact import SeafloorContact
from .seafloorcontactspecification import SeafloorContactSpecification
from .soillayerprofile import SoilLayerProfile
from .soiltype import SoilType
from .supernode import SuperNode
from .tensioner import Tensioner
from .tubularcontact import TubularContact
from .userdefinedelement import UserdefinedElement
from .windturbine import WindTurbine

class SlenderSystem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    superNodes : List[SuperNode]
    lines : List[ARLine]
    lineTypes : List[ARLineType]
    crossSections : List[CrossSection]
    mainRiserLines : List[MainRiserLine]
    externalWrappings : List[ExternalWrappingType]
    ballJointConnectors : List[BallJointConnectorType]
    flexJointConnectors : List[FlexJointConnectorType]
    nodalBodies : List[NodalBodyType]
    internalFluids : List[InternalFluidType]
    pipeInPipeContacts : List[PipeInPipeContact]
    winches : List[ARWinch]
    elasticContactSurfaces : List[ElasticContactSurface]
    tensioners : List[Tensioner]
    rollerContacts : List[RollerContact]
    tubularContacts : List[TubularContact]
    globalSprings : List[GlobalSpring]
    windTurbines : List[WindTurbine]
    localElementAxes : List[LocalElementAxis]
    dragChains : List[DragChainType]
    geotechnicalSprings : List[GeotechnicalSpring]
    seafloorContactComponents : List[SeafloorContact]
    seafloorContactSpecification : SeafloorContactSpecification
    materials : List[Material]
    geotechnicals : List[GeoTechnical]
    geotechnicalLineSpecification : GeotechnicalLineSpecification
    marineGrowthItems : List[MarineGrowth]
    soilLayerProfiles : List[SoilLayerProfile]
    soilTypes : List[SoilType]
    userdefinedElements : List[UserdefinedElement]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.superNodes = list()
        self.lines = list()
        self.lineTypes = list()
        self.crossSections = list()
        self.mainRiserLines = list()
        self.externalWrappings = list()
        self.ballJointConnectors = list()
        self.flexJointConnectors = list()
        self.nodalBodies = list()
        self.internalFluids = list()
        self.pipeInPipeContacts = list()
        self.winches = list()
        self.elasticContactSurfaces = list()
        self.tensioners = list()
        self.rollerContacts = list()
        self.tubularContacts = list()
        self.globalSprings = list()
        self.windTurbines = list()
        self.localElementAxes = list()
        self.dragChains = list()
        self.geotechnicalSprings = list()
        self.seafloorContactComponents = list()
        self.seafloorContactSpecification = None
        self.materials = list()
        self.geotechnicals = list()
        self.geotechnicalLineSpecification = None
        self.marineGrowthItems = list()
        self.soilLayerProfiles = list()
        self.soilTypes = list()
        self.userdefinedElements = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SlenderSystemBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def superNodes(self) -> List[SuperNode]:
        """"""
        return self.__superNodes

    @superNodes.setter
    def superNodes(self, value: List[SuperNode]):
        """Set superNodes"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__superNodes = value

    @property
    def lines(self) -> List[ARLine]:
        """"""
        return self.__lines

    @lines.setter
    def lines(self, value: List[ARLine]):
        """Set lines"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__lines = value

    @property
    def lineTypes(self) -> List[ARLineType]:
        """"""
        return self.__lineTypes

    @lineTypes.setter
    def lineTypes(self, value: List[ARLineType]):
        """Set lineTypes"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__lineTypes = value

    @property
    def crossSections(self) -> List[CrossSection]:
        """"""
        return self.__crossSections

    @crossSections.setter
    def crossSections(self, value: List[CrossSection]):
        """Set crossSections"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__crossSections = value

    @property
    def mainRiserLines(self) -> List[MainRiserLine]:
        """"""
        return self.__mainRiserLines

    @mainRiserLines.setter
    def mainRiserLines(self, value: List[MainRiserLine]):
        """Set mainRiserLines"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__mainRiserLines = value

    @property
    def externalWrappings(self) -> List[ExternalWrappingType]:
        """"""
        return self.__externalWrappings

    @externalWrappings.setter
    def externalWrappings(self, value: List[ExternalWrappingType]):
        """Set externalWrappings"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__externalWrappings = value

    @property
    def ballJointConnectors(self) -> List[BallJointConnectorType]:
        """"""
        return self.__ballJointConnectors

    @ballJointConnectors.setter
    def ballJointConnectors(self, value: List[BallJointConnectorType]):
        """Set ballJointConnectors"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__ballJointConnectors = value

    @property
    def flexJointConnectors(self) -> List[FlexJointConnectorType]:
        """"""
        return self.__flexJointConnectors

    @flexJointConnectors.setter
    def flexJointConnectors(self, value: List[FlexJointConnectorType]):
        """Set flexJointConnectors"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__flexJointConnectors = value

    @property
    def nodalBodies(self) -> List[NodalBodyType]:
        """"""
        return self.__nodalBodies

    @nodalBodies.setter
    def nodalBodies(self, value: List[NodalBodyType]):
        """Set nodalBodies"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__nodalBodies = value

    @property
    def internalFluids(self) -> List[InternalFluidType]:
        """"""
        return self.__internalFluids

    @internalFluids.setter
    def internalFluids(self, value: List[InternalFluidType]):
        """Set internalFluids"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__internalFluids = value

    @property
    def pipeInPipeContacts(self) -> List[PipeInPipeContact]:
        """"""
        return self.__pipeInPipeContacts

    @pipeInPipeContacts.setter
    def pipeInPipeContacts(self, value: List[PipeInPipeContact]):
        """Set pipeInPipeContacts"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__pipeInPipeContacts = value

    @property
    def winches(self) -> List[ARWinch]:
        """"""
        return self.__winches

    @winches.setter
    def winches(self, value: List[ARWinch]):
        """Set winches"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__winches = value

    @property
    def elasticContactSurfaces(self) -> List[ElasticContactSurface]:
        """"""
        return self.__elasticContactSurfaces

    @elasticContactSurfaces.setter
    def elasticContactSurfaces(self, value: List[ElasticContactSurface]):
        """Set elasticContactSurfaces"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__elasticContactSurfaces = value

    @property
    def tensioners(self) -> List[Tensioner]:
        """"""
        return self.__tensioners

    @tensioners.setter
    def tensioners(self, value: List[Tensioner]):
        """Set tensioners"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__tensioners = value

    @property
    def rollerContacts(self) -> List[RollerContact]:
        """"""
        return self.__rollerContacts

    @rollerContacts.setter
    def rollerContacts(self, value: List[RollerContact]):
        """Set rollerContacts"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__rollerContacts = value

    @property
    def tubularContacts(self) -> List[TubularContact]:
        """"""
        return self.__tubularContacts

    @tubularContacts.setter
    def tubularContacts(self, value: List[TubularContact]):
        """Set tubularContacts"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__tubularContacts = value

    @property
    def globalSprings(self) -> List[GlobalSpring]:
        """"""
        return self.__globalSprings

    @globalSprings.setter
    def globalSprings(self, value: List[GlobalSpring]):
        """Set globalSprings"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__globalSprings = value

    @property
    def windTurbines(self) -> List[WindTurbine]:
        """"""
        return self.__windTurbines

    @windTurbines.setter
    def windTurbines(self, value: List[WindTurbine]):
        """Set windTurbines"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__windTurbines = value

    @property
    def localElementAxes(self) -> List[LocalElementAxis]:
        """"""
        return self.__localElementAxes

    @localElementAxes.setter
    def localElementAxes(self, value: List[LocalElementAxis]):
        """Set localElementAxes"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__localElementAxes = value

    @property
    def dragChains(self) -> List[DragChainType]:
        """"""
        return self.__dragChains

    @dragChains.setter
    def dragChains(self, value: List[DragChainType]):
        """Set dragChains"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__dragChains = value

    @property
    def geotechnicalSprings(self) -> List[GeotechnicalSpring]:
        """"""
        return self.__geotechnicalSprings

    @geotechnicalSprings.setter
    def geotechnicalSprings(self, value: List[GeotechnicalSpring]):
        """Set geotechnicalSprings"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__geotechnicalSprings = value

    @property
    def seafloorContactComponents(self) -> List[SeafloorContact]:
        """"""
        return self.__seafloorContactComponents

    @seafloorContactComponents.setter
    def seafloorContactComponents(self, value: List[SeafloorContact]):
        """Set seafloorContactComponents"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__seafloorContactComponents = value

    @property
    def seafloorContactSpecification(self) -> SeafloorContactSpecification:
        """"""
        return self.__seafloorContactSpecification

    @seafloorContactSpecification.setter
    def seafloorContactSpecification(self, value: SeafloorContactSpecification):
        """Set seafloorContactSpecification"""
        self.__seafloorContactSpecification = value

    @property
    def materials(self) -> List[Material]:
        """"""
        return self.__materials

    @materials.setter
    def materials(self, value: List[Material]):
        """Set materials"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__materials = value

    @property
    def geotechnicals(self) -> List[GeoTechnical]:
        """"""
        return self.__geotechnicals

    @geotechnicals.setter
    def geotechnicals(self, value: List[GeoTechnical]):
        """Set geotechnicals"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__geotechnicals = value

    @property
    def geotechnicalLineSpecification(self) -> GeotechnicalLineSpecification:
        """"""
        return self.__geotechnicalLineSpecification

    @geotechnicalLineSpecification.setter
    def geotechnicalLineSpecification(self, value: GeotechnicalLineSpecification):
        """Set geotechnicalLineSpecification"""
        self.__geotechnicalLineSpecification = value

    @property
    def marineGrowthItems(self) -> List[MarineGrowth]:
        """"""
        return self.__marineGrowthItems

    @marineGrowthItems.setter
    def marineGrowthItems(self, value: List[MarineGrowth]):
        """Set marineGrowthItems"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__marineGrowthItems = value

    @property
    def soilLayerProfiles(self) -> List[SoilLayerProfile]:
        """"""
        return self.__soilLayerProfiles

    @soilLayerProfiles.setter
    def soilLayerProfiles(self, value: List[SoilLayerProfile]):
        """Set soilLayerProfiles"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__soilLayerProfiles = value

    @property
    def soilTypes(self) -> List[SoilType]:
        """"""
        return self.__soilTypes

    @soilTypes.setter
    def soilTypes(self, value: List[SoilType]):
        """Set soilTypes"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__soilTypes = value

    @property
    def userdefinedElements(self) -> List[UserdefinedElement]:
        """"""
        return self.__userdefinedElements

    @userdefinedElements.setter
    def userdefinedElements(self, value: List[UserdefinedElement]):
        """Set userdefinedElements"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__userdefinedElements = value
