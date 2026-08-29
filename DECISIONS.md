# Architecture Decisions

## D001 — Runtime
Target execution runtime: **CPython 3.14.6**.

## D002 — Platform
WebPython is a general-purpose project, not an RTA-specific tool.

## D003 — Termux
Termux is not part of the architecture.

## D004 — Lifecycle
The primary developer workflow is **BUILD → RUN → EXECUTE**.

## D005 — API
Browser-to-runtime communication uses an internal API boundary.

## D006 — Runtime truth
The application must verify the interpreter identity and exact version before execution. No silent fallback.

## D007 — Project memory
Important requirements, decisions, architecture, tests, and changes are stored in repository files so the conversation is not the only source of project state.