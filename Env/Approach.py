import numpy as np


class Approach(object):
    def __init__(self, model, t=100, k=5, mode='IC'):
        self.time_steps = t
        self.k = k
        self.model = model
        self.mode = mode

    def write_results(self, name):
        print()
        # np.savetxt('../Results/total_benefits_' + name + '.txt', np.array(self.total_benefits), fmt='%.2f', delimiter=' ')
        # np.savetxt('../Results/ave_num_' + name + '.txt', np.array(self.average_req_num), fmt='%.2f', delimiter=' ')
        # np.savetxt('../Results/ratio_' + name + '.txt', np.array(self.ratio), fmt='%.2f', delimiter=' ')

    def greedy(self):
        seed_set, spread = [], []
        for _ in range(self.k):
            best_spread = 0
            for user in (set(self.model.G.nodes()) - set(seed_set)):
                count = self.model.diffusion(seed_set + [user], self.time_steps)

                if count > best_spread:
                    best_spread, node = count, user
            seed_set.append(user)
            spread.append(count)
        np.savetxt('../Results/' + self.mode + '_greedy.txt', spread, fmt='%.2f', delimiter=' ')
        return spread

    def celf(self):
        marg_gain = [(user, self.model.diffusion([user], self.time_steps)) for user in set(self.model.G.nodes())]
        Q = sorted(marg_gain, key=lambda x: x[1], reverse=True)
        seed_set, spread = [Q[0][0]], [Q[0][1]]
        for _ in range(self.k - 1):
            Q = Q[1:]
            check = False
            while not check:
                current = Q[0][0]
                Q[0] = (current, self.model.diffusion(seed_set + [current], self.time_steps))
                Q = sorted(Q, key=lambda x: x[1], reverse=True)
                check = (Q[0][0] == current)
            seed_set.append(Q[0][0])
            spread.append(Q[0][1])
        np.savetxt('../Results/' + self.mode + '_celf.txt', spread, fmt='%.2f', delimiter=' ')
        return spread

