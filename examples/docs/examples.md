# Examples

To run an example:

1. Navigate to the specific example directory under `examples/`
2. Run the Python script for that example

* `examples/` - Contains all example scripts, one directory per domain
* `input/` - Contains input files used by the examples
* `output/` - Directory where script outputs are saved

The examples are organized by category, with each category focusing on different aspects of the SIMAPY package:

## SIMO

```{toctree}
:maxdepth: 1

simo/write_simo_task
simo/run_simo_condition
simo/read_simo_results
simo/results_to_pandas
simo/import_hydrodynamic_coefficients
simo/create_connected_bodies
```

## RIFLEX

```{toctree}
:maxdepth: 1

riflex/read_and_write_riflex
riflex/run_parallel
```


## Workflow

```{toctree}
:maxdepth: 1

workflow/run_workflow_with_sre
workflow/run_from_stask_with_file
workflow/run_parallel
```

## Metocean

```{toctree}
:maxdepth: 1

metocean/metocean
metocean/create_excel_scatter
metocean/create_hindcast_wave
metocean/create_hindcast_wave_wind
metocean/create_hindcast_wind
metocean/create_sima_scatter
```