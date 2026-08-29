import os
import subprocess
import sys

EXPECTED_IMPLEMENTATION = "CPython"
EXPECTED_VERSION = "3.14.6"
PYTHON_EXECUTABLE = os.environ.get("WEBPYTHON_PYTHON", sys.executable)


def inspect_runtime() -> dict:
    process = subprocess.run(
        [PYTHON_EXECUTABLE, "-c", "import platform,sys; print(platform.python_implementation()); print(platform.python_version()); print(sys.executable)"],
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    if process.returncode != 0:
        raise RuntimeError(process.stderr.strip() or "Unable to inspect Python runtime")
    lines = process.stdout.strip().splitlines()
    return {
        "implementation": lines[0] if len(lines) > 0 else "",
        "version": lines[1] if len(lines) > 1 else "",
        "executable": lines[2] if len(lines) > 2 else PYTHON_EXECUTABLE,
        "required": f"{EXPECTED_IMPLEMENTATION} {EXPECTED_VERSION}",
    }


def require_runtime() -> dict:
    info = inspect_runtime()
    if info["implementation"] != EXPECTED_IMPLEMENTATION or info["version"] != EXPECTED_VERSION:
        raise RuntimeError(
            f"Wrong Python runtime. Required {EXPECTED_IMPLEMENTATION} {EXPECTED_VERSION}; "
            f"detected {info['implementation']} {info['version']}"
        )
    return info
