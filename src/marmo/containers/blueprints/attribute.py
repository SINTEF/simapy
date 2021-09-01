# Represents a key/value entry
# Generated with AttributeBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute

class AttributeBlueprint(Blueprint):
    """Represents a key/value entry"""

    def __init__(self, name="Attribute", package_path="marmo/containers", description="Represents a key/value entry"):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string",""))
        self.attributes.append(Attribute("description","string",""))
        self.attributes.append(Attribute("value","string",""))