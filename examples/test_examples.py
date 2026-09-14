#!/usr/bin/env python3
"""Test runner for all simapy examples.

This script discovers and runs all Python examples in this directory that contain
a main method (if __name__ == "__main__": block), capturing their output and reporting any failures.

Pass one or more directory names to run only those groups::

    python test_examples.py               # every group that can run unattended
    python test_examples.py riflex simo   # only those two directories
    python test_examples.py metocean      # named explicitly, so it runs anyway

Which groups are runnable is decided here rather than by the caller, so CI does
not have to carry a second copy of the list and keep it in step.
"""
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


#: The examples live here, one subdirectory per domain, and run from here.
EXAMPLES = Path(__file__).parent

#: An example that drives SRE runs a solver, so minutes rather than seconds.
DEFAULT_TIMEOUT = int(os.environ.get("EXAMPLE_TIMEOUT", "900"))

#: Groups left out when no group is named, and why. Naming one runs it anyway.
NOT_UNATTENDED = {
    "metocean": "downloads hindcast data and needs metocean_api/metocean_stats",
}


def has_main_method(file_path: Path) -> bool:
    """Check if a Python file contains a main method.
    
    Looks for the pattern 'if __name__ == "__main__":' in the file.
    
    Args:
        file_path: Path to the Python file to check
        
    Returns:
        True if the file has a main method, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for the common main method pattern
            if re.search(r'if\s+__name__\s*==\s*["\']__main__["\'](\s*):', content):
                return True
        return False
    except Exception:
        # If there's an error reading the file, assume it doesn't have a main method
        return False


def runnable_groups(src_dir: Path) -> List[str]:
    """The groups to run when the caller names none: every one but NOT_UNATTENDED.

    Args:
        src_dir: Directory holding the examples, one subdirectory per domain

    Returns:
        Sorted group names, each holding at least one example with a main method
    """
    found = {path.relative_to(src_dir).parts[0] for path in discover_examples(src_dir, [])}
    return sorted(found - set(NOT_UNATTENDED))


def discover_examples(src_dir: Path, groups: List[str] = None) -> List[Path]:
    """Discover all Python example files with main methods below a directory.

    Args:
        src_dir: Directory holding the examples, one subdirectory per domain
        groups: Names of the subdirectories to search; every directory when empty

    Returns:
        List of paths to Python example files that have main methods
    """
    roots = [src_dir / group for group in groups] if groups else [src_dir]
    examples = []
    for py_file in (f for root in roots for f in root.rglob("*.py")):
        # Skip __init__.py files and any test files
        if py_file.name != "__init__.py" and "test" not in py_file.name.lower():
            # Only include files with a main method
            if has_main_method(py_file):
                examples.append(py_file)
    
    return sorted(examples)


def run_example(example_path: Path, timeout: int = DEFAULT_TIMEOUT) -> Tuple[bool, str, str]:
    """Run a single example and capture its output.
    
    Args:
        example_path: Path to the Python example file
        timeout: Maximum time to wait for execution (seconds)
        
    Returns:
        Tuple of (success, stdout, stderr)
    """
    try:
        # Examples use paths relative to the examples directory --
        # input/simo/simo.stask and output/simo/condition -- so that is what
        # they must run from.
        result = subprocess.run(
            [sys.executable, str(example_path)],
            cwd=EXAMPLES,
            capture_output=True,
            text=True,
            # An example's own output must not be able to fail the decode.
            encoding="utf-8",
            errors="replace",
            timeout=timeout
        )
        
        success = result.returncode == 0
        return success, result.stdout, result.stderr
        
    except subprocess.TimeoutExpired:
        return False, "", f"Example timed out after {timeout} seconds"
    except Exception as e:
        return False, "", f"Failed to run example: {str(e)}"


def main():
    """Main test runner function."""
    # The report is full of emoji, and a Windows console defaults to cp1252,
    # where printing one raises UnicodeEncodeError.
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")

    src_dir = EXAMPLES
    groups = sys.argv[1:]

    if not src_dir.exists():
        print(f"❌ Examples directory not found: {src_dir}")
        sys.exit(1)

    missing = [group for group in groups if not (src_dir / group).is_dir()]
    if missing:
        available = sorted({p.relative_to(src_dir).parts[0] for p in discover_examples(src_dir)})
        print(f"❌ No such example group: {', '.join(missing)}")
        print(f"   Available: {', '.join(available)}")
        sys.exit(1)

    # No group named means every group that can run unattended. A caller that
    # names one gets it regardless, so the skip is a default and not a ban.
    if not groups:
        groups = runnable_groups(src_dir)
        for group, reason in sorted(NOT_UNATTENDED.items()):
            print(f"⏭️  Skipping {group}: {reason}")

    print("🔍 Discovering examples with main methods...")
    examples = discover_examples(src_dir, groups)

    if not examples:
        print("❌ No examples with main methods found!")
        sys.exit(1)

    print(f"📋 Found {len(examples)} examples with main methods to test")
    print()
    
    failed_examples = []
    passed_examples = []
    
    for i, example in enumerate(examples, 1):
        relative_path = example.relative_to(EXAMPLES)
        print(f"[{i}/{len(examples)}] Running {relative_path}...")
        
        success, stdout, stderr = run_example(example)
        
        if success:
            print(f"✅ {relative_path} - PASSED")
            passed_examples.append(relative_path)
            if stdout.strip():
                print(f"   Output: {stdout.strip()[:100]}{'...' if len(stdout.strip()) > 100 else ''}")
        else:
            print(f"❌ {relative_path} - FAILED")
            failed_examples.append((relative_path, stderr))
            if stderr.strip():
                print(f"   Error: {stderr.strip()}")
        
        print()
    
    # Summary
    print("=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"✅ Passed: {len(passed_examples)}")
    print(f"❌ Failed: {len(failed_examples)}")
    print(f"📈 Success Rate: {len(passed_examples)}/{len(examples)} ({len(passed_examples)/len(examples)*100:.1f}%)")
    
    if failed_examples:
        print("\n❌ FAILED EXAMPLES:")
        for example, error in failed_examples:
            print(f"  - {example}")
            if error:
                print(f"    {error}")
    
    if passed_examples:
        print("\n✅ PASSED EXAMPLES:")
        for example in passed_examples:
            print(f"  - {example}")
    
    # Exit with error code if any tests failed
    if failed_examples:
        sys.exit(1)
    else:
        print("\n🎉 All examples passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
