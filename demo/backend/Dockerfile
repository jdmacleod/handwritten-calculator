# syntax=docker/dockerfile:1
# Stage 1
# Use a Slim release as a parent image, installing dependencies
FROM python:3.11-slim-buster AS hwcalc-backend-builder
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Stage 2 - copy only necessary files
FROM python:3.11-slim-buster AS hwcalc-backend-svc
WORKDIR /app

COPY --from=hwcalc-backend-builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001
ENV DATA_PATH=./
ENV MODEL_PATH=./trained_models
ENV MODEL_TYPE=mlp

EXPOSE 5001

CMD ["python", "-m", "flask", "run"]
