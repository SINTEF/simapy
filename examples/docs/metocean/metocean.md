# Metocean

Creates input for the SIMA Metocean task from metocean data.

The examples use [metocean-api](https://metocean-api.readthedocs.io) and
[metocean-stats](https://metocean-stats.readthedocs.io), developed in
[SFI Blues](https://sfiblues.no/), to fetch data from providers such as the
[Norwegian Meteorological Institute](https://www.met.no/en). Install them with:

```bash
pip install -r examples/metocean/requirements-metocean.txt
```

The generated HDF5 or JSON files can be imported into the Metocean task in SIMA:
right-click it, choose "import metocean data", and select the file.
