# Running WebPython in the Browser

## Important

GitHub Pages can host the frontend, but it cannot execute a server-side CPython 3.14.6 process. Therefore WebPython's real execution path requires a backend environment.

The supported foundation path is:

```text
Browser
  ↓
WebPython API
  ↓
Docker container
  ↓
CPython 3.14.6
```

## Local machine

Run:

```bash
./scripts/start-webpython.sh
```

Then open `http://localhost:8000`.

## GitHub Codespaces

Open the repository in a Codespace, ensure Docker is available, then run:

```bash
./scripts/start-webpython.sh
```

Open the forwarded port 8000 in the browser.

## Why this matters

The browser UI must not pretend that a different Python implementation is CPython 3.14.6. The foundation deliberately keeps the exact runtime behind the API and verifies it before execution.
