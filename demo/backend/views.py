"""Views for the backend application."""

from flask import jsonify, render_template, request
from flask.views import MethodView, View

from .app_config import MODEL_PATH, MODEL_TYPE
from .core import logger  # local package import
from .services import CaptureItemService, PredictService


class IndexView(View):
    """The index view for the application."""

    def dispatch_request(self) -> str:
        """Render the index page."""
        return render_template("index.html")


class PredictDigitView(MethodView):
    """The view for predicting digits."""

    def post(self) -> str:
        """Handle the prediction request for digits.
        Returns:
            str: JSON response with prediction and confidence.
        """
        model_path = MODEL_PATH / f"hc-digits-{MODEL_TYPE}-model.keras"
        service = PredictService(model_path=model_path)
        image_data_uri = request.json["image"]
        logger.debug(f"Received image_data_uri: {image_data_uri}")
        prediction, confidence = service.handle(image_data_uri)

        response = {"prediction": str(prediction), "confidence": str(confidence)}

        return jsonify(response)


class PredictSymbolView(MethodView):
    """The view for predicting symbols."""

    def post(self) -> str:
        """Handle the prediction request for symbols.
        Returns:
            str: JSON response with prediction and confidence.
        """
        model_path = MODEL_PATH / f"hc-symbols-{MODEL_TYPE}-model.keras"
        service = PredictService(model_path=model_path)
        image_data_uri = request.json["image"]
        logger.debug(f"Received image_data_uri: {image_data_uri}")
        prediction, confidence = service.handle(image_data_uri)

        response = {"prediction": str(prediction), "confidence": str(confidence)}

        return jsonify(response)


class CaptureItemView(MethodView):
    """The view for capturing items."""

    def post(self) -> str:
        """Handle the capture item request.
        Returns:
            str: JSON response with the capture file path.
        """
        service = CaptureItemService()
        image_data_uri = request.json["image"]
        logger.debug(f"Received image_data_uri: {image_data_uri}")
        symbol_name = request.json["symbolName"]
        logger.debug(f"Received symbol name: {symbol_name}")
        uuid = request.json["uuid"]
        logger.debug(f"Received uuid: {uuid}")
        capture_filename = service.handle(image_data_uri, symbol_name, uuid)

        response = {"capture_file": str(capture_filename)}

        return jsonify(response)
