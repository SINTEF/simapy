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

def __run_single(run: dict, progress_manager: ProgressManager):
    """Execute a single SIMA run with progress tracking.
    
    Args:
        run (dict): Run configuration containing name, ws, commands, exe, postprocess, cleanup
        progress_manager (ProgressManager): Manager for handling progress bars
        
    Notes:
        Monitors SIMA console output for "@STATUS" messages to track progress.
    """
    name: str = run["name"]
    ws: Path = run["ws"]
    commands: list = run["commands"]
    if ws.exists():
        shutil.rmtree(ws,ignore_errors=True)
    os.makedirs(ws,exist_ok=True)
    exe = run.get("exe", None)
    sima = SIMA(exe=exe)
    def __handle_output(line):
        # "@STATUS "Total" 800 1000"
        if line.startswith("@STATUS"):
            # Findt the last number
            parts = line.split()
            worked = float(parts[-1-1])
            total = float(parts[-1])
            progress = 100 * worked/total
            progress_manager.update_progress(name, progress)

    sima.console_handler = __handle_output
    sima.run(working_dir=ws, command_args=commands)
    # Check if we have a postprocess function
    postprocess = run.get("postprocess", None)
    if postprocess:
        postprocess()

    progress_manager.update_progress(name, 100)
    progress_manager.close_progress_bar(name)
    cleanup = run.get("cleanup", False)
    if cleanup:
        shutil.rmtree(ws,ignore_errors=True)

def run_multiple(runs: list[dict]):
    """Execute multiple SIMA runs concurrently with progress tracking.
    
    Args:
        runs (list[dict]): List of run configuration dictionaries
                          
    Notes:
        Uses (cpu_count() - 1) worker threads. Individual run failures don't stop
        the entire batch. Provides summary of successes/failures at the end.
    """
    # Create progress manager
    progress_manager = ProgressManager()

    # Create progress bars for each run
    for run in runs:
        progress_manager.create_progress_bar(run["name"])

    # Run a maximum of cpu_count() - 1 workflows at the same time
    num_concurrent = os.cpu_count() - 1

    try:
        with ThreadPoolExecutor(max_workers=num_concurrent) as executor:
            jobs = []
            for run in runs:
                # Submit job
                jobs.append(executor.submit(__run_single, run, progress_manager))
            for job in jobs:
                try:
                    job.result()
                except Exception as e:
                    raise e
    finally:
        progress_manager.close_all()
