# 
# Generated with SuperNodeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint
from sima.simo.blueprints.supernodereference import SuperNodeReferenceBlueprint

class SuperNodeBlueprint(NamedObjectBlueprint,SuperNodeReferenceBlueprint):
    """"""

    def __init__(self, name="SuperNode", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("size","")))
        self.attributes.append(EnumAttribute("constraint","sima/riflex/NodeConstraint","Supernode type."))
        self.attributes.append(BlueprintAttribute("referenceFrame","sima/riflex/ReferenceFrame","Reference frame for local coordinates.",False))
        self.attributes.append(BlueprintAttribute("supportVessel","sima/riflex/SupportVessel","Support body reference.",False))
        self.attributes.append(Attribute("automaticInitialPosition","boolean","Initial position calculated using stress free reference line length, stress free coordinate of the other super node and static coordinates of both super nodes.",default=False))
        self.attributes.append(BlueprintAttribute("masterNode","sima/simo/SuperNodeReference","Master node for Slaved / Fixed Relative Orientation nodes.",False))
        self.attributes.append(EnumAttribute("xConstraint","sima/riflex/BoundaryCondition","Boundary condition for translation in X-direction."))
        self.attributes.append(EnumAttribute("yConstraint","sima/riflex/BoundaryCondition","Boundary condition for translation in Y-direction."))
        self.attributes.append(EnumAttribute("zConstraint","sima/riflex/BoundaryCondition","Boundary condition for translation in Z-direction."))
        self.attributes.append(EnumAttribute("rxConstraint","sima/riflex/BoundaryCondition","Boundary condition for rotation about X-axis"))
        self.attributes.append(EnumAttribute("ryConstraint","sima/riflex/BoundaryCondition","Boundary condition for rotation about Y-axis"))
        self.attributes.append(EnumAttribute("rzConstraint","sima/riflex/BoundaryCondition","Boundary condition for rotation about Z-axis"))
        self.attributes.append(Attribute("xGInitial","number","Initial (stress-free) global coordinate X",default=0.0))
        self.attributes.append(Attribute("yGInitial","number","Initial (stress-free) global coordinate Y",default=0.0))
        self.attributes.append(Attribute("zGInitial","number","Initial (stress-free) global coordinate Z",default=0.0))
        self.attributes.append(Attribute("xGStatic","number","Static global coordinate X",default=0.0))
        self.attributes.append(Attribute("yGStatic","number","Static global coordinate Y",default=0.0))
        self.attributes.append(Attribute("zGStatic","number","Static global coordinate Z",default=0.0))
        self.attributes.append(Attribute("rotation","number","Specified rotation of supernode from stress free position \nto static equilibrium position.",default=0.0))
        self.attributes.append(Attribute("direction","number","Direction of axis for specified rotation.",default=0.0))
        self.attributes.append(BlueprintAttribute("referenceLine","sima/riflex/ARLine","Used for automatic calculation of initial super node position",False))
        self.attributes.append(Attribute("beta","number","Direction to horisontal if set. Rotation is about 'local y-axis' i.e. positive downwards.",default=0.0))
        self.attributes.append(Attribute("radial","boolean","Used to define the supernode position relative to \nthe x axis spanned by the reference supernodes",default=False))
        self.attributes.append(BlueprintAttribute("radialReference1","sima/riflex/SuperNode","Master node for Slaved / Fixed Relative Orientation nodes.",False))
        self.attributes.append(BlueprintAttribute("radialReference2","sima/riflex/SuperNode","Master node for Slaved / Fixed Relative Orientation nodes.",False))
        self.attributes.append(Attribute("radialAngle","number","",default=0.0))
        self.attributes.append(Attribute("verticalOffset","number","",default=0.0))
        self.attributes.append(Attribute("radialDistance","number","",default=0.0))
        self.attributes.append(EnumAttribute("boundaryConditionFrame","sima/riflex/BoundaryConditionFrame","Boundary condition reference co-ordinate system"))
        self.attributes.append(Attribute("xx","number","Skew x-axis x-component in reference system",default=0.0))
        self.attributes.append(Attribute("xy","number","Skew x-axis y-component in reference system",default=0.0))
        self.attributes.append(Attribute("xz","number","Skew x-axis z-component in reference system",default=0.0))
        self.attributes.append(Attribute("xp","number","XY-plane reference vector x-component  in reference system",default=0.0))
        self.attributes.append(Attribute("yp","number","XY-plane reference vector y-component  in reference system",default=0.0))
        self.attributes.append(Attribute("zp","number","XY-plane reference vector z-component  in reference system",default=0.0))