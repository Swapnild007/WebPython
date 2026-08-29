from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .executor import build_python, execute_python
from .runtime import EXPECTED_IMPLEMENTATION, EXPECTED_VERSION, inspect_runtime, require_runtime
from .workspace import WORKSPACE_ROOT, file_path, project_path

ROOT = WORKSPACE_ROOT.parent
FRONTEND = ROOT / "frontend"

app = FastAPI(title="WebPython API", version="0.2.0")


class ProjectRequest(BaseModel):
    project: str = "default"


class FileRequest(ProjectRequest):
    filename: str = "main.py"
    code: str = ""


def save_source(request: FileRequest):
    path = file_path(request.project, request.filename)
    path.write_text(request.code, encoding="utf-8")
    return project_path(request.project), path


@app.get("/")
def index():
    return FileResponse(FRONTEND / "index.html")


@app.get("/api/health")
def health():
    try:
        runtime = inspect_runtime()
        ok = runtime["implementation"] == EXPECTED_IMPLEMENTATION and runtime["version"] == EXPECTED_VERSION
        return {"ok": ok, "runtime": runtime}
    except Exception as exc:
        return {"ok": False, "required": f"{EXPECTED_IMPLEMENTATION} {EXPECTED_VERSION}", "error": str(exc)}


@app.get("/api/projects")
def list_projects():
    return {"projects": sorted(p.name for p in WORKSPACE_ROOT.iterdir() if p.is_dir())}


@app.get("/api/files")
def list_files(project: str = "default"):
    root = project_path(project)
    return {"project": project, "files": sorted(str(p.relative_to(root)) for p in root.rglob("*") if p.is_file())}


@app.get("/api/files/read")
def read_file(project: str = "default", filename: str = "main.py"):
    path = file_path(project, filename)
    if not path.exists():
        raise HTTPException(404, "File not found")
    return {"project": project, "filename": filename, "code": path.read_text(encoding="utf-8")}


@app.post("/api/files/write")
def write_file(request: FileRequest):
    _, path = save_source(request)
    return {"success": True, "project": request.project, "filename": str(path.relative_to(project_path(request.project)))}


@app.post("/api/build")
def build(request: FileRequest):
    try:
        root, path = save_source(request)
        return build_python(root, path)
    except RuntimeError as exc:
        raise HTTPException(503, str(exc)) from exc


@app.post("/api/run")
def run(request: ProjectRequest):
    try:
        project_path(request.project)
        return {"success": True, "stage": "RUN", "runtime": require_runtime()}
    except RuntimeError as exc:
        raise HTTPException(503, str(exc)) from exc


@app.post("/api/execute")
def execute(request: FileRequest):
    try:
        root, path = save_source(request)
        return execute_python(root, path)
    except RuntimeError as exc:
        raise HTTPException(503, str(exc)) from exc
