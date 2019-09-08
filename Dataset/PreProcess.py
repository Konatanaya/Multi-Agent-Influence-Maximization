import os
import numpy as np
import Env.Agents as ag

users = dict()


def process_data():
    files = os.listdir('../Dataset/Unprocessed Dataset/')
    print(files)
    index = int(input("Plz input the index of a dataset:"))
    file = files[index][:-4]
    with open(file='../Dataset/Unprocessed Dataset/' + file + '.txt', mode='r') as f:
        for line in f.readlines():
            arr = line.strip().split()
            if arr[0] not in users:
                users[arr[0]] = ag.UserAgent(arr[0])
            if arr[1] not in users:
                users[arr[1]] = ag.UserAgent(arr[1])
            users[arr[0]].add_neighbor(arr[1], mode='IC')
    with open(file='../Dataset/' + file + '/' + file + '.txt', mode='w') as f:
        for user in users.values():
            for neighbor in user.neighbors:
                f.write(user.id + ' ' + neighbor + ' ' + str(user.neighbors[neighbor]) + '\n')


if __name__ == '__main__':
    process_data()
