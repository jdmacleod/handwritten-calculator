"""Configure the frontend flask app."""

import logging
import os

logger = logging.getLogger(__name__)

APP_NAME = "handwritten-calculator-frontend"

APP_VERSION = "0.1.0"

APP_ROOT = os.getenv("APP_ROOT", "/opt/handwritten-calculator")

API_URL = os.getenv("API_URL", "http://localhost:5000/api/v1")

logger.info(f"using api url {API_URL}")
