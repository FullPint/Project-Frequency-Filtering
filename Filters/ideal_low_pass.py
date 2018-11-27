import numpy as np

def IdealLowPass:
    def __init__(self, shape, cutoff):
        self.p = shape[0]
        self.q = shape[1]
        self.cutoff = cutoff
        self.filter = self.build_filter()

    def build_filter(self):
        filter = np.zeroes((self.p, self.q))
        index_iterator = np.nditer(filter, flags=['multi_index'])
        while not index_iterator.finished:
            u = index_iterator.multi_index[0]
            v = index_iterator.multi_index[1]
            filter[u][v] = 1 if self.calculate_distance(u, v) > self.cutoff else 0
            index_iterator.iternext()
        return filter

    def calculate_distance(self, u, v):
        dist = np.sqrt(np.square(u - (self.p/2)) + np.square(v - (self.q/2)))
        return dist

    def get_filter(self):
        return self.filter  
