import numpy as np


class UserAgent(object):
    def __init__(self, id_number):
        self.id = id_number
        self.total_sum = 1
        self.neighbors = dict()
        self.active = False

    def add_neighbor(self, id_number, weight=None, mode='IC'):
        if mode is 'IC':
            if weight is None:
                self.neighbors[id_number] = np.random.uniform(0, 1)
            else:
                self.neighbors[id_number] = weight
        elif mode is 'LT':
            if weight is None:
                self.neighbors[id_number] = np.random.uniform(0, self.total_sum)
                self.total_sum -= self.neighbors[id_number]
            else:
                self.neighbors[id_number] = weight


class SystemAgent(object):
    def __init__(self, id_number):
        self.id_number = id_number
