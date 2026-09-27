# Cloud Security & DevSecOps Engineering — lesson m04l01 — Container Hardening: Distroless & Rootless
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m04l01
# © LearnSome.tech
# Build stage: compilers and pip live here and are never shipped
FROM python:3.11-slim-bookworm AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/deps -r requirements.txt
COPY src/ ./src/

# Runtime stage: interpreter and libraries, no shell, no package manager
FROM gcr.io/distroless/python3-debian12:nonroot
WORKDIR /app
COPY --from=build /app /app
ENV PYTHONPATH=/app/deps
USER 65532:65532
ENTRYPOINT ["/usr/bin/python3", "src/server.py"]
