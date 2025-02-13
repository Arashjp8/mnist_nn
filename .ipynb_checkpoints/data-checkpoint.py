import numpy as np
import pathlib

def get_mnist():
    with np.load(f"{pathlib.Path(__file__).parent.absolute()}/data/mnist.npz") as f:
        images, lables = f["x_train"], f["y_train"]
    images = images.astype("float32") / 255
    images = np.reshape(images, (images.shape[0], images.shape[1] * images.shape[2]))
    lables = np.eye(10)[lables]
    return images, lables