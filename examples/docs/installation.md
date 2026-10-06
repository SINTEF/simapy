# Installation

The examples live in the `examples/` folder of the simapy repository and use
simapy from the same checkout.

## Requirements

* Python 3.11 or later
* SIMA 5.4 or later, for the examples that run SIMA. Set `SRE_EXE` to `sre.exe`
  in the SIMA installation folder.

## Setting up the examples

1. Clone the repository:

   ```bash
   git clone https://github.com/SINTEF/simapy.git
   cd simapy
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On Linux/macOS
   source .venv/bin/activate
   ```

3. Install simapy from the checkout, with the extras the examples use:

   ```bash
   pip install -e ".[all]" matplotlib
   ```

   The metocean examples need more:

   ```bash
   pip install -r examples/metocean/requirements-metocean.txt
   ```

With [uv](https://docs.astral.sh/uv/), `uv sync` does steps 2 and 3, except the
metocean requirements.
