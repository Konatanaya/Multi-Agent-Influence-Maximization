import time
from Env.ICModel import ICModel
from Approach import Approach
import numpy as np
import matplotlib.pyplot as plt

K = 10


def plot(results):
    fig = plt.figure()
    x = np.arange(0, K+1, 1)
    for item in results:
        plt.plot(x, [0]+results[item], 'bs')
    plt.legend(results.keys())
    plt.xlabel('Seed set size')
    plt.ylabel('Number of activated users')
    plt.show()


if __name__ == '__main__':
    results = dict()
    IC = ICModel()
    app = Approach(IC, k=K)

    # start = time.time()
    # app.greedy()
    # print('\n'+str(time.time()-start))

    start = time.time()
    results['CELF'] = app.celf()
    print('\n' + str(time.time() - start))
    plot(results)
    # print(len(users), len(edges))
