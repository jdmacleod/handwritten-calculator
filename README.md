# Handwritten Calculator: MDAS Handwritten Arithmetic Recognition

A demo application using ML image classification to process basic hand-drawn integer MDAS arithmetic (Multiply, Divide, Add, Subtract).

![MDAS Calculator](./assets/mdas_calculate.png?raw=true)

Implemented using [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/).

## Getting Started

To set up and run the web demo application (frontend + backend) using the provided trained models and dataset, see the web demo [README](./demo/README.md).

To experiment with training using the provided models, see the training [README](./training/README.md).

[Pre-trained models](./trained_models/README.md) and the [symbol dataset](./mdas_symbol_dataset/README.md)  used to train the symbol recognition are provided.

### Using Python Virtual Environments

It's recommended to set up Python virtual environments for the different parts of this project; the demo web app and the training example provide `requirements.txt` files which may be used. See this [Python Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments) for more on setting up and using virtual environments.

### Installation Notes

The code was authored and tested using `python==3.12`, as well as `tensorflow==2.16.2`.

If you are installing on a Macintosh, you may benefit from the `tensorflow-metal` plugin. See the [Apple Developer page on TensorFlow](https://developer.apple.com/metal/tensorflow-plugin/) for more details.

## Model Descriptions

### Multilayer Perceptron (MLP)

Implements basic image classification following this TensorFlow quickstart tutorial: <https://www.tensorflow.org/tutorials/quickstart/beginner>

### Convolutional Neural Network (CNN)

Implements a more refined approach to image classification, following this TensorFlow tutorial: <https://www.tensorflow.org/tutorials/images/classification>

## Handwritten Calculator MDAS Symbol Dataset

See [mdas_symbol_dataset/README.md](mdas_symbol_dataset/README.md) for details.

## Training Handwritten Calculator

You can train the symbol recognition models on the provided dataset or your own custom dataset of captured symbols. Please see the training [README](training/README.md) for how to get started.

## Web demo for Handwritten Calculator

Run a web app locally to do some math, demo the models, and capture your own set of math symbols. Please see the web demo (frontend + backend) [README](demo/README.md) for details.

## License

The symbol dataset is licensed under the [MIT License](./LICENSE). All other code is covered by its respective licenses.

## Changes

See [CHANGELOG](./CHANGELOG.md) for notable changes to this codebase.

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for details. Pull requests and suggestions welcome.

## References

- <https://www.tensorflow.org/tutorials/>
- <https://yann.lecun.com/exdb/mnist/>
- <https://github.com/carolreis/mathreader>
- <https://github.com/Sagyam/Handwritten-Optical-Character-Recognition>
- <https://www.kaggle.com/datasets/xainano/handwrittenmathsymbols>
- <https://developer.apple.com/metal/tensorflow-plugin/>
- [K. Wang, J. Deng, L. Xu, C. Tang, Z. Pei and H. Wang, "The Four Arithmetic Operations for Handwritten Digit Recognition Based On Convolutional Neural Network," 2020 39th Chinese Control Conference (CCC), Shenyang, China, 2020, pp. 7423-7428, doi: 10.23919/CCC50068.2020.9189086. keywords: {Character recognition;Feature extraction;Image segmentation;Machine learning;Training;Handwriting recognition;Convolutional neural networks;Convolutional Neural Network;Handwritten Character Recognition;Four Arithmetic Operations},](https://ieeexplore.ieee.org/document/9189086)
