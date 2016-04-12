__author__ = 'becca.elenzil'

import matplotlib as plot
from time import sleep


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
    plt.pause(0.00001)
    plt.show()

def bubbleSort(some_list):
    display(some_list)
    plt.show()
    plt.pause(20)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(some_list)-1):
            if some_list[i] > some_list[i+1]:
                some_list[i+1], some_list[i] = some_list[i], some_list[i+1]
                display(some_list)
                sorted = False
            plt.show()
    plt.pause(10)

bubbleSort(create_random_list(25))


"""
some_list = [2,1,5]
display(some_list)
sleep(1)
some_list[0], some_list[1] = some_list[1], some_list[0]
display(some_list)
sleep(1)
some_list[1], some_list[2] = some_list[2], some_list[1]
display(some_list)
sleep(1)
some_list[0], some_list[1] = some_list[1], some_list[0]
display(some_list)
sleep(10)
"""

