"""Create a metocean hindcast wave data file for SIMA.

This example demonstrates how to extract wave data from the NORA3 dataset and convert it
into a metocean hindcast format that can be read by SIMA. It focuses on a specific storm
event in Sulafjord, Norway.

Features:
    Data Retrieval:
        Uses metocean_api to extract wave data from the NORA3 dataset
    Wave Parameter Processing:
        Processes wave parameters including significant height, peak period, and direction
    SIMA Integration:
        Converts data to a format compatible with SIMA's metocean module

Requirements:
    - metocean_api for data retrieval
    - simapy.metocean for hindcast data handling
    - xarray for data processing
    - Access to NORA3 wave dataset

Example:
    Basic usage of this script:
    
    >>> python create_hindcast_wave.py
    
    The script generates hindcast files in the output/simamet/ directory.
"""

from pathlib import Path
from datetime import datetime
import time
import numpy as np
import pandas as pd
from dmt.dmt_writer import DMTWriter
from metocean_api import ts
import simapy.metocean.hindcast as hc


def __create_wave(wave_name, hs, tp, direction):
    # NORA3_wave_sub: North East Down, wave_going_to
    # SIMA MET: North East Down, wave coming from
    dir_sima = (180.0 + direction) % 360.0
    return hc.StochasticWave(name=wave_name, hs=hs, tp=tp, direction=dir_sima)


def __create_hindcast(hc_name, product, hc_values: pd.DataFrame, lat_pos, lon_pos):
    waves = []

    waves.append(
        __create_wave("total", hc_values["hs"], hc_values["tp"], hc_values["thq"])
    )
    waves.append(
        __create_wave(
            "windSea", hc_values["hs_sea"], hc_values["tp_sea"], hc_values["thq_sea"]
        )
    )
    waves.append(
        __create_wave(
            "swell",
            hc_values["hs_swell"],
            hc_values["tp_swell"],
            hc_values["thq_swell"],
        )
    )

    # Time is given in Unix epoch
    # convert dates to strings
    dates = hc_values.index
    sdates = np.datetime_as_string(dates, unit="h", timezone="UTC").astype("|S")

    hindcast = hc.Hindcast()
    hindcast.description = f"Collected using Norway MET metocean-api with product {product}"
    hindcast.name = hc_name.replace("-", "_")
    hindcast.date = sdates
    hindcast.latitude = lat_pos
    hindcast.longitude = lon_pos
    hindcast.wave = waves

    return hindcast


def main():
    """Execute the main hindcast example.
    
    Retrieves wave data for a specific storm event in Sulafjord, Norway, and
    converts it to a SIMA-compatible hindcast format. The data is saved as
    both CSV and DMT files for further use in SIMA simulations.
    """
    # https://www.met.no/publikasjoner/met-report  Section Storms in Sulafjord, wind waves and currents
    # https://www.met.no/publikasjoner/met-report/_/attachment/inline/86f02fd2-a979-43ef-a17e-3bdba201e584:c70eb4b6ffe6f3b7b98016f4a0ebfc5ca501c766/MET-report-03-2024.pdf

    # Storm 14th of March 2017
    sd = datetime(2017, 3, 14, 10, 0)
    ed = datetime(2017, 3, 14, 13, 0)

    start_date = sd.strftime("%Y-%m-%d")
    end_date = ed.strftime("%Y-%m-%d")

    positions = {
        "Sulesund": {"lat": 62.402865086109195, "lon": 6.028359996993728},
        "Kvitneset": {"lat": 62.421049661227585, "lon": 6.000482407215768},
        "BuoyA": {"description": "Sulafjorden", "lat": 62.4263, "lon": 6.0447},
        "BuoyB": {"description": "Sulafjorden", "lat": 62.4038, "lon": 6.0806},
        "BuoyD": {"description": "Breisundet", "lat": 62.4464, "lon": 5.9336},
    }

    location = "BuoyB"

    lat_pos = positions[location]["lat"]
    lon_pos = positions[location]["lon"]

    product = "NORA3_wave_sub"

    name = f"hindcast-{location}-{product}-{start_date}-{end_date}"

    output_dir = Path("./output/simamet")
    output_dir.mkdir(exist_ok=True, parents=True)

    csv_file = str(output_dir / f"{name}.csv")

    nc_file = csv_file.replace(".csv", ".nc")

    df_ts = ts.TimeSeries(
        lon=lon_pos,
        lat=lat_pos,
        datafile=nc_file,
        start_time=start_date,
        end_time=end_date,
        product=product,
    )

    # Start timing
    start = time.time()
    df_ts.import_data(save_csv=False, save_nc=True, use_cache=True)

    # End timing and print elapsed time
    end = time.time()
    print("Elapsed time: " + str(end - start) + " seconds")

    values = df_ts.data

    hindcast = __create_hindcast(name,product, values, lat_pos, lon_pos)

    dmtw = DMTWriter()
    output_dir = Path("./output/simamet")
    output_dir.mkdir(exist_ok=True, parents=True)
    print(f"Writing hindcast to {output_dir / name}.dmt")
    dmtw.write(hindcast, output_dir / name)
    print(f"Successfully created hindcast files in {output_dir}")


if __name__ == "__main__":
    main()
