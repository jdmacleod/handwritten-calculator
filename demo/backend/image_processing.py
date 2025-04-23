"""Image processing routines for the backend application."""

import base64
from io import BytesIO

import numpy as np
from PIL import Image, ImageChops, ImageOps

from .core import logger  # local package import


def data_uri_to_image(uri: str) -> Image.Image:
    """Convert a data URI to a PIL Image.
    Args:
        uri (str): The data URI to convert.
    Returns:
        Image.Image: The converted PIL Image.
    """
    encoded_data = uri.split(",")[1]
    image = base64.b64decode(encoded_data)
    return Image.open(BytesIO(image))


def replace_transparent_background(image: Image.Image) -> Image.Image:
    """Replace transparent background with white.
    Args:
        image (Image.Image): The input image.
    Returns:
        Image.Image: The image with transparent background replaced.
    """
    image_arr = np.array(image)

    has_no_alpha = len(image_arr.shape) < 3 or image_arr.shape[2] < 4
    if has_no_alpha:
        return image

    alpha1 = 0
    r2, g2, b2, alpha2 = 255, 255, 255, 255
    _, _, _, alpha = (
        image_arr[:, :, 0],
        image_arr[:, :, 1],
        image_arr[:, :, 2],
        image_arr[:, :, 3],
    )
    mask = alpha == alpha1
    image_arr[:, :, :4][mask] = [r2, g2, b2, alpha2]

    return Image.fromarray(image_arr)


def trim_borders(image: Image.Image) -> Image.Image:
    """Trim borders of an image.
    Args:
        image (Image.Image): The input image.
    Returns:
        Image.Image: The trimmed image.
    """
    bg = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return image.crop(bbox)

    return image


def pad_image(image: Image.Image) -> Image.Image:
    """Pad image by 56 pixels all around, one-half image.
    Args:
        image (Image.Image): The input image.
    Returns:
        Image.Image: The padded image.
    """
    return ImageOps.expand(image, border=56, fill="#fff")


def to_grayscale(image: Image.Image) -> Image.Image:
    """Convert an image to grayscale.
    Args:
        image (Image.Image): The input image.
    Returns:
        Image.Image: The grayscale image.
    """
    return image.convert("L")


def invert_colors(image: Image.Image) -> Image.Image:
    """Invert the colors of an image.
    Args:
        image (Image.Image): The input image.
    Returns:
        Image.Image: The image with inverted colors.
    """
    return ImageOps.invert(image)


def resize_image(image: Image.Image) -> Image.Image:
    """Resize an image to 8x8 pixels.
    Args:
        image (Image.Image): The input image.
    Returns:
        Image.Image: The resized image.
    """
    return image.resize((8, 8), Image.Resampling.BILINEAR)


def center_grayscale_image(image: np.ndarray) -> np.ndarray:
    """Center a grayscale image using cv2."""
    center_x = image.shape[1] // 2
    center_y = image.shape[0] // 2

    # create a translation matrix
    translation_matrix = np.float32([[1, 0, -center_x], [0, 1, -center_y]])

    try:
        import cv2

        centered_image = cv2.warpAffine(
            image, translation_matrix, (image.shape[1], image.shape[0])
        )
    except ImportError:
        logger.warning(
            "Could not import cv2 for image centering, returning unaltered image."
        )
        centered_image = image

    return centered_image


def center_grayscale_image_pil(image: Image.Image) -> Image.Image:
    """Center the contents of a grayscale image using PIL.
    The image is padded by half its dimension all around, and then cropped
    to the original size. This centers the image content.
    Args:
        image (Image.Image): The input image.
    Returns:
        Image.Image: The centered image.
    """
    # pad image by half dimension all around
    pad_value = image.size[0] // 2
    logger.debug(f"padding image all around with black by: {pad_value} pixels")
    image = ImageOps.expand(image, border=pad_value)
    # get bounding box of image content
    bbox = image.getbbox()
    logger.debug(f"image bbox = {bbox}")
    if bbox:
        center_x = ((bbox[2] - bbox[0]) // 2) + bbox[0]
        center_y = ((bbox[3] - bbox[1]) // 2) + bbox[1]
        logger.debug(f"image bbox center x,y = {center_x},{center_y}")
        # determine new centered bbox
        padded_bbox = image.getbbox()
        logger.debug(f"image padded bbox = {padded_bbox}")
        centered_crop_bbox = [
            center_x - pad_value,
            center_y - pad_value,
            center_x + pad_value,
            center_y + pad_value,
        ]
        logger.debug(f"image centered crop = {centered_crop_bbox}")
        image = image.crop(centered_crop_bbox)
    return image


def ensure_image_padding(
    image: Image.Image, min_padding_ratio: float = 0.28
) -> Image.Image:
    """Ensure a grayscale image has minimum padding using PIL.
    The image is padded by half its dimension all around, and then cropped
    to the original size. This centers the image content.
    Args:
        image (Image.Image): The input image.
        min_padding_ratio (float): The minimum padding ratio to ensure.
    Returns:
        Image.Image: The padded image.
    """
    # get bounding box of image content
    bbox = image.getbbox()
    logger.debug(f"ensure padding image bbox = {bbox}")
    if bbox:
        bbox_size_x = bbox[2] - bbox[0]
        bbox_size_y = bbox[3] - bbox[1]
        max_bbox_size = max(bbox_size_x, bbox_size_y)
        image_padding_ratio = (image.size[0] - max_bbox_size) / image.size[0]
        if image_padding_ratio < min_padding_ratio:
            # must force to int, floor division will preserve float type
            additional_padding = int(
                ((max_bbox_size * (1.0 + min_padding_ratio)) - image.size[0]) // 2
            )
            logger.debug(
                f"ensure_padding: padding image by: {additional_padding} pixels"
            )
            image = ImageOps.expand(image, border=additional_padding)
    return image


def process_image(data_uri: str) -> np.ndarray:
    """Process an image from a data URI.
    Args:
        data_uri (str): The data URI of the image.
    Returns:
        np.ndarray: The processed image as a NumPy array.
    """
    image = data_uri_to_image(data_uri)

    is_empty = not image.getbbox()
    if is_empty:
        return None

    image = replace_transparent_background(image)
    image = trim_borders(image)
    image = pad_image(image)
    image = to_grayscale(image)
    image = invert_colors(image)
    image = resize_image(image)

    return np.array([np.array(image).flatten()])
