# This an autogenerated file
# 
# Generated with CommonSoilType
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.commonsoiltype import CommonSoilTypeBlueprint
from typing import Dict
from sima.riflex.commonsoilcoefficients import CommonSoilCoefficients
from sima.riflex.soiltype import SoilType
from sima.sima.scriptablevalue import ScriptableValue

class CommonSoilType(SoilType):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    requiredResolution : int
         Required resolution of soil reaction curves(default 50)
    pvDamping : float
         (default 0.0)
    mtDamping : float
         (default 0.0)
    baseShearLoadDamping : float
         (default 0.0)
    baseMomentDamping : float
         (default 0.0)
    lateralDisplacementForce : CommonSoilCoefficients
    inPlaneMomentRotation : CommonSoilCoefficients
    baseShearLoad : CommonSoilCoefficients
    baseMoment : CommonSoilCoefficients
    """

    def __init__(self , name="", description="", _id="", requiredResolution=50, pvDamping=0.0, mtDamping=0.0, baseShearLoadDamping=0.0, baseMomentDamping=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.requiredResolution = requiredResolution
        self.pvDamping = pvDamping
        self.mtDamping = mtDamping
        self.baseShearLoadDamping = baseShearLoadDamping
        self.baseMomentDamping = baseMomentDamping
        self.lateralDisplacementForce = None
        self.inPlaneMomentRotation = None
        self.baseShearLoad = None
        self.baseMoment = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CommonSoilTypeBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def requiredResolution(self) -> int:
        """Required resolution of soil reaction curves"""
        return self.__requiredResolution

    @requiredResolution.setter
    def requiredResolution(self, value: int):
        """Set requiredResolution"""
        self.__requiredResolution = int(value)

    @property
    def pvDamping(self) -> float:
        """"""
        return self.__pvDamping

    @pvDamping.setter
    def pvDamping(self, value: float):
        """Set pvDamping"""
        self.__pvDamping = float(value)

    @property
    def mtDamping(self) -> float:
        """"""
        return self.__mtDamping

    @mtDamping.setter
    def mtDamping(self, value: float):
        """Set mtDamping"""
        self.__mtDamping = float(value)

    @property
    def baseShearLoadDamping(self) -> float:
        """"""
        return self.__baseShearLoadDamping

    @baseShearLoadDamping.setter
    def baseShearLoadDamping(self, value: float):
        """Set baseShearLoadDamping"""
        self.__baseShearLoadDamping = float(value)

    @property
    def baseMomentDamping(self) -> float:
        """"""
        return self.__baseMomentDamping

    @baseMomentDamping.setter
    def baseMomentDamping(self, value: float):
        """Set baseMomentDamping"""
        self.__baseMomentDamping = float(value)

    @property
    def lateralDisplacementForce(self) -> CommonSoilCoefficients:
        """"""
        return self.__lateralDisplacementForce

    @lateralDisplacementForce.setter
    def lateralDisplacementForce(self, value: CommonSoilCoefficients):
        """Set lateralDisplacementForce"""
        self.__lateralDisplacementForce = value

    @property
    def inPlaneMomentRotation(self) -> CommonSoilCoefficients:
        """"""
        return self.__inPlaneMomentRotation

    @inPlaneMomentRotation.setter
    def inPlaneMomentRotation(self, value: CommonSoilCoefficients):
        """Set inPlaneMomentRotation"""
        self.__inPlaneMomentRotation = value

    @property
    def baseShearLoad(self) -> CommonSoilCoefficients:
        """"""
        return self.__baseShearLoad

    @baseShearLoad.setter
    def baseShearLoad(self, value: CommonSoilCoefficients):
        """Set baseShearLoad"""
        self.__baseShearLoad = value

    @property
    def baseMoment(self) -> CommonSoilCoefficients:
        """"""
        return self.__baseMoment

    @baseMoment.setter
    def baseMoment(self, value: CommonSoilCoefficients):
        """Set baseMoment"""
        self.__baseMoment = value
