"""Read wave data from nora3 and generate metocean hindcast readable from SIMA"""

from pathlib import Path
import time
import numpy as np
import xarray as xr
from dmt.dmt_writer import DMTWriter
from metocean_api import ts
import simapy.metocean.hindcast as hc


def __create_wave(wave_name, hs, tp, direction):
    # NORA3_wave_wind: North East Down, wave_going_to
    # SIMA MET: North East Down, wave coming from
    dir_sima = (180.0 + direction) % 360.0
    return hc.StochasticWave(name=wave_name, hs=hs, tp=tp, direction=dir_sima)


def __create_hindcast(hc_name, hc_values, lat_pos, lon_pos):
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
    dates = hc_values["time"].astype("datetime64[s]")
    sdates = np.datetime_as_string(dates, unit="h", timezone="UTC").astype("|S")

    hindcast = hc.Hindcast()
    hindcast.description = hindcast.description = (
        f"Collected using Norway MET metocean-api with product {product}"
    )
    hindcast.name = hc_name
    hindcast.date = sdates
    hindcast.latitude = lat_pos
    hindcast.longitude = lon_pos
    hindcast.wave = waves

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
    start_date = "2017-01-19"
    end_date = "2017-01-20"

    lon_pos = 5.835813
    lat_pos = 64.731729

    product = "NORA3_wind_wave"

    name = f"hindcast-{product}-{start_date}-{end_date}"
    requested_values = [
        "hs",
        "tp",
        "thq",
        "hs_sea",
        "tp_sea",
        "thq_sea",
        "hs_swell",
        "tp_swell",
        "thq_swell",
        "wind_speed",
        "wind_direction",
    ]

    output_dir = Path("./output/simamet")
    output_dir.mkdir(exist_ok=True, parents=True)
    nc_file = str(output_dir / f"{name}.nc")

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

    with xr.open_dataset(nc_file) as values:
        hindcast_data = __create_hindcast(name, values, df_ts.lat, df_ts.lon)
        dates = values["time"].values
        path = Path(f"./output/simamet/{name}.h5")
        path.parent.mkdir(parents=True, exist_ok=True)
        DMTWriter().write(hindcast_data, path)
        print(f"Written to {path.resolve()}")

