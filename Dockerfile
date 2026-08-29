FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential wget ca-certificates \
    libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
    libffi-dev liblzma-dev libncursesw5-dev uuid-dev tk-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt
RUN wget -q https://www.python.org/ftp/python/3.14.6/Python-3.14.6.tgz \
 && tar -xzf Python-3.14.6.tgz \
 && cd Python-3.14.6 \
 && ./configure --prefix=/opt/cpython-3.14.6 \
 && make -j"$(nproc)" \
 && make install \
 && cd /opt \
 && rm -rf Python-3.14.6 Python-3.14.6.tgz

ENV WEBPYTHON_PYTHON=/opt/cpython-3.14.6/bin/python3
ENV PATH=/opt/cpython-3.14.6/bin:$PATH

WORKDIR /app
COPY backend/requirements.txt backend/requirements.txt
RUN /opt/cpython-3.14.6/bin/python3 -m pip install --no-cache-dir -r backend/requirements.txt
COPY . .

EXPOSE 8000
CMD ["/opt/cpython-3.14.6/bin/python3","-m","uvicorn","backend.app.main:app","--host","0.0.0.0","--port","8000"]
