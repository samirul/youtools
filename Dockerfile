FROM python:3.12.3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/virtual-py/bin:$PATH"
WORKDIR /youtools-app
COPY requirements.txt /youtools-app/
COPY . /youtools-app/
COPY scripts.sh .
RUN python -m venv /virtual-py && \
    /virtual-py/bin/pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y postgresql-client && \
    /virtual-py/bin/pip install --no-cache-dir -r requirements.txt && \
    adduser --disabled-password --no-create-home youtools-user && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R youtools-user:youtools-user /vol && \
    chmod -R 755 /vol && \
    chmod +x scripts.sh

USER youtools-user

CMD ["./scripts.sh"]