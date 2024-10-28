from flask import Flask, jsonify, render_template, request
from model import (capture_item_from_input, predict_digit_from_input,
                   predict_symbol_from_input)

from app_config import APP_NAME, APP_VERSION

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html", app_name=APP_NAME, app_version=APP_VERSION)


@app.route("/capture")
def capture():
    return render_template("capture.html")


@app.route("/digit")
def digit():
    return render_template("digit.html")


@app.route("/symbol")
def symbol():
    return render_template("symbol.html")


@app.route("/predict-digit", methods=["GET", "POST"])
def predict_digit():
    raw_input = request.get_json(silent=True)

    app.logger.info(f"Sending raw_input: {raw_input}")
    prediction, confidence = predict_digit_from_input(raw_input)

    response = {"prediction": str(prediction), "confidence": str(confidence)}

    return jsonify(response)


@app.route("/predict-symbol", methods=["GET", "POST"])
def predict_symbol():
    raw_input = request.get_json(silent=True)

    app.logger.info(f"Sending raw_input: {raw_input}")
    prediction, confidence = predict_symbol_from_input(raw_input)

    response = {"prediction": str(prediction), "confidence": str(confidence)}

    return jsonify(response)


@app.route("/capture-item", methods=["GET", "POST"])
def capture_item():
    raw_input = request.get_json(silent=True)

    app.logger.info(f"Sending raw_input: {raw_input}")
    item_filename = capture_item_from_input(raw_input)

    response = {"item_filename": str(item_filename)}

    return jsonify(response)
