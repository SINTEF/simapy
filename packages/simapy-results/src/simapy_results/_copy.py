"""Copying a condition's results out of the workspace that produced them."""

from __future__ import annotations

import shutil
from pathlib import Path

from ._readers.psc import MAPPER_FILENAME
from ._readers.riflex_storage import SUFFIXES, storage_key
from ._riflexres import RIFLEX_MAPPER_FILENAME
from ._scan import ID_MAP_FILENAME, RESULTS_FILENAME, _directories_of, _read_manifest, is_result

#: Not results, but a copy without them reads back with hashed names.
READ_BESIDE_RESULTS = (ID_MAP_FILENAME, RIFLEX_MAPPER_FILENAME, MAPPER_FILENAME)


def copy_results(condition: str | Path, destination: str | Path) -> None:
    """Copy each directory ``results.json`` names, at the same relative path.

    SIMA's own copy flattens the timestamp folder away, which breaks those paths.
    """
    condition, destination = Path(condition), Path(destination)
    content = _read_manifest(condition / RESULTS_FILENAME) or {}
    described = [content, *(m for m in content.get("conditions", []) if isinstance(m, dict))]
    folders = {path for entry in described
               for path in _directories_of(entry.get("directories")).values()}
    for folder in sorted(folders):
        source = condition / folder
        if not source.is_dir():
            continue
        target = destination / folder
        target.mkdir(parents=True, exist_ok=True)
        for file in source.iterdir():
            if is_result(file) or file.name in READ_BESIDE_RESULTS:
                shutil.copy2(file, target / file.name)
                if file.suffix.lower() in SUFFIXES:
                    shutil.copy2(storage_key(file), target / storage_key(file).name)
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copy2(condition / RESULTS_FILENAME, destination / RESULTS_FILENAME)
