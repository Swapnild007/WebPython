import subprocess
from pathlib import Path

from .runtime import require_runtime

DEFAULT_BUILD_TIMEOUT = 30
DEFAULT_EXECUTION_TIMEOUT = 60


def build_python(project_root: Path, source_file: Path) -> dict:
    runtime = require_runtime()
    process = subprocess.run(
        [runtime["executable"], "-m", "py_compile", str(source_file)],
        cwd=project_root,
        capture_output=True,
        text=True,
        timeout=DEFAULT_BUILD_TIMEOUT,
        check=False,
    )
    return {
        "success": process.returncode == 0,
        "stage": "BUILD",
        "stdout": process.stdout,
        "stderr": process.stderr,
        "exit_code": process.returncode,
        "runtime": runtime,
    }


def execute_python(project_root: Path, source_file: Path) -> dict:
    runtime = require_runtime()
    try:
        process = subprocess.run(
            [runtime["executable"], str(source_file)],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=DEFAULT_EXECUTION_TIMEOUT,
            check=False,
        )
        return {
            "success": process.returncode == 0,
            "stage": "EXECUTE",
            "stdout": process.stdout,
            "stderr": process.stderr,
            "exit_code": process.returncode,
            "runtime": runtime,
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "success": False,
            "stage": "EXECUTE",
            "stdout": exc.stdout or "",
            "stderr": (exc.stderr or "") + "\nExecution timed out after 60 seconds.",
            "exit_code": 124,
            "runtime": runtime,
        }
