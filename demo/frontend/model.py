"""Models for the frontend."""

import requests

from .app_config import API_TIMEOUT, API_URL  # local package import
from .core import logger  # local package import


def predict_digit_from_input(image: str) -> tuple[int, float]:
    """Predict a digit from an input image.

    Args:
        image (_type_): _description_

    Raises:
        Exception: _description_

    Returns:
        tuple: prediction and confidence
    """
    logger.debug(f"POST with json = {image}")
    try:
        response = requests.post(
            f"{API_URL}/predict-digit", json=image, timeout=API_TIMEOUT
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        raise

    logger.debug(f"Got response {response.json()}")
    logger.debug(f"Got response content {response.content.decode('utf-8')}")
    logger.debug(f"Got response text {response.text}")

    response_data = response.json()
    prediction = response_data["prediction"]
    confidence = response_data["confidence"]
    logger.info(f"Returning prediction: {prediction}, confidence: {confidence}")
    return prediction, confidence


def predict_symbol_from_input(image: str) -> tuple[int, float]:
    """Predict a symbol from an input image.

    Args:
        image (str): encoded image in JSON format

    Raises:
        Exception: _description_

    Returns:
        tuple: prediction and confidence
    """
    logger.debug(f"POST with json = {image}")
    try:
        response = requests.post(
            f"{API_URL}/predict-symbol", json=image, timeout=API_TIMEOUT
        )
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Is the backend running - Connection error: {e}")
        raise

    logger.debug(f"Got response {response.json()}")
    logger.debug(f"Got response content {response.content.decode('utf-8')}")
    logger.debug(f"Got response text {response.text}")

    response_data = response.json()
    prediction = response_data["prediction"]
    confidence = response_data["confidence"]
    logger.info(f"Returning prediction: {prediction}, confidence: {confidence}")
    return prediction, confidence


def capture_item_from_input(image: str) -> str:
    """Capture an input image to a file.

    Args:
        image (str): encoded image in JSON format.

    Raises:
        Exception: _description_

    Returns:
        str: the filename of the captured image
    """
    logger.debug(f"POST with json = {image}")
    try:
        response = requests.post(
            f"{API_URL}/capture-item", json=image, timeout=API_TIMEOUT
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        raise

    logger.debug(f"Got response {response.json()}")
    logger.debug(f"Got response content {response.content.decode('utf-8')}")
    logger.debug(f"Got response text {response.text}")

    response_data = response.json()
    item_filename = response_data["capture_file"]
    logger.info(f"Returning item_filename: {item_filename}")
    return item_filename
