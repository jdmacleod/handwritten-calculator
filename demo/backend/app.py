import os

from app_config import APP_NAME, APP_VERSION, MODEL_TYPE   # local package import
from flask import Flask, jsonify
from views import (CaptureItemView, IndexView, PredictDigitView,
                   PredictSymbolView)

app = Flask(__name__)


@app.route("/heartbeat")
def heartbeat():
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

app.add_url_rule("/", view_func=IndexView.as_view("index"), methods=["GET"])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
