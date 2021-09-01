"""SIMA executable wrapper class"""
import subprocess
import os
from typing import List, Sequence
from pathlib import Path


class SIMA:
    """"Run a command using SIMA runtime engine (sre executable)"""

    def __init__(self, exe=None) -> None:
        self.exe = self.__get_executable(exe)
        self.proc = None

    def __get_executable(self, exe):
        if exe:
            return exe
        exe =  os.getenv('SIMA_EXE')
        if not exe:
            raise Exception("No executable given, and SIMA_EXE environment variable is not set")
        return exe

    def run(self, workspace: str, commands: Sequence[str], env=None) -> Sequence[str]:
        """Run the sima executable and return output from standard out and standard err"""
        if not Path(self.exe).exists():
            raise Exception(f"Executable does not exist: {self.exe}")
        args = [self.exe]
        args.append("-consoleLog")
        args.append("--progress")
        args.append("-data")
        args.append(workspace)
        args = args + commands


        self.proc = subprocess.Popen(args,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,env=env)
        return self.__read_lines()


    def __read_lines(self) -> List[str]:
        proc = self.proc
        lines = []
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            lines.append(line.decode(encoding="utf8").rstrip())

        return lines

def main():
    """Run a single command and read back the result"""
    home = Path.home()
    workspace = home / "SIMA Workspaces" / "SIMAPy_test"

    sima = SIMA()
    commands = ["--help","all"]
    res = sima.run(workspace,commands)
    print(res)

if __name__ == '__main__':
    main()
