import os
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import time
from Env.ICModel import ICModel
import Approaches.Approach as ap

if __name__ == '__main__':
    IC = ICModel()
    greedy = ap.Greedy(IC)
    start = time.time()
    greedy.simulate()
    print(str(time.time()-start))
    # print(len(users), len(edges))
