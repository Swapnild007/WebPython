# WebPython Foundation Architecture

```text
┌──────────────┐
│   Browser    │
│ Web IDE      │
└──────┬───────┘
       │ HTTP / JSON
       ▼
┌──────────────┐
│ WebPython    │
│ Internal API │
└──────┬───────┘
       ▼
┌──────────────┐
│ Execution    │
│ Manager      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Project      │
│ Workspace    │
└──────┬───────┘
       ▼
┌──────────────┐
│ CPython      │
│ 3.14.6       │
└──────────────┘
```

## Responsibilities

### Browser
Editor, project navigation, lifecycle controls, and output display.

### Internal API
The stable communication boundary between UI and execution services.

### Execution manager
Runtime verification, build validation, process execution, timeout, and result collection.

### Workspace
Project files and future package/dependency metadata.

### Runtime
The only accepted execution interpreter is CPython 3.14.6.

## Security direction

Foundation uses workspace path validation, execution timeouts, and containerization as an initial boundary. Production hardening will add stronger per-run isolation, resource limits, network controls, and authentication as required.