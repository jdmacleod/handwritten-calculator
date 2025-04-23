# syntax=docker/dockerfile:1
# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:2.16.2-gpu AS hwcalc-backend-builder
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

# the TensorFlow image is based on Ubuntu, so we can use apt-get
# Update and install some libraries
RUN apt-get update && apt install ffmpeg libsm6 libxext6 -y

COPY requirements.txt requirements.txt
# Install any needed packages specified in requirements.txt
# RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# blinker is already installed by distutils, we will ignore it
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt --ignore-installed

EXPOSE 5001
COPY . .
ENV DATA_PATH=./
ENV MODEL_PATH=./trained_models
ENV MODEL_TYPE=mlp
CMD ["flask", "run", "--debug"]
