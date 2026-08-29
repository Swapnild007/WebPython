# WebPython

**Build. Run. Execute.**

A browser-based Python development environment designed to support small, medium, and large Python projects.

## Foundation

- Browser IDE
- Internal API boundary
- Project workspace
- Build / Run / Execute lifecycle
- Runtime verification
- stdout / stderr / exit code
- Execution timeout
- Docker-ready execution environment
- Target runtime: **CPython 3.14.6**

## Principles

1. No Termux.
2. No fake interpreter.
3. Never claim execution success without verifying the runtime.
4. Keep architecture and decisions documented in the repository.

## Architecture

```text
Browser
  ↓
WebPython API
  ↓
Execution Manager
  ↓
Isolated Workspace
  ↓
CPython 3.14.6
```

## Project status

**Foundation: initialized**

The first milestone is to make `BUILD → RUN → EXECUTE` work end-to-end with verified CPython 3.14.6 before adding advanced features.