"""Backend Flask application for the demo project."""

import os

from flask import Flask, jsonify

from .app_config import APP_NAME, APP_VERSION, MODEL_TYPE  # local package import
from .views import CaptureItemView, PredictDigitView, PredictSymbolView

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """Return a landing page response.

    Returns:
        str: _description_
    """
    return jsonify(
        {
            "comment": "API Endpoint",
            "name": APP_NAME,
            "version": APP_VERSION,
            "api_url": "/api/v1",
        }
    )


@app.route("/heartbeat")
def heartbeat() -> str:
    """Return a heartbeat response.

    Returns:
        str: _description_
    """
    return jsonify(
        {
            "name": APP_NAME,
            "version": APP_VERSION,
            "model": MODEL_TYPE,
            "status": "healthy",
        }
    )


app.add_url_rule(
    "/api/v1/predict-digit",
    view_func=PredictDigitView.as_view("predict_digit"),
    methods=["POST"],
)

app.add_url_rule(
    "/api/v1/predict-symbol",
    view_func=PredictSymbolView.as_view("predict_symbol"),
    methods=["POST"],
)

app.add_url_rule(
    "/api/v1/capture-item",
    view_func=CaptureItemView.as_view("capture_item"),
    methods=["POST"],
)

if __name__ == "__main__":
    port = int(os.environ.get("FLASK_RUN_PORT", 5001))
    app.run(host="0.0.0.0", port=port)
