"""Run a command using SIMA runtime engine (sre executable)"""
import subprocess
import os
from pathlib import Path
from typing import Sequence,Callable
from simapy.sima_writer import SIMAWriter


class SIMA:
    """"Run a command using SIMA runtime engine (sre executable)"""

    def __init__(self, exe=None, fail_on_error=True):
        self.fail_on_error = fail_on_error
        self.environment = os.environ.copy()
        # A Console handler is a function that can handle standard out from the process
        # This can i.e. be used to parse @STATUS messages from the SIMA process wich can be used for progress indication
        self.console_handler: Callable[[str],None] = self.__handle_console_output
        if exe:
            self.exe = exe
        else:
            self.exe =  os.getenv('SRE_EXE',os.getenv('SIMA_EXE'))
            if not self.exe:
                raise ValueError("No executable given, and SRE_EXE environment variable is not set")


    def set_max_concurrent_runs(self, value: int):
        """Set the maximum number of concurrent condition and workflow runs.
        0 means no SIMA will determine this automatically."""
        if value < 0:
            raise ValueError("Value must be greater than or equal to 0")
        self.environment["MAX_CONCURRENT_CONDITION_RUNS"]=str(value)
        self.environment["MAX_CONCURRENT_WORKFLOW_RUNS"]=str(value)


    def __handle_console_output(self, sline: str) -> None:
        print(sline, end="\n")

    def run(self, working_dir, command_args: Sequence[str]):
        """Run the sima executable and print output to standard out.
           Standard err is piped to stderr.txt in the working directory"""

        wdir = Path(str(working_dir))
        arguments = [self.exe]
        arguments.append("-consoleLog")
        arguments.append("--progress")
        arguments.extend(["-data", working_dir])
        wdir.mkdir(parents=True, exist_ok=True)
        self.__add_command_args(working_dir, arguments, command_args)
        out_file = wdir / "stdout.txt"
        with open(out_file, "w", encoding="utf8") as o_f:
            proc = subprocess.Popen(arguments,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        env=self.environment)
            self.__read_lines(proc, o_f)
            # Wait for the process to finish
            exit_code = proc.wait()
            if exit_code != 0 and self.fail_on_error:
                raise RuntimeError(f"SIMA exited with error code {exit_code}")

    def __read_lines(self,proc,out_file):
        console_handler = self.console_handler
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            sline = line.decode(encoding="utf8").rstrip()
            console_handler(sline)
            print(sline, end="\n", file=out_file)

    def __add_command_args(self, working_dir: Path, args: Sequence, command_args: Sequence[str]):
        """Add command arguments to the list of arguments"""
        if len(command_args) > 0:
            if isinstance(command_args[0], str):
                args.extend(command_args)
            else:
                filename = working_dir / "commands.json"
                SIMAWriter().write(command_args, filename)
                args.extend(["--commands",f"file={filename}"])

def main():
    """Run a single command and read back the result"""
    home = Path.home()
    workspace = home / "SIMA Workspaces" / "SIMAPy_test"

    sima = SIMA()
    commands = ["--help","all"]
    sima.run(workspace,commands)


if __name__ == '__main__':
    main()
