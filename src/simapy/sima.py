"""Run a command using SIMA runtime engine (sre executable)"""
import asyncio
import os
from pathlib import Path
from typing import Sequence
from simapy.sima_writer import SIMAWriter


async def run_command(args, error_file, out_file):
    """"Run a command asynchronously and print output to standard out. 
    Standard err is piped to stderr.txt in the working directory"""
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=error_file
    )

    while True:
        stdout, _ = await process.communicate()

        if stdout:
            for line in stdout.splitlines():
                sline = line.decode("utf-8")
                if sline.startswith("@STATUS"):
                    print("STATUS found:" + sline, end="\n")
                else:
                    print(sline, end="\n")
                    print(sline, end="\n", file=out_file)

        if process.returncode is not None:
            return process.returncode


class SIMA:
    """"Run a command using SIMA runtime engine (sre executable)"""

    def __init__(self, exe=None, fail_on_error=True):
        self.fail_on_error = fail_on_error
        if exe:
            self.exe = exe
        else:
            self.exe =  os.getenv('SRE_EXE',os.getenv('SIMA_EXE'))
            if not self.exe:
                raise ValueError("No executable given, and SRE_EXE environment variable is not set")


    def run(self, working_dir: Path, command_args: Sequence):
        """Run the sima executable and print output to standard out. 
           Standard err is piped to stderr.txt in the working directory"""
        arguments = [self.exe]
        arguments.extend(["-configuration", "/var/opt/sima/config"])
        arguments.append("-consoleLog")
        arguments.append("--progress")
        arguments.extend(["-data", working_dir])
        working_dir.mkdir(parents=True, exist_ok=True)
        self.__add_command_args(working_dir, arguments, command_args)
        err_file = working_dir / "stderr.txt"
        out_file = working_dir / "stdout.txt"
        with open(err_file, "w", encoding="utf8") as ef, open(
            out_file, "w", encoding="utf8"
        ) as of:
            exit_code = asyncio.run(run_command(arguments, ef, of))
            if exit_code != 0 and self.fail_on_error:
                raise RuntimeError(f"SIMA exited with error code {exit_code}")

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
