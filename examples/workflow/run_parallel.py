"""
This example demonstrates how the Python module concurrent.futures may be used to run
workflows with multiple SIMA instances in parallel.
"""
import os
import sys
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from simapy.sre import SIMA
from simapy.results import Status, open_results
from simapy.sima_writer import SIMAWriter
from simapy.sima.signals.equallyspacedsignal import EquallySpacedSignal

def run_single(case_num: int, a: float, b: float):
    print(f'Starting case {case_num}')
    ws_root = Path(__file__).parents[1] / 'output' / 'workflow' / 'concurent'
    ws = ws_root / f'ws_{case_num}'
    if ws.exists():
        shutil.rmtree(ws,ignore_errors=True)
    os.makedirs(ws,exist_ok=True)

    a_signal = EquallySpacedSignal(name='a')
    a_signal.value = [a]
    b_signal = EquallySpacedSignal(name='b')
    b_signal.value = [b]

    SIMAWriter().write([a_signal, b_signal], ws / 'input.json')

    # Locate stask file in the examples 'input' folder
    stask = Path(__file__).parents[1] / 'input' / 'workflow' / 'simple_workflow_run.stask'

    # Requires that the environment is set, but an alternative path may be given

    sima = SIMA()
    # Create a handler to print the progress while running
    def _handle_output(line):
        # "@STATUS "Total" 800 1000"
        if line.startswith("@STATUS"):
            parts = line.split()
            worked = float(parts[-2])
            total = float(parts[-1])
            progress = 100 * worked/total
            print(f"Progress case {case_num}: ",progress,"%")

    sima.console_handler = _handle_output
    sima.run_workflow(ws, task='WorkflowTask', workflow='outer', stask=stask)

    res = open_results(ws / 'Output' / 'output.json')
    failed = [s for s in res.sources if s.status is not Status.READ]
    if failed:
        raise RuntimeError(f'Case {case_num}: ' + '; '.join(f'{s.file}: {s.detail}' for s in failed))
    values = ', '.join(f'{signal.y[0]:g}' for signal in res.select().values())
    print(f'Case {case_num} completed successfully: {values}')


def main():
    # Run a maximum of cpu_count() - 1 workflows at the same time
    num_concurrent = max(1, (os.cpu_count() or 2) - 1)
    # Total number of workflow runs
    num_cases = 10
    with ThreadPoolExecutor(max_workers=num_concurrent) as executor:
        jobs = []
        for i in range(num_cases):
            # Set some arbitrary values for a and b
            a = i * 2.0
            b = (i + 1) * 10.0
            # Submit job
            jobs.append(executor.submit(run_single, i, a, b))
        any_failure = False
        for i, job in enumerate(jobs):
            try:
                job.result()
            except Exception as e:
                print(f'Job {i} Failed: {e}')
                any_failure = True

    if any_failure:
        print('Runs completed with errors')
        sys.exit(1)
    else:
        print('All runs completed successfully')

if __name__ == "__main__":
    main()
