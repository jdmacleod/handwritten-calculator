from app_config import MODEL_PATH, MODEL_TYPE
from core import logger  # local package import
from flask import Response, jsonify, render_template, request
from flask.views import MethodView, View
from services import CaptureItemService, PredictService


class IndexView(View):
    def dispatch_request(self):
        return render_template("index.html")


class PredictDigitView(MethodView):
    def post(self):
        model_path = MODEL_PATH / f"hc-digits-{MODEL_TYPE}-model.keras"
        service = PredictService(model_path=model_path)
        image_data_uri = request.json["image"]
        logger.debug(f"Received image_data_uri: {image_data_uri}")
        prediction, confidence = service.handle(image_data_uri)

        response = {"prediction": str(prediction), "confidence": str(confidence)}

        return jsonify(response)


class PredictSymbolView(MethodView):
    def post(self):
        model_path = MODEL_PATH / f"hc-symbols-{MODEL_TYPE}-model.keras"
        service = PredictService(model_path=model_path)
        image_data_uri = request.json["image"]
        logger.debug(f"Received image_data_uri: {image_data_uri}")
        prediction, confidence = service.handle(image_data_uri)

        response = {"prediction": str(prediction), "confidence": str(confidence)}

        return jsonify(response)


class CaptureItemView(MethodView):
    def post(self):
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
