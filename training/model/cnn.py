"""Create a Convolutional Neural Network (cnn) model for image classification."""

# adapts the CNN example from TensorFlow tutorial
# https://www.tensorflow.org/tutorials/images/cnn

import keras  # direct import as of TensorFlow 2.16


def create_model(num_classes: int = 10) -> keras.Model:
    """Create example CNN model after the TensorFlow tutorial."""
    model = keras.Sequential(
        name="CNN_Sequential",
        layers=[
            keras.Input(shape=(28, 28, 1)),
            keras.layers.Conv2D(
                filters=32, kernel_size=(3, 3), padding="same", activation="relu"
            ),
            keras.layers.MaxPool2D(
                padding="same",
            ),
            keras.layers.Conv2D(
                filters=64, kernel_size=(3, 3), padding="same", activation="relu"
            ),
            keras.layers.MaxPool2D(
                padding="same",
            ),
            keras.layers.Conv2D(
                filters=128, kernel_size=(3, 3), padding="same", activation="relu"
            ),
            keras.layers.MaxPool2D(
                padding="same",
            ),
            keras.layers.Flatten(),
            keras.layers.Dense(256, activation="relu"),
            keras.layers.Dropout(0.4),
            keras.layers.Dense(num_classes),
        ],
    )
    model.compile(
        optimizer="adam",
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"],
    )
    return model
