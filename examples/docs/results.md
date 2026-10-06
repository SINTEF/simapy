# Reading results

Install the extras with `pip install simapy[all]`: h5py reads HDF5 results,
pandas makes frames. Condition results need SIMA 5.4 or later.

Run a condition and the results come back with it:

```python
from pathlib import Path
from simapy.sre import SIMA

sima = SIMA()
res = sima.run_condition(
    Path("output/beam"),                 # the workspace SIMA runs in
    task="SimpleBeam",
    condition="Initial",
    run_type="dynamic",
    variables={"Hs": 3.0, "Tp": 6.0},
)

peak = res.run.signal("Dynamic/BeamLine/segment_1/element_1/Axial force").y.max()
```

Add `stask=Path("input/beam.stask")` to import the task first.

Results you already have are opened by their condition folder,
`<workspace>/<task>/<condition>`:

```python
from simapy.results import open_results

res = open_results("output/simo/condition/BouncingBalls/conditionSet")
signal = res.run.signal("conditionSet_1/Dynamic/BALL1/Global total position/ZG translation")

signal.unit, signal.xunit, len(signal)   # ('m', 's', 5000)
signal.y[:3]                             # array([30.        , 29.99555016, 29.98225212])
```

Either way the tree is the one SIMA's post processor shows: the same
containers, signal names and units, with static and dynamic together even when
they ran in separate folders. `res.run` is the condition. For a condition set it
is the set, with one condition per member:

```python
[c.name for c in res.run.containers if c.type == "condition"]   # ['conditionSet_1', ...]
```

Only the latest run is read, never an earlier one left in the workspace.
Nothing has to be exported first, and a condition folder copied elsewhere reads
the same.

## Workflow output

A workflow's file output node writes one named file, so open that file:

```python
res = open_results("output/workflow/ws/out.json")
res.run.signal("some_data/mysine_frompy").unit     # '-'
```

HDF5 and JSON give the same tree. Prefer HDF5 for large output: JSON is parsed
whole when opened, HDF5 reads values only when `.x` or `.y` is touched.

Opening the folder does not pick up a `.json`. A workflow writes its input and
its output as the same signals model in the same place, so only you know which
file is the output.

## Finding signals

`signal()` and `container()` take a path:

```python
res.run.signal("Static/RiserLine/Static forces/EFF. TENSION")
res.run.container("Static/RiserLine")
```

`[]` takes the same path and returns either, which suits exploring; a type
checker only knows it is one of the two.

`select` picks several at once with SIMA's signal requirements, so a requirement
that works in SIMA works here:

```python
res.select("*.Dynamic.*.F-MAX")
res.select(name=["XG translation", "YG translation"])
res.select("*.RiserLine.*", name="F-MAX")
```

- Positional arguments match the path. As in SIMA, it is names joined by `.`
  from the top, the task first: `Simple_Flexible_Riser.Initial.Dynamic.RiserLine.Force envelope curve.F-MAX`.
- `*` matches anything, across levels too.
- A path without `*` names one node, and naming a container selects all of it.
- Keyword arguments match attributes, such as `name`, `type` or `unit`. A list
  gives alternatives, and different keywords must all match.

The result maps each signal's `/` path to the signal. The paths are relative to
what you called `select` on, so they go straight back into `[]`. Two signals
with the same name are renamed as SIMA does: `F-MAX` and `F-MAX_duplicate_1`.

## numpy arrays

`.x` and `.y` are numpy arrays:

```python
import numpy as np

tension = res.run.signal("Static/RiserLine/Static forces/EFF. TENSION")

tension.y.max(), tension.y.mean(), tension.y.std()
np.trapezoid(tension.y, tension.x)          # area under the curve
tension.x[tension.y > 1.8e5]                # where along the line it exceeds 180 kN
```

Values are read on demand. Opening a folder reads names, units and lengths from
the file headers; only `.x`, `.y` and slicing touch the data.

A time series with a fixed step stores no time axis. `.x` is built from the
start and step each time you ask:

```python
signal.is_equidistant            # True
signal.xstart, signal.xdelta     # (0.0, 0.019999999552965164)
```

## Units

Values come back in SI base units, whatever the solver wrote: a force written in
kN reads as N, a mass in Mg as kg. Numbers from runs configured differently are
directly comparable, and match what SIMA shows.

`.to()` returns the signal in another unit and leaves the original alone:

```python
tension.unit, tension.y[:3]           # 'N',  [183114.1 184240.9 185366. ]

tension.to("kN").y[:3]                # [183.1141 184.2409 185.366 ]
tension.to("tonne").y[0]              # 18.672441659486168
tension.to(xunit="mm").x[:3]          # [1000. 3000. 5000.]
```

A converted signal with a fixed step keeps it:

```python
signal.to(xunit="h").xdelta           # 5.555555431379212e-06
signal.to(xunit="h").is_equidistant   # True
```

Degrees, radians, seconds, hours, Hz and rpm are never converted when reading,
only when you ask:

```python
lift = open_results("output/simo/condition/Heavy_Lifting_Operation/Initial")
rotation = lift.run.signal("Dynamic/Platform/Global total position/XB rotation")

rotation.unit, rotation.y[:3]         # 'deg', [-2.48208284 -2.48203874 -2.48190641]
rotation.to("rad").y[:3]              # [-0.04332052 -0.04331975 -0.04331744]
```

A conversion that makes no sense is refused:

```python
tension.to("m")
# ValueError: cannot convert 'N' to 'm': they measure different things (N and m).

tension.to("kip")
# ValueError: cannot convert to 'kip': it is not a unit with a known conversion.
```

If a file names a unit SIMA does not know, the values are left as written, the
signal gets an `unscaled` attribute, and reading it warns once.

### Condition variables

The variables a run used come with their units, in the tree and in the
description:

```python
member = res.run.container("conditionSet_1")
member.signal("Variables/kzz").unit              # 'N*m'

kzz = res.description.members[0].variables["kzz"]
kzz                                              # Variable(value=500.0, unit='N*m')
print(kzz)                                       # 500.0 [N*m]
```

For a plain condition `res.description.variables` holds them; for a set it holds
what the set keeps constant. Text and reference variables have no unit and read
`-`.

## pandas

A signal becomes a Series indexed by its x-axis:

```python
series = tension.to_series()
series.name          # 'EFF. TENSION'
series.index.name    # 'm'
series.attrs         # {'unit': 'N', 'xunit': 'm', 'line': 'RiserLine'}

series.rolling(10).mean()
series.loc[10.0:50.0]
```

A container becomes a DataFrame, one column per signal:

```python
df = res.run.container("Static/RiserLine/Static forces").to_dataframe()

#        EFF. TENSION
# m
# 1.0        183114.1
# 3.0        184240.9
# 5.0        185366.0
```

Signals in one container share an x-axis. Signals in different containers
generally do not, and joining them would invent data, so it is refused:

```python
res.run.container("Static/RiserLine").to_dataframe(recursive=True)
# ValueError: 'XZ' and 'YZ' do not share an x-axis (same 66 samples, different x values).
#             Frame each container separately.
```

Pass `index=False` for columns side by side by position instead.

`signals_to_frame` frames any signals that share an axis, such as the same
signal from several runs, and `names=` sets the columns.

## Examples

| example | what it shows |
|---|---|
| [Run Parallel Conditions](riflex/run_parallel.md) | three runs of one model, compared |
| [Read SIMO Results](simo/read_simo_results.md) | a condition set, its members compared |
| [Results as pandas](simo/results_to_pandas.md) | Series, DataFrame, and one column per member |
