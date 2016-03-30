__author__ = 'becca.elenzil'

import matplotlib as plot


import matplotlib.pyplot as plt
from random import shuffle


plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return some_list

def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.pause(0.0001)
    plt.show()

def bubbleSort(some_list):
    plt.pause(10)
    sorted = False
    k = 0
    while not sorted:
        sorted = True
        for i in range(len(some_list)-1):
            if some_list[i] > some_list[i+1]:
                some_list[i+1], some_list[i] = some_list[i], some_list[i+1]
                display(some_list)
                sorted = False
            plt.show()
        #k += 1

bubbleSort(create_random_list(20))


"""
some_list = [2,1,5,3,]
display(some_list)
some_list[0], some_list[1] = some_list[1], some_list[0]
display(some_list)
some_list[1], some_list[2] = some_list[2], some_list[1]
display(some_list)
some_list[0], some_list[1] = some_list[1], some_list[0]
display(some_list)
"""

