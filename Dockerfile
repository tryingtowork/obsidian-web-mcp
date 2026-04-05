FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY README.md .
COPY src/ ./src/

RUN pip install --no-cache-dir .

VOLUME ["/vault"]

ENV VAULT_PATH=/vault

EXPOSE 8420

CMD ["vault-mcp"]