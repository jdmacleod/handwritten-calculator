# Models and Training code for Handwritten Calculator

TensorFlow models for recognition of handwritten numbers and symbols with training. Part of the handwritten-calculator ensemble.

Trained models and a sample symbol dataset are provided. The information below can be used to repeat the training that was done, or to train with new parameters, possibly on a new dataset.

## Quick Start

### Set Up Python3 Virtual Environment

```bash
cd training
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt
```

### Unpack MDAS dataset (needed for training)

See [README](../mdas_symbol_dataset/README.md)

### Train and Deploy Models

#### Train Multilayer Perceptron models

```bash
python train_digits_mlp.py
python train_symbols_mlp.py
```

#### Train Convolutional Neural Network models

```bash
python train_digits_cnn.py
python train_symbols_cnn.py
```

#### Copy trained model files to project directory

```bash
cp -pv *.keras ../trained_models
```

### Collect and Process Symbol Training Data

Follow the web demo app [README](../demo/README.md) to set up the frontend and backend to be able to capture symbol images for training.

Use <http://localhost:5001/capture> to capture symbol training data images.

The stored images will be written to `...demo/backend/capture/`.

#### Process Captured Symbol Images

```bash
# copy the captured written symbol images into this directory
cp -rpv ../demo/backend/capture ./symbols_captured
# process the symbol dataset to amplify it and partition to training, test, validation
python scripts/amplify_symbol_data.py
```

## Acknowledgements

Extends the [TensorFlow tutorials](https://www.tensorflow.org/tutorials).

Uses material described in this series of posts:
<https://goodboychan.github.io/python/deep_learning/tensorflow-keras/2020/10/10/01-CNN-with-MNIST.html#Build-model-with-Sequential-API>
