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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("kinematicsPosition","sima/riflex/KinematicsPositions","Kinematic positions"))
        self.attributes.append(EnumAttribute("kinematicsInWaveZone","sima/riflex/KinematicsInWaveZone","Type of kinematics in wave zone"))
        self.attributes.append(Attribute("defaultProcedureOn","boolean","If chosen the default kinematics points procedure is run in RIFLEX. If not chosen the default procedure is not run in RIFLEX. In both cases additional detailed specification of wave kinematics points are run if present.",default=True))
        self.attributes.append(Attribute("nodeStep","integer","Wave kinematics is calculated for every 'Node Step' node between Z Lower\nand Z Upper",default=1))
        self.attributes.append(Attribute("zLower","number","Z-coordinate indicating lowest node position for which wave kinematics are calculated",default=0.0))
        self.attributes.append(Attribute("zUpper","number","Upper limit for wave kinematics",default=0.0))
        self.attributes.append(Attribute("applyDiffractedWaves","boolean","Whether diffracted wave points are to be specified",default=False))
        self.attributes.append(BlueprintAttribute("waveKinematicDiffPoints","sima/riflex/WaveKinematicsDiffPoint","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("waveKinematicNodePoints","sima/riflex/WaveKinematicsNodePoint","",True,Dimension("*")))
        self.attributes.append(Attribute("waveKinematicsFile","boolean","Whether wave kinematics time series should be read from file or not",default=False))
        self.attributes.append(Attribute("waveKinematicsFileName","string","Reference to a wave kinematics file",default=""))
        self.attributes.append(BlueprintAttribute("waveKinematicsTimeSeriesReferences","sima/riflex/WaveKinematicsTimeSeriesReference","",True,Dimension("*")))
        self.attributes.append(Attribute("waveKinematicsMaxColumns","integer","Maximum number of columns in the wave kinematics time series file",default=0))
        self.attributes.append(Attribute("waveKinematicsTimeColumn","integer","Column number for time in the wave kinematics time series file",default=0))
        self.attributes.append(Attribute("waveKinematicsStorage","boolean","Wave kinematics storage indicator",default=False))
        self.attributes.append(EnumAttribute("fileFormat","sima/riflex/StorageType",""))