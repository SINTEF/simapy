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
from simapy.sima_writer import SIMAWriter
from simapy.sima.signals.equallyspacedsignal import EquallySpacedSignal

def run_single(case_num: int, a: float, b: float):
    print(f'Starting case {case_num}')
    ws_root = Path(__file__).parent / '..' / '..' / 'output' / 'workflow' / 'concurent'
    ws = ws_root / f'ws_{case_num}'
    if ws.exists():
        shutil.rmtree(ws,ignore_errors=True)
    os.makedirs(ws,exist_ok=True)

    a_signal = EquallySpacedSignal(name='a')
    a_signal.value = [a]
    b_signal = EquallySpacedSignal(name='b')
    b_signal.value = [b]

    SIMAWriter().write([a_signal, b_signal], ws / 'input.json')

    # Locate stask file in folder 'input' at the root of this repository
    stask = Path(__file__).parent / '..' / '..' / 'input' / 'workflow' / 'simple_workflow_run.stask'

    commands = []
    commands.append('--import')
    commands.append('file='+str(stask.absolute()))
    commands.append('--run')
    commands.append('task=WorkflowTask')
    commands.append('workflow=outer')

    # Requires that the environment is set, but an alternative path may be given

    sima = SIMA()
    # Create a handler to print the progress while running
    def __handle_output(line):
        # "@STATUS "Total" 800 1000"
        if line.startswith("@STATUS"):
            # Findt the last number
            parts = line.split()
            worked = float(parts[-1-1])
            total = float(parts[-1])
            progress = 100 * worked/total
            print(f"Progress case {case_num}: ",progress,"%")

    sima.console_handler = __handle_output
    sima.run(working_dir=str(ws), command_args=commands)
    print(f'Case {case_num} completed successfully')


def main():
    # Run a maximum of cpu_count() - 1 workflows at the same time
    num_concurrent = os.cpu_count() - 1
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