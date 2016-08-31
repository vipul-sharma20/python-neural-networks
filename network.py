import numpy as np


class Network(object):

    def __init__(self, size):
        self.size = size
        self.layers = len(size)
        self.bias = [np.random.randn(y, 1) for y in size[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(size[:-1], size[1:])]

