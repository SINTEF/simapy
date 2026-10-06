"""Run a SIMO condition from a task file.

Imports a SIMA task file (stask), runs one condition and gets the results back
in the same call. The condition here is a set of three members, and it comes
back as one set holding them.

Requirements:
    - Environment variable `SRE_EXE` which points to the SIMA executable
    - Input file: 'input/simo/simo.stask'

Example:
    >>> python simo/run_simo_condition.py
"""
import os
import shutil
from pathlib import Path

from simapy.results import Status
from simapy.sre import SIMA

EXAMPLES = Path(__file__).parents[1]

#: Where the run puts its results, and what it runs. read_simo_results.py
#: imports these so the reader looks exactly where the runner wrote.
WORKSPACE = EXAMPLES / "output" / "simo" / "condition"
STASK = EXAMPLES / "input" / "simo" / "simo.stask"
TASK = "BouncingBalls"
CONDITION = "conditionSet"
RUN_TYPE = "dynamic"


def main():
    """Run the condition and report what came back.

    Starts from an empty workspace so the run is repeatable.

    Returns:
        The `ResultSet`, so a caller can go straight on to reading it.
    """
    if WORKSPACE.exists():
        shutil.rmtree(WORKSPACE, ignore_errors=True)

    sima = SIMA(exe=os.getenv("SRE_EXE"))
    res = sima.run_condition(WORKSPACE, task=TASK, condition=CONDITION,
                             run_type=RUN_TYPE, stask=STASK)

    members = res.description.members
    print(f"\n{len(members)} member(s) in {WORKSPACE.relative_to(EXAMPLES)}")
    for member in members:
        # str(variable) is "500.0 [N*m]"
        values = ", ".join(f"{n}={v}" for n, v in member.variables.items())
        print(f"   {member.condition:16} {values:20} "
              f"{len(res.run.container(member.condition).select())} signals")

    unread = sum(1 for src in res.sources if src.status is not Status.READ)
    if unread:
        print(f"\n   {unread} file(s) could not be read; res.sources says why")

    return res


if __name__ == "__main__":
    main()
