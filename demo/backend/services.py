"Services for the backend application."

import base64
import io
import logging
import os
import pathlib

import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps
from tensorflow import keras

from .core import logger  # local package import
from .image_processing import center_grayscale_image_pil, ensure_image_padding


class PredictService:
    """Service for making predictions using a trained model."""

    def __init__(self, model_path: pathlib.Path) -> None:
        """Initialize the PredictService with a model path.
        Args:
            model_path (pathlib.Path): Path to the trained model.
        """
        self.model = tf.keras.models.load_model(model_path)
        self.probability_model = keras.Sequential([self.model, keras.layers.Softmax()])

    def handle(self, image_data_uri: str) -> tuple[int, float]:
        """Handle the prediction request.
        Args:
            image_data_uri (str): Base64 encoded image data URI.
        Returns:
            tuple: prediction and confidence
        """
        encoded_data = image_data_uri.split(",")[1]
        image_data = base64.urlsafe_b64decode(encoded_data)

        # Import image
        image = Image.open(io.BytesIO(image_data))

        # Convert the RGB image to grayscale image
        image = image.convert("L")

        # Invert the image, in our webapp we are drawing black on white like paper.
        # the MNIST dataset is white on black
        image = ImageOps.invert(image)

        # recenter the image
        image = center_grayscale_image_pil(image)
        # image = trim_borders(image)
        # image = pad_image(image)

        # ensure the image has a minimum padding ratio
        # as the training dataset
        # MNIST images are 20x20 image inside a 28x28 canvas
        # min padding_ratio of 8/28 = 0.285
        image = ensure_image_padding(image, min_padding_ratio=0.28)

        # Resize the image to 28x28, matching MNIST dimensions
        image = image.resize((28, 28))

        # Convert the image into numpy array
        image = np.array(image)

        # Normalize the pixel values in image
        image = image / 255.0

        # Set the datatype of image as float32
        image = image.astype(np.float32)

        # If we're debugging...
        # visualize the image
        # plt.imshow(image, cmap="gray")
        # plt.show()
        # write the image to disk for inspection
        if logger.isEnabledFor(logging.DEBUG):
            fname = "test_numpy_export"
            np.save(fname, image)
            logger.debug(f"wrote numpy data to disk as : {fname}")

        # Reshape the image for the model
        # image = image.reshape(1, 28, 28, 1)

        # the model expects a batch of images
        img_batch_single = np.expand_dims(image, 0)

        # prediction
        prediction_single = self.probability_model.predict(img_batch_single)
        prediction = np.argmax(prediction_single)
        confidence = prediction_single[0][prediction]
        return prediction, confidence


class CaptureItemService:
    """Service for capturing and processing images."""

    def __init__(self) -> None:
        pass

    def handle(self, image_data_uri: str, symbol_name: str, uuid: str) -> str:
        """Handle the capture item request.
        Args:
            image_data_uri (str): Base64 encoded image data URI.
            symbol_name (str): Name of the symbol.
            uuid (str): Unique identifier for the image.
        Returns:
            str: Path to the saved image.
        """
        logger.debug(f"symbol name is {symbol_name}")
        logger.debug(f"uuid is {uuid}")
        encoded_data = image_data_uri.split(",")[1]
        image_data = base64.urlsafe_b64decode(encoded_data)

        # Import image
        image = Image.open(io.BytesIO(image_data))

        # Convert the RGB image to grayscale image
        image = image.convert("L")

        # Invert the image, in our webapp we are drawing black on white like paper.
        # the MNIST dataset is white on black
        image = ImageOps.invert(image)

        # recenter the image
        image = center_grayscale_image_pil(image)
        # image = trim_borders(image)
        # image = pad_image(image)

        # ensure the image has a minimum padding ratio
        # as the training dataset
        # MNIST images are 20x20 image inside a 28x28 canvas
        # min padding_ratio of 8/28 = 0.285
        image = ensure_image_padding(image, min_padding_ratio=0.28)

        # Resize the image to 28x28
        image = image.resize((28, 28))

        # make directories for symbol type
        capture_path = os.path.join("capture", symbol_name)
        os.makedirs(capture_path, exist_ok=True)

        # write out PNG
        png_path = os.path.join(capture_path, f"{symbol_name}-{uuid}.png")
        image.save(png_path)

        # if we're debugging...
        if logger.isEnabledFor(logging.DEBUG):
            # Convert the image into numpy array
            image = np.array(image)

            # Normalize the pixel values in image
            image = image / 255.0

            # Set the datatype of image as float32
            image = image.astype(np.float32)

            # visualize the image
            # plt.imshow(image, cmap="gray")
            # plt.show()

            # write the image to disk for inspection when debugging is enabled

            fname = "test_capture_export"
            np.save(fname, image)
            logger.debug(f"wrote numpy data to disk as : {fname}")

        return png_path
