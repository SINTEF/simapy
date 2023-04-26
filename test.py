from os import path
from pathlib import Path
from marmo import containers
from simapy.sima_reader import SIMAReader

file = Path(".") / "src/tests/resources/result.s5"
contents = SIMAReader().read(file)
print(contents)