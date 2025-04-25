"""Create a Multilayer Perceptron (mlp) model for image classification."""

# uses the MLP example from TensorFlow tutorial
# https://www.tensorflow.org/tutorials/quickstart/beginner#build_a_machine_learning_model
# https://www.tensorflow.org/guide/keras/sequential_model

import keras  # direct import as of TensorFlow 2.16


def create_model(num_classes: int = 10) -> keras.Model:
    """Create example MLP model from TensorFlow tutorial."""
    model = keras.Sequential(
        name="MLP_Sequential",
        layers=[
            keras.Input(shape=(28, 28, 1)),
            keras.layers.Flatten(),
            keras.layers.Dense(128, activation="relu"),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(num_classes),
        ],
    )
    model.compile(
        optimizer="adam",
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"],
    )
    return model
