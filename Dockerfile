FROM python:3.13.0-slim-bookworm AS app

WORKDIR /app

ARG UID=1000
ARG GID=1000

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && groupadd -g "${GID}" python \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python \
  && mkdir -p /public \
  && chown python:python -R /public /app

USER python

COPY --chown=python:python requirements*.txt ./
COPY --chown=python:python bin/ ./bin

RUN chmod 0755 bin/* && bin/pip3-install

ARG DEBUG="false"
ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

COPY --chown=python:python src/static/* /app/public/
COPY --chown=python:python . .

WORKDIR /app/src

RUN if [ "${DEBUG}" = "false" ]; then \
  SECRET_KEY=dummyvalue python3 manage.py collectstatic --no-input; \
    else mkdir -p /app/public; fi

EXPOSE 8000

CMD ["gunicorn", "-c", "python:config.gunicorn", "config.wsgi"]
