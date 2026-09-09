"""Read wave data from nora3 and generate metocean hindcast readable from SIMA"""

import time
from pathlib import Path
from datetime import datetime
import numpy as np
import xarray as xr
from dmt.dmt_writer import DMTWriter
from metocean_api import ts
import simapy.metocean.hindcast as hc


def __create_hindcast(hc_name, hc_values, lat_pos, lon_pos):
    # Time is given in Unix epoch
    # convert dates to strings
    dates = hc_values["time"].astype("datetime64[s]")
    sdates = np.datetime_as_string(dates, unit="h", timezone="UTC").astype("|S")

    hindcast = hc.Hindcast()
    hindcast.name = hc_name.replace("-", "_")
    hindcast.date = sdates
    hindcast.latitude = lat_pos
    hindcast.longitude = lon_pos

    speed = hc_values["wind_speed"]
    # Wind direction in fixed heights above surface,wind_from_direction	degrees clockwise from north (meteorological)
    # SIMA: North East Down, wind coming from, same as MET
    direction = hc_values["wind_direction"]
    heights = hc_values["height"]
    winds = []
    for i, height in enumerate(heights):
        wind = hc.StochasticWind()
        level = height.values
        wind.level = level
        wind.name = f"{level}m"
        wind.speed = speed[:, i].values
        wind.direction = direction[:, i].values
        winds.append(wind)

    hindcast.wind = winds
    return hindcast


if __name__ == "__main__":
    # https://www.met.no/publikasjoner/met-report  Section Storms in Sulafjord, wind waves and currents
    # https://www.met.no/publikasjoner/met-report/_/attachment/inline/86f02fd2-a979-43ef-a17e-3bdba201e584:c70eb4b6ffe6f3b7b98016f4a0ebfc5ca501c766/MET-report-03-2024.pdf

    # Storm March 14, 2017
    sd = datetime(2017, 3, 14, 0, 0)
    ed = datetime(2017, 3, 14, 23, 0)
    start_date = sd.strftime("%Y-%m-%d")
    end_date = ed.strftime("%Y-%m-%d")

    locations = {
        "Sulesund": {"lat": 62.402865086109195, "lon": 6.028359996993728},
        "Kvitneset": {"lat": 62.421049661227585, "lon": 6.000482407215768},
        "BuoyA": {"description": "Sulafjorden", "lat": 62.4263, "lon": 6.0447},
        "BuoyD": {"description": "Breisundet", "lat": 62.4464, "lon": 5.9336},
    }

    # Start timing
    start = time.time()
    for name, location in locations.items():
        lat_pos = location["lat"]
        lon_pos = location["lon"]

        product = "NORA3_wind_sub"

        name = f"hindcast-{name}-{product}-{start_date}-{end_date}"

        nc_file = f"./output/simamet/{name}.nc"

        df_ts = ts.TimeSeries(
            lon=lon_pos,
            lat=lat_pos,
            datafile=nc_file,
            start_time=start_date,
            end_time=end_date,
            product=product,
        )

        df_ts.import_data(save_csv=False, save_nc=True, use_cache=True)

        with xr.open_dataset(nc_file) as values:
            values = values.sel(time=slice(sd, ed))
            hindcast_data = __create_hindcast(
                name, values, df_ts.lat_data, df_ts.lon_data
            )
            path = Path(f"./output/simamet/{name}.h5")
            path.parent.mkdir(parents=True, exist_ok=True)
            DMTWriter().write(hindcast_data, path)
            print(f"Written to {path.resolve()}")

    # End timing and print elapsed time
    end = time.time()
    print("Elapsed time: " + str(end - start) + " seconds")
