"""Run a command using SIMA runtime engine (sre executable)"""
import subprocess
import os
import sys
import threading
from pathlib import Path
from typing import Mapping, Sequence
from simapy_results import RESULTS_FILENAME, ResultsError, ResultSet, copy_results, open_results
from .sima_writer import SIMAWriter
from .progress_handler import ProgressHandler
from .sima.command.conditionruncommand import ConditionRunCommand
from .sima.command.importcommand import ImportCommand
from .sima.command.workflowruncommand import WorkflowRunCommand
from .sima.sima.property import Property


class SIMA:
    """"Run a command using SIMA runtime engine (sre executable)"""

    def __init__(self, exe=None, fail_on_error=True,show_output=True):
        self.fail_on_error = fail_on_error
        self.environment = os.environ.copy()
        self.show_output = show_output
        self.exe: str = None
        # Add python directory to PATH to ensure that python is found when running SIMA
        python_dir = os.path.dirname(sys.executable)
        self.environment["PATH"] = python_dir + os.pathsep + self.environment["PATH"]
        # A Console handler is a function that can handle standard out from the process
        # This can i.e. be used to parse @STATUS messages from the SIMA process wich can be used for progress indication
        progress_handler = ProgressHandler(show_output)
        self.console_handler = progress_handler.handle_output
        if exe:
            self.exe = exe
        else:
            self.exe =  os.getenv('SRE_EXE',os.getenv('SIMA_EXE'))
            if not self.exe:
                raise ValueError("No executable given, and SRE_EXE environment variable is not set")
        if not os.path.exists(self.exe):
            raise ValueError(f"Executable {self.exe} does not exist")



    def set_max_concurrent_runs(self, value: int):
        """Set the maximum number of concurrent condition and workflow runs.
        0 means no SIMA will determine this automatically."""
        if value < 0:
            raise ValueError("Value must be greater than or equal to 0")
        self.environment["MAX_CONCURRENT_CONDITION_RUNS"]=str(value)
        self.environment["MAX_CONCURRENT_WORKFLOW_RUNS"]=str(value)


    def run_condition(self, working_dir, task: str, condition: str,
                      run_type: str = "dynamic", stask=None,
                      variables: Mapping[str, object] = None,
                      results_dir=None) -> ResultSet:
        """Run one condition and read its results back. Needs SIMA 5.4 or later.

        Args:
            working_dir: The workspace SIMA runs in. Created if it does not exist.
            task: Name of the task holding the condition.
            condition: Name of the condition to run.
            run_type: `dynamic`, `static`, or whatever the condition supports.
            stask: A task file to import first. Only needed when the workspace
                does not already hold the task.
            variables: Condition variables to override, as `{name: value}`.
            results_dir: If given, results are copied here and the working
                directory can be discarded. If not, they are read in place.

        Returns:
            The condition as SIMA's post processor shows it; for a condition
            set, the set with one condition per member.

        Raises:
            ResultsError: if the run wrote no `results.json`, as a failed run
                does with `fail_on_error=False`.
        """
        wdir = Path(str(working_dir))
        produced = (wdir / task / condition).absolute()
        manifest = produced / RESULTS_FILENAME
        before = _stamp(manifest)
        self.run(wdir, _commands(ConditionRunCommand(task=task, condition=condition,
                                                     runType=run_type), stask, variables))
        # SIMA rewrites it on every run, so an unchanged one describes an earlier run.
        if _stamp(manifest) in (None, before):
            raise ResultsError(f"running {task}/{condition} wrote no {manifest}")
        if results_dir is None:
            return open_results(produced)
        destination = Path(str(results_dir)).absolute()
        copy_results(produced, destination)
        return open_results(destination)

    def run_workflow(self, working_dir, task: str, workflow: str, stask=None,
                     variables: Mapping[str, object] = None) -> None:
        """Run one workflow.

        Nothing is read back; open the file the workflow writes with
        `simapy.results.open_results`.

        Args:
            working_dir: The workspace SIMA runs in. Created if it does not exist.
            task: Name of the task holding the workflow.
            workflow: Name of the workflow to run.
            stask: A task file to import first. Only needed when the workspace
                does not already hold the task.
            variables: Task variables or workflow inputs to override, as
                `{name: value}`.
        """
        run = WorkflowRunCommand(task=task, workflow=workflow)
        self.run(Path(str(working_dir)), _commands(run, stask, variables))

    def run(self, working_dir, command_args: Sequence[str], timeout: float | None = None):
        """Run the sima executable.

        Standard out goes to the console handler and to stdout.txt, standard
        err to stderr.txt, both in the working directory.

        Raises:
            subprocess.TimeoutExpired: if `timeout` seconds pass first; the
                process is killed.
        """

        wdir = Path(str(working_dir))
        arguments = [self.exe]
        arguments.append("-consoleLog")
        arguments.append("--progress")
        arguments.extend(["-data", str(wdir)])
        wdir.mkdir(parents=True, exist_ok=True)
        self.__add_command_args(wdir, arguments, command_args)
        out_file = wdir / "stdout.txt"
        err_file = wdir / "stderr.txt"
        with open(out_file, "w", encoding="utf8") as o_f, open(err_file, "w", encoding="utf8") as e_f:
            proc = subprocess.Popen(arguments,
                        stdin=subprocess.DEVNULL,
                        stdout=subprocess.PIPE,
                        stderr=e_f,
                        env=self.environment)
            expired = threading.Event()

            def kill():
                expired.set()
                proc.kill()

            timer = threading.Timer(timeout, kill) if timeout is not None else None
            if timer is not None:
                timer.start()
            try:
                self.__read_lines(proc, o_f)
                exit_code = proc.wait()
            finally:
                if timer is not None:
                    timer.cancel()
            if expired.is_set():
                raise subprocess.TimeoutExpired(arguments, timeout)
            if exit_code != 0 and self.fail_on_error:
                raise RuntimeError(f"SIMA exited with error code {exit_code}. See sima.log or stderr.txt in {working_dir} for details")

    def __read_lines(self,proc,out_file):
        console_handler = self.console_handler
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            sline = line.decode(encoding="utf8", errors="replace").rstrip()
            console_handler(sline)
            print(sline, end="\n", file=out_file)

    def __add_command_args(self, working_dir: Path, args: Sequence, command_args: Sequence[str]):
        """Add command arguments to the list of arguments"""
        if len(command_args) > 0:
            if isinstance(command_args[0], str):
                args.extend(command_args)
            else:
                filename = Path(working_dir / "commands.json").absolute()
                SIMAWriter().write(command_args, filename)
                args.extend(["--commands",f"file={filename}"])


def _commands(run, stask, variables: Mapping[str, object] | None) -> list:
    """`run` with `variables` as its input, after an import of `stask` if given."""
    if variables:
        # SIMA reads booleans with Boolean.parseBoolean, which ignores case.
        run.input = [Property(key=k, value=str(v)) for k, v in variables.items()]
    if stask is None:
        return [run]
    return [ImportCommand(file=str(Path(str(stask)).absolute())), run]


def _stamp(path: Path) -> tuple[int, int] | None:
    return (path.stat().st_mtime_ns, path.stat().st_size) if path.is_file() else None


def main():
    """Run a single command and read back the result"""
    home = Path.home()
    workspace = home / "SIMA Workspaces" / "SIMAPy_test"

    sima = SIMA()
    commands = ["--help","all"]
    sima.run(workspace,commands)


if __name__ == '__main__':
    main()
