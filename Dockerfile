FROM python:3.12.3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 5672
EXPOSE 15672
WORKDIR /youtools-app
COPY requirements.txt /youtools-app/
COPY . /youtools-app/
RUN python -m venv /virtual-py && \
    /virtual-py/bin/pip install --upgrade pip && \
    apk add --no-cache bash && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /virtual-py/bin/pip install --no-cache-dir -r requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home youtools-user && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/static/logo && \
    mkdir -p /vol/web/media && \
    chown -R youtools-user:youtools-user /vol && \
    chmod -R 755 /vol

COPY ./logo /vol/web/static/logo

COPY ./avatar /vol/web/media/profile-pic

ENV PATH="/scripts:/virtual-py/bin:$PATH"

USER youtools-user