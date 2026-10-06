# Examples using simapy

[simapy](https://github.com/SINTEF/simapy) is a Python library for interacting with SIMA.

The documentation for these examples is built from [docs/](docs/):
[installation](docs/installation.md), then one page per example.

## Installation

From the repository root, install simapy from the checkout with the extras the
examples use:

```bash
pip install -e ".[all]" matplotlib
```

The metocean examples also need `pip install -r examples/metocean/requirements-metocean.txt`.

## Examples

One folder per domain: `simo/`, `riflex/`, `workflow/` and `metocean/`. Input
files are in `input/`, and the scripts write to `output/`.

## License

[MIT](https://choosealicense.com/licenses/mit/)
