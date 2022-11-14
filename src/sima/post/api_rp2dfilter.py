# This an autogenerated file
# 
# Generated with API_RP2DFilter
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.api_rp2dfilter import API_RP2DFilterBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.fabricationfactor import FabricationFactor
from sima.post.inputslot import InputSlot
from sima.post.internalpressuredesignfactor import InternalPressureDesignFactor
from sima.post.limitstatecategory import LimitStateCategory
from sima.post.operationnode import OperationNode
from sima.post.outputslot import OutputSlot
from sima.post.pipetype import PipeType
from sima.sima.scriptablevalue import ScriptableValue

class API_RP2DFilter(OperationNode):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    _id : str
         (default None)
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    x : int
         (default 0)
    y : int
         (default 0)
    h : int
         (default 0)
    w : int
         (default 0)
    controlSignalInputSlots : List[ControlSignalInputSlot]
    filterInputSlots : List[InputSlot]
    filterOutputSlots : List[OutputSlot]
    nomOD : float
         Nominal outside diameter(default 0.0)
    pipeThickness : float
         Thickness of pipe(default 0.0)
    yieldStrength : float
         Specified minimum yield strength of the pipe(default 500000000.0)
    youngsFactor : float
         Young's modulus(default 210000000000.0)
    poissonsRatio : float
         Poisson's ratio for pipe wall material(default 0.3)
    fabricationFactor : FabricationFactor
         Absolute value of the negative tolerance taken from the material standard/specification of the pipe
    ultimateStrength : float
         Specified minimum ultimate strength of the pipe(default 700000000.0)
    ovality : float
         Ovality(default 0.0025)
    pipeVariability : float
         Parameter to account for variability in pipe mechanical properties and wall thickness(default 0.45)
    minInternalPressure : float
         Minimum internal presssure used in collapse check(default 0.0)
    maxInternalPressure : float
         Maximum internal presssure used in burst check(default 5000000.0)
    pipeType : PipeType
         Load factor for accidental loads
    extFluidDensity : float
         External fluid density(default 1024.0)
    accelerationOfGravity : float
         Acceleration of gravity(default 9.81)
    limitStateCategory : LimitStateCategory
    internalPressureDesignFactor : InternalPressureDesignFactor
         Internal pressure design factor
    """

    def __init__(self , description="", _id=None, name=None, x=0, y=0, h=0, w=0, nomOD=0.0, pipeThickness=0.0, yieldStrength=500000000.0, youngsFactor=210000000000.0, poissonsRatio=0.3, fabricationFactor=FabricationFactor.SEAMLESSPIPE, ultimateStrength=700000000.0, ovality=0.0025, pipeVariability=0.45, minInternalPressure=0.0, maxInternalPressure=5000000.0, pipeType=PipeType.COLD_EXPANDED, extFluidDensity=1024.0, accelerationOfGravity=9.81, limitStateCategory=LimitStateCategory.SLS, internalPressureDesignFactor=InternalPressureDesignFactor.DESIGN_PRESSURE, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.filterInputSlots = list()
        self.filterOutputSlots = list()
        self.nomOD = nomOD
        self.pipeThickness = pipeThickness
        self.yieldStrength = yieldStrength
        self.youngsFactor = youngsFactor
        self.poissonsRatio = poissonsRatio
        self.fabricationFactor = fabricationFactor
        self.ultimateStrength = ultimateStrength
        self.ovality = ovality
        self.pipeVariability = pipeVariability
        self.minInternalPressure = minInternalPressure
        self.maxInternalPressure = maxInternalPressure
        self.pipeType = pipeType
        self.extFluidDensity = extFluidDensity
        self.accelerationOfGravity = accelerationOfGravity
        self.limitStateCategory = limitStateCategory
        self.internalPressureDesignFactor = internalPressureDesignFactor
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return API_RP2DFilterBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def x(self) -> int:
        """"""
        return self.__x

    @x.setter
    def x(self, value: int):
        """Set x"""
        self.__x = int(value)

    @property
    def y(self) -> int:
        """"""
        return self.__y

    @y.setter
    def y(self, value: int):
        """Set y"""
        self.__y = int(value)

    @property
    def h(self) -> int:
        """"""
        return self.__h

    @h.setter
    def h(self, value: int):
        """Set h"""
        self.__h = int(value)

    @property
    def w(self) -> int:
        """"""
        return self.__w

    @w.setter
    def w(self, value: int):
        """Set w"""
        self.__w = int(value)

    @property
    def controlSignalInputSlots(self) -> List[ControlSignalInputSlot]:
        """"""
        return self.__controlSignalInputSlots

    @controlSignalInputSlots.setter
    def controlSignalInputSlots(self, value: List[ControlSignalInputSlot]):
        """Set controlSignalInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__controlSignalInputSlots = value

    @property
    def filterInputSlots(self) -> List[InputSlot]:
        """"""
        return self.__filterInputSlots

    @filterInputSlots.setter
    def filterInputSlots(self, value: List[InputSlot]):
        """Set filterInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__filterInputSlots = value

    @property
    def filterOutputSlots(self) -> List[OutputSlot]:
        """"""
        return self.__filterOutputSlots

    @filterOutputSlots.setter
    def filterOutputSlots(self, value: List[OutputSlot]):
        """Set filterOutputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__filterOutputSlots = value

    @property
    def nomOD(self) -> float:
        """Nominal outside diameter"""
        return self.__nomOD

    @nomOD.setter
    def nomOD(self, value: float):
        """Set nomOD"""
        self.__nomOD = float(value)

    @property
    def pipeThickness(self) -> float:
        """Thickness of pipe"""
        return self.__pipeThickness

    @pipeThickness.setter
    def pipeThickness(self, value: float):
        """Set pipeThickness"""
        self.__pipeThickness = float(value)

    @property
    def yieldStrength(self) -> float:
        """Specified minimum yield strength of the pipe"""
        return self.__yieldStrength

    @yieldStrength.setter
    def yieldStrength(self, value: float):
        """Set yieldStrength"""
        self.__yieldStrength = float(value)

    @property
    def youngsFactor(self) -> float:
        """Young's modulus"""
        return self.__youngsFactor

    @youngsFactor.setter
    def youngsFactor(self, value: float):
        """Set youngsFactor"""
        self.__youngsFactor = float(value)

    @property
    def poissonsRatio(self) -> float:
        """Poisson's ratio for pipe wall material"""
        return self.__poissonsRatio

    @poissonsRatio.setter
    def poissonsRatio(self, value: float):
        """Set poissonsRatio"""
        self.__poissonsRatio = float(value)

    @property
    def fabricationFactor(self) -> FabricationFactor:
        """Absolute value of the negative tolerance taken from the material standard/specification of the pipe"""
        return self.__fabricationFactor

    @fabricationFactor.setter
    def fabricationFactor(self, value: FabricationFactor):
        """Set fabricationFactor"""
        self.__fabricationFactor = value

    @property
    def ultimateStrength(self) -> float:
        """Specified minimum ultimate strength of the pipe"""
        return self.__ultimateStrength

    @ultimateStrength.setter
    def ultimateStrength(self, value: float):
        """Set ultimateStrength"""
        self.__ultimateStrength = float(value)

    @property
    def ovality(self) -> float:
        """Ovality"""
        return self.__ovality

    @ovality.setter
    def ovality(self, value: float):
        """Set ovality"""
        self.__ovality = float(value)

    @property
    def pipeVariability(self) -> float:
        """Parameter to account for variability in pipe mechanical properties and wall thickness"""
        return self.__pipeVariability

    @pipeVariability.setter
    def pipeVariability(self, value: float):
        """Set pipeVariability"""
        self.__pipeVariability = float(value)

    @property
    def minInternalPressure(self) -> float:
        """Minimum internal presssure used in collapse check"""
        return self.__minInternalPressure

    @minInternalPressure.setter
    def minInternalPressure(self, value: float):
        """Set minInternalPressure"""
        self.__minInternalPressure = float(value)

    @property
    def maxInternalPressure(self) -> float:
        """Maximum internal presssure used in burst check"""
        return self.__maxInternalPressure

    @maxInternalPressure.setter
    def maxInternalPressure(self, value: float):
        """Set maxInternalPressure"""
        self.__maxInternalPressure = float(value)

    @property
    def pipeType(self) -> PipeType:
        """Load factor for accidental loads"""
        return self.__pipeType

    @pipeType.setter
    def pipeType(self, value: PipeType):
        """Set pipeType"""
        self.__pipeType = value

    @property
    def extFluidDensity(self) -> float:
        """External fluid density"""
        return self.__extFluidDensity

    @extFluidDensity.setter
    def extFluidDensity(self, value: float):
        """Set extFluidDensity"""
        self.__extFluidDensity = float(value)

    @property
    def accelerationOfGravity(self) -> float:
        """Acceleration of gravity"""
        return self.__accelerationOfGravity

    @accelerationOfGravity.setter
    def accelerationOfGravity(self, value: float):
        """Set accelerationOfGravity"""
        self.__accelerationOfGravity = float(value)

    @property
    def limitStateCategory(self) -> LimitStateCategory:
        """"""
        return self.__limitStateCategory

    @limitStateCategory.setter
    def limitStateCategory(self, value: LimitStateCategory):
        """Set limitStateCategory"""
        self.__limitStateCategory = value

    @property
    def internalPressureDesignFactor(self) -> InternalPressureDesignFactor:
        """Internal pressure design factor"""
        return self.__internalPressureDesignFactor

    @internalPressureDesignFactor.setter
    def internalPressureDesignFactor(self, value: InternalPressureDesignFactor):
        """Set internalPressureDesignFactor"""
        self.__internalPressureDesignFactor = value
