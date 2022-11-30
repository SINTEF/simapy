# 
# Generated with IrregularWaveProcedureBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class IrregularWaveProcedureBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="IrregularWaveProcedure", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("kinematicsPosition","sima/riflex/KinematicsPositions","Kinematic positions"))
        self.add_attribute(EnumAttribute("kinematicsInWaveZone","sima/riflex/KinematicsInWaveZone","Type of kinematics in wave zone"))
        self.add_attribute(Attribute("defaultProcedureOn","boolean","If chosen the default kinematics points procedure is run in RIFLEX. If not chosen the default procedure is not run in RIFLEX. In both cases additional detailed specification of wave kinematics points are run if present.",default=True))
        self.add_attribute(Attribute("nodeStep","integer","Wave kinematics is calculated for every 'Node Step' node between Z Lower\nand Z Upper",default=1))
        self.add_attribute(Attribute("zLower","number","Z-coordinate indicating lowest node position for which wave kinematics are calculated",default=0.0))
        self.add_attribute(Attribute("zUpper","number","Upper limit for wave kinematics",default=0.0))
        self.add_attribute(Attribute("applyDiffractedWaves","boolean","Whether diffracted wave points are to be specified",default=False))
        self.add_attribute(BlueprintAttribute("waveKinematicDiffPoints","sima/riflex/WaveKinematicsDiffPoint","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("waveKinematicNodePoints","sima/riflex/WaveKinematicsNodePoint","",True,Dimension("*")))
        self.add_attribute(Attribute("waveKinematicsFile","boolean","Whether wave kinematics time series should be read from file or not",default=False))
        self.add_attribute(Attribute("waveKinematicsFileName","string","Reference to a wave kinematics file"))
        self.add_attribute(BlueprintAttribute("waveKinematicsTimeSeriesReferences","sima/riflex/WaveKinematicsTimeSeriesReference","",True,Dimension("*")))
        self.add_attribute(Attribute("waveKinematicsMaxColumns","integer","Maximum number of columns in the wave kinematics time series file",default=0))
        self.add_attribute(Attribute("waveKinematicsTimeColumn","integer","Column number for time in the wave kinematics time series file",default=0))
        self.add_attribute(Attribute("waveKinematicsStorage","boolean","Wave kinematics storage indicator",default=False))
        self.add_attribute(EnumAttribute("fileFormat","sima/riflex/StorageType",""))