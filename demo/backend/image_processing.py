import base64
from io import BytesIO

import numpy as np
from core import logger  # local package import
from PIL import Image, ImageChops, ImageOps


def data_uri_to_image(uri):
    encoded_data = uri.split(",")[1]
    image = base64.b64decode(encoded_data)
    return Image.open(BytesIO(image))


def replace_transparent_background(image):
    image_arr = np.array(image)

    has_no_alpha = len(image_arr.shape) < 3 or image_arr.shape[2] < 4
    if has_no_alpha:
        return image

    alpha1 = 0
    r2, g2, b2, alpha2 = 255, 255, 255, 255
    red, green, blue, alpha = (
        image_arr[:, :, 0],
        image_arr[:, :, 1],
        image_arr[:, :, 2],
        image_arr[:, :, 3],
    )
    mask = alpha == alpha1
    image_arr[:, :, :4][mask] = [r2, g2, b2, alpha2]

    return Image.fromarray(image_arr)


def trim_borders(image):
    bg = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return image.crop(bbox)

    return image


def pad_image(image):
    """Pad image by 56 pixels all around, one-half image."""
    return ImageOps.expand(image, border=56, fill="#fff")


def to_grayscale(image):
    return image.convert("L")


def invert_colors(image):
    return ImageOps.invert(image)


def resize_image(image):
    return image.resize((8, 8), Image.BILINEAR)


def scale_down_intensity(image):
    image_arr = np.array(image)
    image_arr = exposure.rescale_intensity(image_arr, out_range=(0, 16))
    return Image.fromarray(image_arr)


def pad_image_borders(image):
    """Pad an image so it has a percentage of open border.

    The MNIST Digits training set does not generally have writing that extends
    to the edge of the image.

    """
    pass


def center_grayscale_image(image):
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
    except:
        logger.warning(
            "Could not import cv2 for image centering, returning unaltered image."
        )
        centered_image = image

    return centered_image


def center_grayscale_image_pil(image):
    """Center the contents of a grayscale image using PIL."""
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


def ensure_image_padding(image, min_padding_ratio=0.28):
    """Ensure a grayscale image has minimum padding all around the image contents using PIL."""
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
                f"ensure_padding: padding image all around with black by: {additional_padding} pixels"
            )
            image = ImageOps.expand(image, border=additional_padding)
    return image


def process_image(data_uri):
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
    # image = scale_down_intensity(image)

    return np.array([np.array(image).flatten()])