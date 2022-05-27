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
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(EnumAttribute("lineTension","sima/simo/KalmanLineTension","Flag for measurement of line tensions to be included in the controller"))
        self.attributes.append(EnumAttribute("estimationMethod","sima/simo/KalmanEstimationMethod","Estimation method flag"))
        self.attributes.append(Attribute("wfStartingPeriod","number","Starting period for wave frequency estimation",default=0.0))
        self.attributes.append(Attribute("nominalVelocity","number","Nominal velocity, used when linearizing nonlinear damping forces",default=0.25))
        self.attributes.append(BlueprintAttribute("lineCharacteristicItems","sima/simo/LineCharacteristicItem","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("hawserForceMeasurements","sima/simo/HawserForceMeasurement","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("stiffnessMatrix","sima/hydro/Matrix3","",True))
        self.attributes.append(BlueprintAttribute("lines","sima/simo/LineMeasurementItem","",True,Dimension("*")))