# #### Base Layer
# FROM python:3.10-slim AS base

# ENV POETRY_NO_INTERACTION=1 \
#     POETRY_VIRTUALENVS_IN_PROJECT=1 \
#     POETRY_VIRTUALENVS_CREATE=1 \
#     POETRY_CACHE_DIR=/tmp/poetry_cache \
#     POETRY_HOME="/opt/poetry" \
#     PYSETUP_PATH="/opt/pysetup" \
#     VENV_PATH="/opt/pysetup/.venv"

# ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# #### Builder Layer

# FROM base AS builder

# COPY apt.conf /etc/apt/
# RUN apt-get update && apt-get install -y  --no-install-recommends libpq-dev

# WORKDIR $PYSETUP_PATH
# COPY pyproject.toml poetry.lock* ./

# RUN pip install poetry
# RUN poetry install  --only main  && rm -rf $POETRY_CACHE_DIR;

# # RUNTIME LAYER
# FROM base AS runtime
# COPY --from=builder ${VENV_PATH} ${VENV_PATH}
# WORKDIR /app
# COPY . .
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh
# EXPOSE 8000

# CMD ["/entrypoint.sh"]




FROM python:3.10-slim
RUN mkdir -p /opt/pysetup/.venv


ENV PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$VENV_PATH/bin:$PATH"
ENV VIRTUAL_ENV="$VENV_PATH"
ENV PIP_INDEX_URL=https://repo.mofid.dev/artifactory/api/pypi/pypi/simple


WORKDIR /app
COPY requirements.txt  requirements.txt
RUN python -m pip install  --upgrade pip
RUN python -m pip install  --no-cache-dir -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

CMD ["python"]
