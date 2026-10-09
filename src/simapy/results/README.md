# simapy.results

Read SIMA results as a lazy signal hierarchy.

```python
from simapy.results import open_results

res = open_results(r"C:\ws\TestWs\Simple_Flexible_Riser\Initial")
sig = res.run.signal("Static/RiserLine/Static forces/EFF. TENSION")

sig.unit, sig.xunit, len(sig)   # ('N', 'm', 65)   -- no numbers parsed yet
sig.y[:3]                       # array([183114.1, 184240.9, 185366. ])
```

## A port, not a parallel design

The tree, the merge rules, the sibling order and `select` are ports of SIMA's
own code (`ConditionResultImporter`, `SignalItemUtil`, `SignalItemQuery`). Where
behaviour looks odd, matching SIMA is usually the reason:

* **Signals merge without deduplication.** Importing the same file twice doubles
  its signals, as in SIMA. Repeats are renamed as SIMA's tree view renames them:
  `Tension`, `Tension_duplicate_1`, …
* **Containers merge by attribute union.** Two same-named containers merge unless
  both set one key to different values; such a pair stays separate and warns.
* **Siblings sort with SIMA's comparator**, which is not a total order: an
  untyped node ties with everything. That is why `RiserLine` stays ahead of
  `Static iterations`.

## A condition, a run folder, or a file

Point `open_results` at a condition folder, at one working directory a solver
left its files in, or at one result file. Beside the results, a few files carry
what is not itself a result. All are optional:

| file | gives | without it |
|---|---|---|
| `names.map`, `riflexres.inp` | hashed model id to name -- `Risea63d` to `RiserLine`; `riflexres.inp` wins, as in SIMA's MPF import | ids stay hashed |
| `results.json` | the task and condition, the variables with their units, and each analysis's working directory | names from the path, variables from `variables.inp`, one folder at a time |
| `variables.inp` | the variable values alone, and the task name | no `Variables` container |

SIMA writes `results.json` from 5.4, and `SIMA.run_condition` reads the
condition through it, so it refuses a run that wrote none. A variable's value
and unit come from one place: `results.json` when it gives values, else
`variables.inp`, whose variables read unit `-`. The folder path names the run too --
`<workspace>/<task>/<condition>`, skipping timestamp folders such as
`1-20260901063413` -- but only until the results are moved.

**A condition is what `results.json` says it is.** Static and dynamic can run
into separate timestamp folders, and with folder deletion off, stale ones
accumulate; nothing in the folders pairs them. The condition's `results.json`
maps each analysis to its working directory, so opening the condition folder
reads exactly those, and each folder gives only its own analysis -- SIMA copies
static results such as `psc.lis` into the dynamic folder too.

Without that map the caller says which run it means. The condition folder then
raises `ResultsError` naming its runs:

```python
open_results(condition)                                           # the whole condition
open_results(condition / "1-20260901083636")                      # one run folder
open_results(condition / "1-20260901083937" / "ConditionSet_1")   # one set member's folder
```

### Which files are results

SIMA decides mostly by hard-coded name: an allowlist. What is reproduced here is
a denylist of working files (`simo.h5`, `env.h5`, intermediates) plus "some
reader claims the extension". That is exact while the readers claim only `mpf`,
`h5`, `hdf5`, `b5` and one exact name, `psc.lis`, because nothing else in a run
folder (`.inp`, `.dat`, the other `.lis`, `.ldat`, …) uses those. Unclaimed
files are left out of `sources` rather than reported as gaps, with one
exception below.

**Storage simapy does not read is reported, not skipped.** RIFLEX binary or
ASCII storage (`sima_noddis.bin` beside `key_sima_noddis.txt`) and SIMO's old
result structure (`results.tda`) are results, so dropping them would leave a
tree that looks complete without its time series. They show in `sources` as
`unsupported`, and an `UnsupportedStorageWarning` names the SIMA setting that
stores them as HDF5. The key file is what identifies RIFLEX storage: RIFLEX
writes other `.asc` files that are not results.

`simo-static-results.h5` and `simo-dynamic-results.h5` are results despite being
on SIMA's list of working files; SIMA adds them back explicitly, and so does this.

`.json` is never picked up by a scan, though a reader reads it: a workflow writes
its input and its output as the same signals model in one folder, and nothing in
either says which is which. Open the file by name.

**`psc.lis` is copied between runs**: SIMA puts the static run's into every
dynamic folder. With `directories` the copy is never read, since each folder
gives only its own analysis. Without them a folder offers `psc.lis` only beside
a static result of its own (`simo-static-results.h5`, a `stamod` file), so a
dynamic folder never claims it. A new reader needs the same look. Its names come
from the `simores.inp` SIMA writes beside it; without that file the source
fails, because SIMA's fallback is the model.

## Laziness

| source | at open | values |
|---|---|---|
| HDF5 | shapes and attributes | the file is reopened and sliced on each access, uncached |
| MPF | headers, row counts and byte offsets | a matrix parsed whole on first touch, cached |
| JSON | the whole document | already in memory |
| `psc.lis` | the whole file, with `simores.inp` | already in memory |

`name`, `type`, `attributes`, `unit`, `xunit`, `len()` and navigation never
parse a number. The HDF5 reader reopens rather than holding datasets open,
because keeping every result file open for the life of the tree leaks
descriptors.

A SIMO time series has no stored x-axis: just `start` and `delta`, as in SIMA.
`Signal.x` is synthesised on each call and never kept, and `Signal.same_axis`
compares start, delta and size without reading anything. That lets a whole SIMO
body become one frame with a single time index:

```python
res.run.container("Dynamic/Platform").to_dataframe(recursive=True)   # (100, 26)
```

## Selecting signals

`select` applies SIMA's signal requirements, so a requirement copied from SIMA
selects the same signals:

```python
res.select("*.Dynamic.*.F-MAX")                       # path requirements
res.select(name=["XG translation", "YG translation"]) # one key: alternatives
res.select("*.RiserLine.*", name="F-MAX")            # different keys: all must hold
```

* A path is SIMA's: names joined by `.` from the root, the task first --
  `Simple_Flexible_Riser.Initial.Dynamic.RiserLine.Force envelope curve.F-MAX`.
  As in SIMA, a `.` inside a name is indistinguishable from the separator.
* `*` matches anything, across levels too; `?` at most one character.
* A path without `*` names a node exactly, and naming a container selects its
  subtree. Likewise, a container meeting every requirement brings all its signals.

The query-string mode (`name==*Fx* && line!=Riser1`) is not ported.

The result maps `/` paths, relative to the container called on, to signals, so
each key goes straight back into `[]`.

## numpy is the core; pandas is a view

`Signal.x` and `Signal.y` are read-only ndarrays. pandas and h5py are optional:
`pip install simapy[pandas]`, `simapy[hdf5]`, or `simapy[all]`.

A container is the natural frame, since it is one source block -- one RIFLEX
`MATRIX`, one HDF5 group -- and its signals normally share an x-axis. Signals
whose axes differ are refused rather than aligned, because **RIFLEX x-axes
repeat values**: a curvature is sampled at both ends of every element
(`[0, 2, 2, 4, 4, …]`), and aligning two such axes would invent data.
`index=False` gives positional semantics instead.

## Condition sets

Opening a set's condition folder gives the tree SIMA's post processor shows:
task, then the set (type `conditionContainer`), then one condition per member,
each with its own `Variables` first and its analyses after. The set's own
`Variables` hold what it keeps constant. `res.description.members` describes
each member.

```python
FORCE = "Dynamic/Platform/Positioning elements/MooringLine1/Total force"

res = open_results(condition)
for member in res.description.members:
    print(member.variables["hs"].value, res.run.container(member.condition).signal(FORCE).y.max())
```

## Best effort

Opening a folder never raises because one result file is unreadable. The failure
lands in `res.sources` and as an `ErrorSignal` where the data should have been,
as in SIMA. `ResultsError` is raised only when the source is neither a folder nor
a file, is a file no reader claims, or is a folder holding no result file.

```python
for src in res.sources:
    print(f"{src.file:26} {src.type:4} {src}")
# sima_stamod.mpf            mpf  read (15 signals)
# sima_elmfor.h5             h5   failed: SourceError: ...
```

## One public module, and a read-only tree

`simapy.results` is the whole API; every module behind it is private, so readers,
registry, importer, merge rules and scanner can change. The tree is read-only:
nodes expose accessors only, an array handed out is either fresh or
non-writeable, and the functions that fill a tree live in `_build`. Adding a
format means adding a reader here, not registering one from outside.

## Verified against SIMA

`test_results_oracle.py` checks container shape, names, units, lengths and end
values against `riflex_run_oracle.json`, a snapshot of the file SIMA's post
processor wrote to `Riflex_Results.h5` from the same run. The HDF5 reader reads
all 44 of those signals back from that file under their true names, so the MPF
and HDF5 readers agree by independent routes.

`test_results_psc.py` checks every body, container, signal, unit and value read
from `psc.lis` against `psc_oracle.json`, the tree SIMA built from the same
static run.

HDF5 keys cannot hold `.`, `/` or non-ASCII, so the exporter writes
`EFF_ TENSION` and keeps `EFF. TENSION` in a `name` attribute (and suffixes
`_duplicate_N` on collisions). The reader looks nodes up by key while building,
then renames them to the true name.

## The two HDF5 layouts

Dispatch is on the root `format` attribute. `_readers/hdf5.py` reads the
unformatted layout RIFLEX writes (`ts_buffer.b5`, `Riflex_Results.h5`);
`_readers/simos_r0.py` reads SIMO's. In the latter, metadata lives in child
datasets (`value`, `unit`, `xunit`, `name`), array members are keyed `0`, `1`, …
and named by a `name` dataset, and values are **rescaled** to base units as both
Java implementations do -- reading them untouched would be off by 1000 on most
forces.

SIMO's own result files, `simo-static-results.h5` and `simo-dynamic-results.h5`,
get what SIMA's `SIMOHDF5ResultsImporter` does on top: the root `results` level
goes, and each body becomes a container of type `body` directly under its
analysis.

## Units

`_units.py` ports SIMA's unit registry and label grammar rather than tabulating
answers. Resolution is per atom: `kN/m^2` is `{kN: 1, m: -2}`, each atom mapped
to its base and recomposed, so `kN*m/deg` works unanticipated. The grammar is
SIMA's, quirks included -- `/` binds loosest, so `a/b*c` is `a/(b*c)`.
`test_results_units.py` transcribes SIMA's own unit tests; the three deliberate
divergences (whitespace, colliding exponents, empty atoms) are documented in the
module and tested.

A label SIMA does not know keeps the file's numbers *and* label, is marked with
an `unscaled` attribute, and warns once per axis when read. Scaling the known
atoms only would turn `kN/glorp` into numbers labelled kN that are not.

`Signal.to()` has no SIMA counterpart: SIMA scales on the way in and never back.
It works per atom too, and `to("kN").to("N")` is the identity. Base units SIMA
keeps apart -- `deg`/`rad`, `s`/`h`, `Hz`/`rpm`/`1/s` -- never convert on the way
in; `to()` bridges them on request, but only where the factor is exact by
definition (no `year`, no `C`). `Pa` is not bridged to `N/m^2`, because SIMA
treats pressure as its own quantity.

## Not done

* `ldat` and `res`, never: SIMA registers them for its own use (3D view, listing
  output), and they hold nothing to compare.
* Reading `bin`/`asc` storage, being moved to HDF5 upstream, and TDA, being
  phased out for HDF5. Both are reported instead.
* Writing. The tree stays decoupled from the DMT signals model in
  `simapy.sima.signals`; if results ever go back into SIMA, those classes already
  serialise to signals JSON and HDF5.
* Eigenvalue and outmod post-transforms in the MPF reader.
* Post-processing: resampling between SIMO and RIFLEX, statistics, spectra.
* An `s2x` reader, and replacing the srv integration tester's MPF reader -- both
  wait for the migration in `srv`.
