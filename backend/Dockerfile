FROM python:3.15.2-slim

WORKDIR /app

COPY pyproject.toml ./

COPY src/ ./src/

RUN pip install .

CMD ["python", "-m", "src.main"]