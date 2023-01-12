FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:/"

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY . .

RUN poetry install --no-dev

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]