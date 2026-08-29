from pathlib import Path

from fastapi import HTTPException

ROOT = Path(__file__).resolve().parents[2]
WORKSPACE_ROOT = ROOT / "workspace"
WORKSPACE_ROOT.mkdir(parents=True, exist_ok=True)


def project_path(project: str) -> Path:
    candidate = Path(project)
    if not project or candidate.is_absolute() or candidate.name != project or project in {".", ".."}:
        raise HTTPException(400, "Invalid project name")
    path = (WORKSPACE_ROOT / project).resolve()
    if path.parent != WORKSPACE_ROOT.resolve():
        raise HTTPException(400, "Project path escapes workspace")
    path.mkdir(parents=True, exist_ok=True)
    return path


def file_path(project: str, filename: str) -> Path:
    root = project_path(project)
    relative = Path(filename)
    if not filename or relative.is_absolute() or ".." in relative.parts:
        raise HTTPException(400, "Invalid filename")
    path = (root / relative).resolve()
    if root != path and root not in path.parents:
        raise HTTPException(400, "File path escapes project workspace")
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
