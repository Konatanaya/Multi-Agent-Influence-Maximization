import time
from Env.ICModel import ICModel
from Approach import Approach
import matplotlib.pyplot as plt


def plot():
    fig = plt.figure()
    plt.plot()


if __name__ == '__main__':
    IC = ICModel()
    app = Approach(IC)
    # start = time.time()
    # app.greedy()
    # print('\n'+str(time.time()-start))

    start = time.time()
    app.celf()
    print('\n' + str(time.time() - start))
    # print(len(users), len(edges))
