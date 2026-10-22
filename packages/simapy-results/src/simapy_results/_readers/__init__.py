"""Format readers. Importing this package registers them.

Each reader ports the matching importer in SIMA and is keyed on the manifest's
``type`` string.
"""

from . import hdf5  # noqa: F401  -- registers the HDF5 reader for h5/hdf5/b5
from . import mpf  # noqa: F401  -- registers the MatrixPlot reader
from . import psc  # noqa: F401  -- registers the SIMO static results reader for psc.lis
from . import riflex_storage  # noqa: F401  -- registers the RIFLEX bin/asc storage reader
from . import signals_json  # noqa: F401  -- registers the JSON reader

__all__ = ["hdf5", "mpf", "psc", "riflex_storage", "signals_json"]
