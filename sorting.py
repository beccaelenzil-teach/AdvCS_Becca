__author__ = 'becca.elenzil'

#selection sort

def selectionSort(list):

    for k in range(0,len(list)-2):
        smallestValue = list[k]
        for i in range(k+1,len(list)):
            if list[i] < smallestValue:
                smallestValue = list[i]
                smallIndex = i

        list = list[0:k] + [smallestValue] + [list[k]] + list[(smallIndex+1):]

        print list

    return list

print selectionSort([4,3,6,2, 5, 7, 8, 6, 5, 2, 1, 4, 1])
