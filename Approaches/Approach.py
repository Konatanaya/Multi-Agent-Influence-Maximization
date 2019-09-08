import numpy as np


class Approach(object):
    def __init__(self, t=1000, k=5):
        self.time_steps = t
        self.k = k


class Greedy(Approach):
    def __init__(self, model):
        Approach.__init__(self)
        self.model = model

    def simulate(self):
        seed_set, spread = [], []
        for _ in range(self.k):
            best_spread = 0
            for user in (set(self.model.G.nodes())-set(seed_set)):
                count = self.model.diffusion(seed_set+[user], self.time_steps)

                if count > best_spread:
                    best_spread, node = count, user
            seed_set.append(user)
            spread.append(count)
