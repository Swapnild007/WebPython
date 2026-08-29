# WebPython Project Specification

## Goal
Build a general-purpose browser-based Python development environment that can grow from tiny scripts to large multi-file applications.

## Core workflow

**BUILD → RUN → EXECUTE**

## Foundation requirements

- Genuine CPython 3.14.6 execution target
- Browser IDE
- Internal HTTP API
- Project and file management
- Runtime health verification
- stdout / stderr capture
- exit-code reporting
- execution timeout
- workspace isolation boundary
- Docker deployment path

## Explicit exclusions

- Termux
- RTA-specific functionality
- fake Python runtimes
- silent fallback to another Python version

## Definition of done for Foundation

The system must execute a simple Python program and visibly report verified CPython 3.14.6, successful output, and exit code 0.