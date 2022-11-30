# This an autogenerated file
# 
# Generated with ThinWalledPipeMaterial
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.thinwalledpipematerial import ThinWalledPipeMaterialBlueprint
from typing import Dict
from sima.riflex.materialmodel import MaterialModel
from sima.riflex.strainstressitem import StrainStressItem
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ThinWalledPipeMaterial(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    materialModel : MaterialModel
         Type of material model.
    elasticityModulus : float
         Modulus of elasticity(default 0.0)
    shearModulus : float
         Shear modulus(default 0.0)
    yieldStress : float
         Yield stress(default 0.0)
    strainStressCurveRise : float
         Rise of strain-stress curve for plastic region.(default 0.0)
    materialHardening : float
         Hardening parameter for material.(default 1.0)
    numIntegrationPoints : int
         Number of integration points along circumference.(default 16)
    strainStressCharacteristics : List[StrainStressItem]
         Strain-stress curve.
    """

    def __init__(self , description="", materialModel=MaterialModel.LINEAR_MATERIAL, elasticityModulus=0.0, shearModulus=0.0, yieldStress=0.0, strainStressCurveRise=0.0, materialHardening=1.0, numIntegrationPoints=16, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.materialModel = materialModel
        self.elasticityModulus = elasticityModulus
        self.shearModulus = shearModulus
        self.yieldStress = yieldStress
        self.strainStressCurveRise = strainStressCurveRise
        self.materialHardening = materialHardening
        self.numIntegrationPoints = numIntegrationPoints
        self.strainStressCharacteristics = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ThinWalledPipeMaterialBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def materialModel(self) -> MaterialModel:
        """Type of material model."""
        return self.__materialModel

    @materialModel.setter
    def materialModel(self, value: MaterialModel):
        """Set materialModel"""
        self.__materialModel = value

    @property
    def elasticityModulus(self) -> float:
        """Modulus of elasticity"""
        return self.__elasticityModulus

    @elasticityModulus.setter
    def elasticityModulus(self, value: float):
        """Set elasticityModulus"""
        self.__elasticityModulus = float(value)

    @property
    def shearModulus(self) -> float:
        """Shear modulus"""
        return self.__shearModulus

    @shearModulus.setter
    def shearModulus(self, value: float):
        """Set shearModulus"""
        self.__shearModulus = float(value)

    @property
    def yieldStress(self) -> float:
        """Yield stress"""
        return self.__yieldStress

    @yieldStress.setter
    def yieldStress(self, value: float):
        """Set yieldStress"""
        self.__yieldStress = float(value)

    @property
    def strainStressCurveRise(self) -> float:
        """Rise of strain-stress curve for plastic region."""
        return self.__strainStressCurveRise

    @strainStressCurveRise.setter
    def strainStressCurveRise(self, value: float):
        """Set strainStressCurveRise"""
        self.__strainStressCurveRise = float(value)

    @property
    def materialHardening(self) -> float:
        """Hardening parameter for material."""
        return self.__materialHardening

    @materialHardening.setter
    def materialHardening(self, value: float):
        """Set materialHardening"""
        self.__materialHardening = float(value)

    @property
    def numIntegrationPoints(self) -> int:
        """Number of integration points along circumference."""
        return self.__numIntegrationPoints

    @numIntegrationPoints.setter
    def numIntegrationPoints(self, value: int):
        """Set numIntegrationPoints"""
        self.__numIntegrationPoints = int(value)

    @property
    def strainStressCharacteristics(self) -> List[StrainStressItem]:
        """Strain-stress curve."""
        return self.__strainStressCharacteristics

    @strainStressCharacteristics.setter
    def strainStressCharacteristics(self, value: List[StrainStressItem]):
        """Set strainStressCharacteristics"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__strainStressCharacteristics = value
