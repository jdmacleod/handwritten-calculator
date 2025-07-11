"""Configure the frontend flask app."""

import logging
import os

logger = logging.getLogger(__name__)

APP_NAME = "handwritten-calculator-frontend"

APP_VERSION = "0.2.0"

APP_ROOT = os.getenv("APP_ROOT", "/opt/handwritten-calculator")

API_URL = os.getenv("API_URL", "http://localhost:5001/api/v1")

logger.info("using api url %s", API_URL)

API_TIMEOUT = int(os.getenv("API_TIMEOUT", "2"))
