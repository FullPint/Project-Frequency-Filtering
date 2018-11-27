import numpy as np

class Laplace:
    def __init__(self, shape):
        self.p = shape[0]
        self.q = shape[1]
        self.filter = self.build_filter()

    def build_filter(self):
        h = np.zeroes((self.p, self.q))
        index_iterator = np.nditer(filter, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            h[u][v] = 1 + (np.square(u - self.p) + np.square(v - self.q))
            index_iterator.iternext()
        return filter

    def get_laplace(self):
        return self.filter
