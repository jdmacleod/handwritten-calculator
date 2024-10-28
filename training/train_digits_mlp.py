import tensorflow as tf
from model import mlp  # local package import

print(f"TensorFlow Version: {tf.version.VERSION}")

# Load the MNIST handwritten numbers dataset
(train_images, train_labels), (test_images, test_labels) = (
    tf.keras.datasets.mnist.load_data()
)

# MNIST digits dataset has 10 classes, digits 0-9
NUM_CLASSES = 10

MODEL_TYPE = "mlp"

# scale the pixel values in the dataset to be between 0-1 instead of 0-255
# this also converts the pixel values from integer to floating point
# TODO: find the reference that explains the reasons for this step
train_images = train_images / 255.0
test_images = test_images / 255.0

# Use only the first 1000 images to speed up initial testing iterations
# train_labels = train_labels[:1000]
# test_labels = test_labels[:1000]

# train_images = train_images[:1000]
# test_images = test_images[:1000]

model = mlp.create_model(num_classes=NUM_CLASSES)
model.summary()

# evaluate model before training on the test set
loss, acc = model.evaluate(test_images, test_labels, verbose=2)
print("untrained model, test accuracy: {:5.2f}%".format(100 * acc))

model.fit(train_images, train_labels, epochs=10)

# evaluate model after training on the test set
loss, acc = model.evaluate(test_images, test_labels, verbose=2)
print("trained model, test accuracy: {:5.2f}%".format(100 * acc))

# This model is a "multi-layer perceptron"
model_filename = f"hc-digits-{MODEL_TYPE}-model.keras"

model.save(model_filename)
print(f"saved trained model as: {model_filename}")
