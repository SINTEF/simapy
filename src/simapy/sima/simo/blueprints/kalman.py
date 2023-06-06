# 
# Generated with KalmanBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .estimator import EstimatorBlueprint

class KalmanBlueprint(EstimatorBlueprint):
    """"""

    def __init__(self, name="Kalman", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(EnumAttribute("lineTension","sima/simo/KalmanLineTension","Flag for measurement of line tensions to be included in the controller"))
        self.add_attribute(EnumAttribute("estimationMethod","sima/simo/KalmanEstimationMethod","Estimation method flag"))
        self.add_attribute(Attribute("wfStartingPeriod","number","Starting period for wave frequency estimation",default=0.0))
        self.add_attribute(Attribute("nominalVelocity","number","Nominal velocity, used when linearizing nonlinear damping forces",default=0.25))
        self.add_attribute(BlueprintAttribute("lineCharacteristicItems","sima/simo/LineCharacteristicItem","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("hawserForceMeasurements","sima/simo/HawserForceMeasurement","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("stiffnessMatrix","sima/hydro/Matrix3","",True))
        self.add_attribute(BlueprintAttribute("lines","sima/simo/LineMeasurementItem","",True,Dimension("*")))