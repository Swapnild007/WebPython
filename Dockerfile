FROM python:3.14.6-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    WEBPYTHON_PYTHON=/usr/local/bin/python3

WORKDIR /app

COPY backend/requirements.txt backend/requirements.txt
RUN python -m pip install --no-cache-dir -r backend/requirements.txt

COPY backend ./backend
COPY frontend ./frontend
COPY docs ./docs
COPY README.md LICENSE NOTICE.md THIRD_PARTY_LICENSES.md ./

EXPOSE 8000

CMD ["python","-m","uvicorn","backend.app.main:app","--host","0.0.0.0","--port","8000"]
