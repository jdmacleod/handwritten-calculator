import requests
from app_config import API_URL  # local package import
from core import logger  # local package import


def predict_digit_from_input(image):
    logger.debug(f"POST with json = {image}")
    response = requests.post(f"{API_URL}/predict-digit", json=image)
    if response:
        logger.debug(f"Got response {response.json()}")
        logger.debug(f"Got response content {response.content}")
        logger.debug(f"Got response text {response.text}")

        response_data = response.json()
        prediction = response_data["prediction"]
        confidence = response_data["confidence"]
        logger.info(f"Returning prediction: {prediction}, confidence: {confidence}")
        return prediction, confidence
    else:
        raise Exception(f"Non-success status code: {response.status_code}")


def predict_symbol_from_input(image):
    logger.debug(f"POST with json = {image}")
    response = requests.post(f"{API_URL}/predict-symbol", json=image)
    if response:
        logger.debug(f"Got response {response.json()}")
        logger.debug(f"Got response content {response.content}")
        logger.debug(f"Got response text {response.text}")

        response_data = response.json()
        prediction = response_data["prediction"]
        confidence = response_data["confidence"]
        logger.info(f"Returning prediction: {prediction}, confidence: {confidence}")
        return prediction, confidence
    else:
        raise Exception(f"Non-success status code: {response.status_code}")


def capture_item_from_input(image):
    logger.debug(f"POST with json = {image}")
    response = requests.post(f"{API_URL}/capture-item", json=image)
    if response:
        logger.debug(f"Got response {response.json()}")
        logger.debug(f"Got response content {response.content}")
        logger.debug(f"Got response text {response.text}")

        response_data = response.json()
        item_filename = response_data["capture_file"]
        logger.info(f"Returning item_filename: {item_filename}")
        return item_filename
    else:
        raise Exception(f"Non-success status code: {response.status_code}")
