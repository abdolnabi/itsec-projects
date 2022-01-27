from random import SystemRandom

class RandomGenerator:
    @classmethod
    def randgen(cls, upper_bound, lower_bound=1):
        return SystemRandom().randrange(lower_bound, upper_bound)



