FROM python:3.11.4-slim-bullseye AS builder

WORKDIR /the_factory_bot_task
COPY poetry.lock pyproject.toml ./

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}
COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]