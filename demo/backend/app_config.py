"""Configure the backend flask app."""

import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

APP_NAME = "handwritten-calculator-backend"

APP_VERSION = "0.1.0"

APP_ROOT = os.getenv("APP_ROOT", "/opt/handwritten-calculator")

API_URL = os.getenv("API_URL", "http://localhost:5000")

# Path where the trained models are stored
MODEL_PATH = Path(os.getenv("MODEL_PATH", "./"))

# Set the type of model to be used by the demo
MODEL_TYPE = os.getenv("MODEL_TYPE", "mlp")

logger.info("using model type %s", MODEL_TYPE)

# Path for all data used in API
DATA_PATH = Path(os.getenv("DATA_PATH", "/data"))

# Prefix for storing input symbol images
CAPTURE_PREFIX = "capture"

# Path where all captured symbol images are stored
CAPTURE_PATH = DATA_PATH / CAPTURE_PREFIX
logger.info("using path %s to store captured symbol images", CAPTURE_PATH)

# Make sure any of those paths exist
os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(CAPTURE_PATH, exist_ok=True)
