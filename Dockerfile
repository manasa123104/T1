# Build stage: install dependencies and run the unit tests.
FROM python:3.12-slim AS test
WORKDIR /src
COPY . .
RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || pip install --no-cache-dir pytest
RUN if [ -d tests ]; then python -m pytest -q; else python -m compileall -q app; fi

# Runtime stage: application code only.
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1 PORT=8091
COPY --from=test /src/app ./app
EXPOSE 8091
USER 1000
CMD ["python", "-m", "app.device_provisioning"]
