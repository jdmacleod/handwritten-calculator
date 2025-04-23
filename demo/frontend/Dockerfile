# syntax=docker/dockerfile:1
FROM python:3.13-alpine AS hwcalc-frontend-builder
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Update the alpine image and install some libraries
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .
ENV MODEL_TYPE=mlp
CMD ["flask", "run", "--debug"]
