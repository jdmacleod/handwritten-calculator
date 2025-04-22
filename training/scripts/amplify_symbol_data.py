"""Generate partitioned symbol images for training, testing, and validation."""

import glob
import logging
import os
import shutil
import uuid
from pathlib import Path

import splitfolders  # external
import tqdm  # external progress bar
from PIL import Image  # external

logger = logging.getLogger(__name__)

captured_img_path = Path("symbols_captured")

amplified_img_path = Path("symbols_amplified")


def generate_rotated_image(
    imagefile: str, dataset_path: str, rotation_degrees: int = 0
) -> None:
    """Generate a rotated image from the provided image, writing to disk.

    Args:
        imagefile (str): the image filename to rotate
        dataset_path (str): path where the image shall be written to.
        rotation (int, optional): rotation in degrees to apply (CCW). Defaults to 0.
    """
    image = Image.open(imagefile)
    rotated_image = image.rotate(rotation_degrees)
    duplicate_name = f"{str(uuid.uuid4())}.png"
    rotated_image.save(os.path.join(dataset_path, duplicate_name))


def generate_mirrored_image(
    imagefile: str, dataset_path: str, action: str = "flop"
) -> None:
    """Generate a mirrored image from the provided image, writing to disk.

    Args:
        imagefile (str): the image filename to rotate
        dataset_path (str): path where the image shall be written to.
        action (str, optional): Mirror about vertical (flop) or horizontal (flip) axis. Defaults to flop.
    """
    image = Image.open(imagefile)
    duplicate_name = f"{str(uuid.uuid4())}.png"
    if action == "flip":
        mirrored_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        mirrored_image.save(os.path.join(dataset_path, duplicate_name))
    elif action == "flop":
        mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        mirrored_image.save(os.path.join(dataset_path, duplicate_name))
    else:
        raise RuntimeWarning(
            f"Unexpected mirror action {action}, skipping it for image {imagefile}!"
        )


def amplify_dataset(dataset_path: str, operations: list[str] | None = None) -> None:
    """Duplicate existing files in a directory with image processing.

    Apply operations per provided list
        rot90 - rotate CCW 90 degrees
        rot180 - rotate CCW 180 degrees
        rot270 - rotate CCW 270 degrees
        flip - mirror image, swapping top for bottom (about a horizontal axis)
        flop - mirror image, swapping left for right (about a vertical axis)

    """
    if operations:
        list_of_files = glob.glob(f"{dataset_path}/*.png")
        folder_path = Path(dataset_path)
        for file in tqdm.tqdm(list_of_files, desc=folder_path.stem):
            for op in operations:
                match op:
                    case "rot90":
                        generate_rotated_image(
                            imagefile=file,
                            dataset_path=dataset_path,
                            rotation_degrees=90,
                        )
                    case "rot180":
                        generate_rotated_image(
                            imagefile=file,
                            dataset_path=dataset_path,
                            rotation_degrees=180,
                        )
                    case "rot270":
                        generate_rotated_image(
                            imagefile=file,
                            dataset_path=dataset_path,
                            rotation_degrees=270,
                        )
                    case "flip":
                        generate_mirrored_image(
                            imagefile=file, dataset_path=dataset_path, action="flip"
                        )
                    case "flop":
                        generate_mirrored_image(
                            imagefile=file, dataset_path=dataset_path, action="flop"
                        )
                    case _:
                        pass
        logger.info(f"amplified {dataset_path} with operations {operations}.")
    else:
        logger.warning(
            f"no operations provided to amplify dataset {dataset_path}, skipping it!"
        )


# copy the captured files to a directory for amplification
shutil.copytree(captured_img_path, amplified_img_path, dirs_exist_ok=True)

# amplify the symbol files with symmetry operations
class_subfolders = [f.path for f in os.scandir(amplified_img_path)]
for subfolder in sorted(class_subfolders):
    folder_path = Path(subfolder)
    logger.info(f"processing {folder_path.stem}")
    match folder_path.stem:
        case "addition_plus":
            amplify_dataset(
                subfolder, operations=["rot90", "rot180", "rot270", "flip", "flop"]
            )
        case "division_obelus":
            amplify_dataset(subfolder, operations=["rot180", "flip", "flop"])
        case "division_slash":
            amplify_dataset(subfolder, operations=["rot180"])
        case "multiplication_dot":
            amplify_dataset(
                subfolder, operations=["rot90", "rot180", "rot270", "flip", "flop"]
            )
        case "multiplication_cross":
            amplify_dataset(
                subfolder, operations=["rot90", "rot180", "rot270", "flip", "flop"]
            )
        case "subtraction_minus":
            amplify_dataset(subfolder, operations=["rot180", "flip", "flop"])
        case _:
            pass

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(
    amplified_img_path,
    output="symbols_partitioned",
    seed=1337,
    ratio=(0.8, 0.1, 0.1),
    group_prefix=None,
    move=False,
)  # default values
