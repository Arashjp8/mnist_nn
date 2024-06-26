# MNIST Image Processing Model

This project implements a simple neural network to classify MNIST images using NumPy. The network consists of an input layer, one hidden layer, and an output layer, with sigmoid activation functions and mean squared error loss.

## Table of Contents

- [Overview](#overview)
- [Model Architecture](#model-architecture)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)

## Overview

This repository contains a simple neural network implemented in Python using NumPy for training and evaluating on the MNIST dataset. The network consists of a single hidden layer with sigmoid activations.

## Model Architecture

The model architecture is as follows:

- **Input Layer**: 784 neurons (28x28 pixels)
- **Hidden Layer**: 20 neurons
- **Output Layer**: 10 neurons (one for each digit 0-9)

The activation function used is the sigmoid function, and the cost function is the mean squared error.

## Dependencies

- Python 3.x
- NumPy
- Matplotlib (for visualizing the results)

You can install the necessary packages using pip:

```bash
pip install numpy matplotlib
```

## Usage

1. Prepare the MNIST dataset: Ensure you have the MNIST dataset loaded using the get_mnist() function which should return the images and labels.
2. Run the training script: The model will train for a specified number of epochs and output the accuracy after each epoch.
