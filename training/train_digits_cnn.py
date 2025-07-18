"""Train digit classifier using CNN model."""

import keras  # direct import as of TensorFlow 2.16
import tensorflow as tf

from .model import cnn  # local package import

print(f"TensorFlow Version: {tf.version.VERSION}")

# Load the MNIST handwritten numbers dataset
(train_images, train_labels), (test_images, test_labels) = (
    keras.datasets.mnist.load_data()
)

# MNIST digits dataset has 10 classes, digits 0-9
NUM_CLASSES = 10

MODEL_TYPE = "cnn"

# scale the pixel values in the dataset to be between 0-1 instead of 0-255
# this also converts the pixel values from integer to floating point
# See this post on why normalizing the data range is done
# https://stats.stackexchange.com/questions/253172/how-should-i-normalise-the-inputs-to-a-neural-network
train_images = train_images / 255.0
test_images = test_images / 255.0

# Use only the first 1000 images to speed up initial testing iterations
# train_labels = train_labels[:1000]
# test_labels = test_labels[:1000]

# train_images = train_images[:1000]
# test_images = test_images[:1000]

model = cnn.create_model(num_classes=NUM_CLASSES)
model.summary()

# evaluate model before training on the test set
loss, acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"untrained model, test accuracy: {100 * acc:5.2f}%")

model.fit(train_images, train_labels, epochs=10)

# evaluate model after training on the test set
loss, acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"trained model, test accuracy: {100 * acc:5.2f}%")

# This model is a "multi-layer perceptron"
MODEL_FILENAME = f"hc-digits-{MODEL_TYPE}-model.keras"

model.save(MODEL_FILENAME)
print(f"saved trained model as: {MODEL_FILENAME}")
