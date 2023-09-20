# This an autogenerated file
# 
# Generated with Kalman
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.kalman import KalmanBlueprint
from typing import Dict
from ..hydro import Matrix3
from ..sima import ScriptableValue
from .estimator import Estimator
from .hawserforcemeasurement import HawserForceMeasurement
from .kalmanestimationmethod import KalmanEstimationMethod
from .kalmanlinetension import KalmanLineTension
from .linecharacteristicitem import LineCharacteristicItem
from .linemeasurementitem import LineMeasurementItem

class Kalman(Estimator):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    lineTension : KalmanLineTension
         Flag for measurement of line tensions to be included in the controller
    estimationMethod : KalmanEstimationMethod
         Estimation method flag
    wfStartingPeriod : float
         Starting period for wave frequency estimation(default 0.0)
    nominalVelocity : float
         Nominal velocity, used when linearizing nonlinear damping forces(default 0.25)
    lineCharacteristicItems : List[LineCharacteristicItem]
    hawserForceMeasurements : List[HawserForceMeasurement]
    stiffnessMatrix : Matrix3
    lines : List[LineMeasurementItem]
    """

    def __init__(self , description="", lineTension=KalmanLineTension.NONE, estimationMethod=KalmanEstimationMethod.FORCE, wfStartingPeriod=0.0, nominalVelocity=0.25, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.lineTension = lineTension
        self.estimationMethod = estimationMethod
        self.wfStartingPeriod = wfStartingPeriod
        self.nominalVelocity = nominalVelocity
        self.lineCharacteristicItems = list()
        self.hawserForceMeasurements = list()
        self.stiffnessMatrix = None
        self.lines = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return KalmanBlueprint()


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
    def lineTension(self) -> KalmanLineTension:
        """Flag for measurement of line tensions to be included in the controller"""
        return self.__lineTension

    @lineTension.setter
    def lineTension(self, value: KalmanLineTension):
        """Set lineTension"""
        self.__lineTension = value

    @property
    def estimationMethod(self) -> KalmanEstimationMethod:
        """Estimation method flag"""
        return self.__estimationMethod

    @estimationMethod.setter
    def estimationMethod(self, value: KalmanEstimationMethod):
        """Set estimationMethod"""
        self.__estimationMethod = value

    @property
    def wfStartingPeriod(self) -> float:
        """Starting period for wave frequency estimation"""
        return self.__wfStartingPeriod

    @wfStartingPeriod.setter
    def wfStartingPeriod(self, value: float):
        """Set wfStartingPeriod"""
        self.__wfStartingPeriod = float(value)

    @property
    def nominalVelocity(self) -> float:
        """Nominal velocity, used when linearizing nonlinear damping forces"""
        return self.__nominalVelocity

    @nominalVelocity.setter
    def nominalVelocity(self, value: float):
        """Set nominalVelocity"""
        self.__nominalVelocity = float(value)

    @property
    def lineCharacteristicItems(self) -> List[LineCharacteristicItem]:
        """"""
        return self.__lineCharacteristicItems

    @lineCharacteristicItems.setter
    def lineCharacteristicItems(self, value: List[LineCharacteristicItem]):
        """Set lineCharacteristicItems"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__lineCharacteristicItems = value

    @property
    def hawserForceMeasurements(self) -> List[HawserForceMeasurement]:
        """"""
        return self.__hawserForceMeasurements

    @hawserForceMeasurements.setter
    def hawserForceMeasurements(self, value: List[HawserForceMeasurement]):
        """Set hawserForceMeasurements"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__hawserForceMeasurements = value

    @property
    def stiffnessMatrix(self) -> Matrix3:
        """"""
        return self.__stiffnessMatrix

    @stiffnessMatrix.setter
    def stiffnessMatrix(self, value: Matrix3):
        """Set stiffnessMatrix"""
        self.__stiffnessMatrix = value

    @property
    def lines(self) -> List[LineMeasurementItem]:
        """"""
        return self.__lines

    @lines.setter
    def lines(self, value: List[LineMeasurementItem]):
        """Set lines"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__lines = value