
"""
# Create SIMA Scatter Tables

This example demonstrates how to create metocean scatter tables and save them in 
SIMA-compatible format using the SIMAPy API.

## Description

The script shows how to create metocean scatter tables from external data sources
(using the [metocean stats library](https://metocean-stats.readthedocs.io)) and save them for use in SIMA. 
The workflow includes:

1. Using the `metocean_stats` library to retrieve wave data for a specific location and time period
2. Calculating a scatter table from the time series data (significant wave height vs. peak period)
3. Converting the data to SIMA's internal scatter table format
4. Exporting the scatter table to a SIMA-compatible HDF5 file

## Key Features

- **Metocean Data Access**: Demonstrates accessing wave data from the NORA3 dataset
- **Statistical Analysis**: Shows how to generate scatter tables from time series data
- **SIMA Integration**: Converts the data to SIMA's internal data structures
- **DMT Export**: Saves the data in SIMA's Data Model Technology (DMT) format

## Usage

This example is particularly useful for:

- Creating site-specific metocean data for marine simulations
- Preparing environmental conditions for design or operational analysis
- Generating scatter tables for fatigue analysis or operational assessments

```python
# Basic usage of this script
python create_sima_scatter.py
```

The exported HDF5 file can be imported directly into SIMA by right-clicking on a 
Metocean Task and selecting "Import metocean data".
"""
from pathlib import Path
import pandas as pd
from metocean_api import ts
from metocean_stats.stats.general import calculate_scatter
from simapy.metocean.scatter.scatter import Scatter as SimaScatter
from simapy.metocean.scatter.sector import Sector
from simapy.metocean.scatter.wave import Wave
from dmt.dmt_writer import DMTWriter


def _create_sima_scatter(scatter: pd.DataFrame) -> SimaScatter:
    """
    Convert a pandas DataFrame scatter table to a SIMA scatter object.
    
    This function takes a pandas DataFrame containing a wave scatter table
    (with significant wave height as index and peak period as columns)
    and converts it to a SIMA scatter object that can be saved in SIMA's
    native format.
    
    Args:
        scatter (pd.DataFrame): DataFrame containing the scatter table with
                               Hs as index and Tp as columns
                               
    Returns:
        SimaScatter: A SIMA scatter object ready for export
    """
    sima_scatter = SimaScatter()
    sima_scatter.name = "Scatter"
    hs = scatter.index
    tp = scatter.columns
    occurences = scatter.values

    sima_scatter.hsUpperLimits = hs
    sima_scatter.tpUpperLimits = tp

    omni = Sector()
    omni.name = "Omni"
    omni.description = f"Omni-directional scatter table created from product {product} for the period {start_date} to {end_date}"
    sima_scatter.omni = omni
    wave = Wave()
    wave.occurrence = occurences
    omni.wave = wave
    return sima_scatter

if __name__ == "__main__":
    lat_pos = 62.5365
    lon_pos = 4.1770
    start_date = "2020-10-21"
    end_date = "2020-11-21"

    product = "NORA3_wave_sub"
    var1_name = "hs"
    var2_name = "tp"

    var1_block_size = 1.0
    var2_block_size = 2.0

    requested_values = [var1_name, var2_name]

    df_ts = ts.TimeSeries(
        lon=lon_pos,
        lat=lat_pos,
        start_time=start_date,
        end_time=end_date,
        variable=requested_values,
        product=product,
    )

    df_ts.import_data(save_csv=False, save_nc=False, use_cache=True)

    scatter: pd.DataFrame = calculate_scatter(df_ts.data, var1_name, var1_block_size, var2_name, var2_block_size)

    sima_scatter = _create_sima_scatter(scatter)

    path = Path(f"./output/simamet/scatter_{product}-{start_date}-{end_date}.h5")
    path.parent.mkdir(parents=True, exist_ok=True)
    DMTWriter().write(sima_scatter, path)
    print(f"Saved to {path.resolve()}")
