import numpy as np

class HighBoost:
    def __init__(self, shape, A, hp):
        self.p = shape[0]
        self.q = shape[1]
        self.A = A
        self.hp = np.array(hp)
        self.filter = self.build_filter()

    def build_filter(self):
        filter = np.zeroes((p,q))
        filter = (self.A - 1) + hp
        return filter

    def get_high_boodt(self):
        return self.filter
