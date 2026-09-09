## Metocean

Demonstrates use of metocean data to create input to Metocean Task in SIMA

We use python libraries developed in [SFIBlues](https://sfiblues.no/) to collect metocean data from metocean data providers such as the [Norwegian Meteorological Institute](https://www.met.no/en)

See [metocean-api](https://metocean-api.readthedocs.io) and [metocean-stats](https://metocean-stats.readthedocs.io)

The generated h5/json files can be imported into the SIMA Metocan Task and then be used in further analyses

Right click Metocean Task in SIMA and choose "import metocean data", then select the generated file to import

The following requirements are needed to run the examples

pip install -r requirements-metocean.txt