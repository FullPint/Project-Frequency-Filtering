from high_boost import HighBoost

class UnsharpMask(HighBoost):
    def __init__(self, shape, hp):
        HighBoost.__init__(self, shape, hp, A=1)
