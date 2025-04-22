"""Train symbol classifier using CNN model."""

import os

import tensorflow as tf

from .model import cnn  # local package import

print(f"TensorFlow Version: {tf.version.VERSION}")

# Load the captured Symbols PNG training dataset from disk.
# addition_plus
# division_obelus
# division_slash
# multiplication_cross
# multiplication_dot
# subtraction_minus
# six (6) symbols

NUM_CLASSES = 6
MODEL_TYPE = "cnn"

DATASET_DIR = os.path.join(os.pardir, "mdas_symbol_dataset", "symbols_partitioned")

training_data_dir = os.path.join(DATASET_DIR, "train")
testing_data_dir = os.path.join(DATASET_DIR, "test")
validation_data_dir = os.path.join(DATASET_DIR, "val")

BATCH_SIZE = 32
IMG_HEIGHT = 28
IMG_WIDTH = 28

train_images_ds = tf.keras.utils.image_dataset_from_directory(
    training_data_dir,
    color_mode="grayscale",
    seed=123,
    batch_size=BATCH_SIZE,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
)

validate_images_ds = tf.keras.utils.image_dataset_from_directory(
    validation_data_dir,
    color_mode="grayscale",
    seed=123,
    batch_size=BATCH_SIZE,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
)

# load the testing dataset
# see these references
# https://keras.io/api/datasets/mnist/
# https://stackoverflow.com/questions/13610074/is-there-a-rule-of-thumb-for-how-to-divide-a-dataset-into-training-and-validatio

test_images_ds = tf.keras.utils.image_dataset_from_directory(
    testing_data_dir,
    color_mode="grayscale",
    seed=123,
    batch_size=BATCH_SIZE,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
)

class_names = train_images_ds.class_names
print(class_names)

# scale the pixel values in the training dataset to be between 0-1 instead of 0-255
# this also converts the pixel values from integer to floating point
# See this post on why normalizing the data range is done
# https://stats.stackexchange.com/questions/253172/how-should-i-normalise-the-inputs-to-a-neural-network

normalization_layer = tf.keras.layers.Rescaling(1.0 / 255)
normalized_train_ds = train_images_ds.map(lambda x, y: (normalization_layer(x), y))
normalized_validate_ds = validate_images_ds.map(
    lambda x, y: (normalization_layer(x), y)
)
normalized_test_ds = test_images_ds.map(lambda x, y: (normalization_layer(x), y))

# Use only the first 1000 images to speed up initial testing iterations
# train_labels = train_labels[:1000]
# test_labels = test_labels[:1000]

# train_images = train_images[:1000]
# test_images = test_images[:1000]

model = cnn.create_model(num_classes=NUM_CLASSES)
model.summary()

# evaluate model before training on the test set
# here we pass in a tf.data.Dataset as the input data
# https://www.tensorflow.org/api_docs/python/tf/keras/Model#evaluate
loss, acc = model.evaluate(normalized_test_ds, verbose=2)
print(f"untrained model, test accuracy: {100 * acc:5.2f}%")

# train the model
# here we pass in a tf.data.Dataset as the input data
# https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit
model.fit(normalized_train_ds, validation_data=normalized_validate_ds, epochs=10)

# evaluate model after training on the test set
# here we pass in a tf.data.Dataset as the input data
loss, acc = model.evaluate(normalized_test_ds, verbose=2)
print(f"trained model, test accuracy: {100 * acc:5.2f}%")

# This model is a "multi-layer perceptron"
MODEL_FILENAME = f"hc-symbols-{MODEL_TYPE}-model.keras"

model.save(MODEL_FILENAME)
print(f"saved trained model as: {MODEL_FILENAME}")
