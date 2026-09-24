"""Parallel Runner Module.

Runs multiple SIMA analysis conditions concurrently using ThreadPoolExecutor
with real-time progress tracking and error handling.
"""
import os
import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from simapy.sre import SIMA
from .progress import ProgressManager


def _run_single(run: dict, progress_manager: ProgressManager):
    """Execute a single SIMA run with progress tracking.

    Args:
        run (dict): Run configuration: name, ws, stask, task, condition, and
            optionally run_type, variables, results_dir, exe, postprocess
        progress_manager (ProgressManager): Manager for handling progress bars

    Notes:
        Monitors SIMA console output for "@STATUS" messages to track progress.
    """
    name: str = run["name"]
    ws: Path = run["ws"]
    if ws.exists():
        shutil.rmtree(ws, ignore_errors=True)
    os.makedirs(ws, exist_ok=True)
    sima = SIMA(exe=run.get("exe"))

    def _handle_output(line):
        # "@STATUS "Total" 800 1000"
        if line.startswith("@STATUS"):
            parts = line.split()
            worked = float(parts[-2])
            total = float(parts[-1])
            progress_manager.update_progress(name, 100 * worked / total)

    sima.console_handler = _handle_output
    res = sima.run_condition(
        ws,
        task=run["task"],
        condition=run["condition"],
        run_type=run.get("run_type", "dynamic"),
        stask=run.get("stask"),
        variables=run.get("variables"),
        results_dir=run.get("results_dir"),
    )
    # The postprocess function gets the results, so it does not have to know
    # where they were written.
    postprocess = run.get("postprocess")
    if postprocess:
        postprocess(res)

    progress_manager.update_progress(name, 100)
    progress_manager.close_progress_bar(name)


def run_multiple(runs: list[dict]) -> list[dict]:
    """Execute multiple SIMA runs concurrently with progress tracking.

    Args:
        runs (list[dict]): List of run configuration dictionaries

    Returns:
        list[dict]: The runs that completed, in the order given.

    Notes:
        Uses cpu_count() - 1 worker threads. A failed run is reported and the
        rest carry on.
    """
    progress_manager = ProgressManager()
    for run in runs:
        progress_manager.create_progress_bar(run["name"])

    completed = []
    try:
        with ThreadPoolExecutor(max_workers=max(1, (os.cpu_count() or 2) - 1)) as executor:
            jobs = [executor.submit(_run_single, run, progress_manager) for run in runs]
            for run, job in zip(runs, jobs):
                try:
                    job.result()
                    completed.append(run)
                except Exception as error:
                    print(f"   {run['name']} failed: {error}")
    finally:
        progress_manager.close_all()
    return completed
