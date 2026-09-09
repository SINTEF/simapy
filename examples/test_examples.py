#!/usr/bin/env python3
"""Test runner for all simapy examples.

This script discovers and runs all Python examples in this directory that contain
a main method (if __name__ == "__main__": block), capturing their output and reporting any failures.
"""
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


#: The examples live here, one subdirectory per domain, and run from here.
EXAMPLES = Path(__file__).parent


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


def discover_examples(src_dir: Path) -> List[Path]:
    """Discover all Python example files with main methods below a directory.
    
    Args:
        src_dir: Directory holding the examples, one subdirectory per domain
        
    Returns:
        List of paths to Python example files that have main methods
    """
    examples = []
    for py_file in src_dir.rglob("*.py"):
        # Skip __init__.py files and any test files
        if py_file.name != "__init__.py" and "test" not in py_file.name.lower():
            # Only include files with a main method
            if has_main_method(py_file):
                examples.append(py_file)
    
    return sorted(examples)


def run_example(example_path: Path, timeout: int = 60) -> Tuple[bool, str, str]:
    """Run a single example and capture its output.
    
    Args:
        example_path: Path to the Python example file
        timeout: Maximum time to wait for execution (seconds)
        
    Returns:
        Tuple of (success, stdout, stderr)
    """
    try:
        # Change to the project root directory to ensure relative paths work
        # Examples use paths relative to this directory -- input/simo/simo.stask
        # and output/simo/condition -- so that is what they must run from.
        project_root = EXAMPLES
        
        result = subprocess.run(
            [sys.executable, str(example_path)],
            cwd=project_root,
            capture_output=True,
            text=True,
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
    src_dir = EXAMPLES

    if not src_dir.exists():
        print(f"❌ Examples directory not found: {src_dir}")
        sys.exit(1)
    
    print("🔍 Discovering examples with main methods...")
    examples = discover_examples(src_dir)
    
    if not examples:
        print("❌ No examples with main methods found!")
        sys.exit(1)
    
    print(f"📋 Found {len(examples)} examples with main methods to test")
    print()
    
    failed_examples = []
    passed_examples = []
    
    for i, example in enumerate(examples, 1):
        relative_path = example.relative_to(project_root)
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
