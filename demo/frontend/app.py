"""Frontend application endpoints."""

import requests.exceptions
from flask import Flask, jsonify, render_template, request

from .app_config import API_URL, APP_NAME, APP_VERSION
from .model import (
    capture_item_from_input,
    predict_digit_from_input,
    predict_symbol_from_input,
)

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """The home page of the application."""
    return render_template("home.html")


@app.route("/about")
def about() -> str:
    """The about page of the application."""
    return render_template("about.html", app_name=APP_NAME, app_version=APP_VERSION)


@app.route("/capture")
def capture() -> str:
    """Capture page of the application."""
    return render_template("capture.html")


@app.route("/digit")
def digit() -> str:
    """Digit recognition page of the application."""
    return render_template("digit.html")


@app.route("/symbol")
def symbol() -> str:
    """Symbol recognition page of the application."""
    return render_template("symbol.html")


@app.route("/predict-digit", methods=["GET", "POST"])
def predict_digit() -> str:
    """Digit prediction endpoint."""
    raw_input = request.get_json(silent=True)

    app.logger.info("Sending raw_input: %s", raw_input)
    try:
        prediction, confidence = predict_digit_from_input(raw_input)
        response = {"prediction": str(prediction), "confidence": str(confidence)}
    except requests.exceptions.ConnectionError as e:
        app.logger.error("Connection Error during prediction: %s", e)
        exception_message = f"Error connecting to backend URL {API_URL}. Check if the backend is running."
        response = {"prediction": "?", "confidence": "0", "message": exception_message}
    return jsonify(response)


@app.route("/predict-symbol", methods=["GET", "POST"])
def predict_symbol() -> str:
    """Symbol prediction endpoint."""
    raw_input = request.get_json(silent=True)

    app.logger.info("Sending raw_input: %s", raw_input)
    try:
        prediction, confidence = predict_symbol_from_input(raw_input)
        response = {"prediction": str(prediction), "confidence": str(confidence)}
    except requests.exceptions.ConnectionError as e:
        app.logger.error("Connection Error during prediction: %s", e)
        exception_message = f"Error connecting to backend URL {API_URL}. Check if the backend is running."
        response = {"prediction": "?", "confidence": "0", "message": exception_message}
    return jsonify(response)


@app.route("/capture-item", methods=["GET", "POST"])
def capture_item() -> str:
    """Capture item endpoint."""
    raw_input = request.get_json(silent=True)

    app.logger.info("Sending raw_input: %s", raw_input)
    try:
        item_filename = capture_item_from_input(raw_input)
        response = {"item_filename": str(item_filename)}

    except requests.exceptions.ConnectionError as e:
        app.logger.error("Connection Error during capture: %s", e)
        exception_message = f"Error connecting to backend URL {API_URL}. Check if the backend is running."
        response = {"item_filename": "", "message": exception_message}

    return jsonify(response)
