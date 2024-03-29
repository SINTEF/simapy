# This an autogenerated file
# 
# Generated with TimeDomainVIVLoadCoefficients
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.timedomainvivloadcoefficients import TimeDomainVIVLoadCoefficientsBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .vivloadformulation import VIVLoadFormulation

class TimeDomainVIVLoadCoefficients(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    vivLoadFormulation : VIVLoadFormulation
    cv : float
         Vortex shedding load coefficient for cross-flow excitation (nondimensional)(default 0.0)
    fnull : float
         Natural cross-flow vortex shedding frequency (nondimensional)(default 0.0)
    fmin : float
         Minimum cross-flow vortex shedding frequency (nondimensional)(default 0.0)
    fmax : float
         Maximum cross-flow vortex shedding frequency (nondimensional)(default 0.0)
    nmem : int
         Number of time steps used in calculation of standard deviation(default 500)
    cvil : float
         Load coefficient for in-line excitation(default 0.0)
    chh : float
         Higher harmonic load coefficient (nondimensional)(default 0.0)
    fnullil : float
         Natural in-line vortex shedding frequency (nondimensional)(default 0.0)
    fminil : float
         Minimum in-line vortex shedding frequency (nondimensional)(default 0.0)
    fmaxil : float
         Maximum in-line vortex shedding frequency (nondimensional)(default 0.0)
    """

    def __init__(self , description="", vivLoadFormulation=VIVLoadFormulation.CROSSFLOW_VIV_ONLY, cv=0.0, fnull=0.0, fmin=0.0, fmax=0.0, nmem=500, cvil=0.0, chh=0.0, fnullil=0.0, fminil=0.0, fmaxil=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.vivLoadFormulation = vivLoadFormulation
        self.cv = cv
        self.fnull = fnull
        self.fmin = fmin
        self.fmax = fmax
        self.nmem = nmem
        self.cvil = cvil
        self.chh = chh
        self.fnullil = fnullil
        self.fminil = fminil
        self.fmaxil = fmaxil
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TimeDomainVIVLoadCoefficientsBlueprint()


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
    def vivLoadFormulation(self) -> VIVLoadFormulation:
        """"""
        return self.__vivLoadFormulation

    @vivLoadFormulation.setter
    def vivLoadFormulation(self, value: VIVLoadFormulation):
        """Set vivLoadFormulation"""
        self.__vivLoadFormulation = value

    @property
    def cv(self) -> float:
        """Vortex shedding load coefficient for cross-flow excitation (nondimensional)"""
        return self.__cv

    @cv.setter
    def cv(self, value: float):
        """Set cv"""
        self.__cv = float(value)

    @property
    def fnull(self) -> float:
        """Natural cross-flow vortex shedding frequency (nondimensional)"""
        return self.__fnull

    @fnull.setter
    def fnull(self, value: float):
        """Set fnull"""
        self.__fnull = float(value)

    @property
    def fmin(self) -> float:
        """Minimum cross-flow vortex shedding frequency (nondimensional)"""
        return self.__fmin

    @fmin.setter
    def fmin(self, value: float):
        """Set fmin"""
        self.__fmin = float(value)

    @property
    def fmax(self) -> float:
        """Maximum cross-flow vortex shedding frequency (nondimensional)"""
        return self.__fmax

    @fmax.setter
    def fmax(self, value: float):
        """Set fmax"""
        self.__fmax = float(value)

    @property
    def nmem(self) -> int:
        """Number of time steps used in calculation of standard deviation"""
        return self.__nmem

    @nmem.setter
    def nmem(self, value: int):
        """Set nmem"""
        self.__nmem = int(value)

    @property
    def cvil(self) -> float:
        """Load coefficient for in-line excitation"""
        return self.__cvil

    @cvil.setter
    def cvil(self, value: float):
        """Set cvil"""
        self.__cvil = float(value)

    @property
    def chh(self) -> float:
        """Higher harmonic load coefficient (nondimensional)"""
        return self.__chh

    @chh.setter
    def chh(self, value: float):
        """Set chh"""
        self.__chh = float(value)

    @property
    def fnullil(self) -> float:
        """Natural in-line vortex shedding frequency (nondimensional)"""
        return self.__fnullil

    @fnullil.setter
    def fnullil(self, value: float):
        """Set fnullil"""
        self.__fnullil = float(value)

    @property
    def fminil(self) -> float:
        """Minimum in-line vortex shedding frequency (nondimensional)"""
        return self.__fminil

    @fminil.setter
    def fminil(self, value: float):
        """Set fminil"""
        self.__fminil = float(value)

    @property
    def fmaxil(self) -> float:
        """Maximum in-line vortex shedding frequency (nondimensional)"""
        return self.__fmaxil

    @fmaxil.setter
    def fmaxil(self, value: float):
        """Set fmaxil"""
        self.__fmaxil = float(value)
