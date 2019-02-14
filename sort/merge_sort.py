#!/usr/bin/env  python3
'''
Python implementation of merge sort algorithm.
Worst Case Scenario : O(n)

'''

#this modules are required for testing only
import random
import copy
import matplotlib.pyplot as plt 

#actual implementation starts here
def merge_sort(LIST):
    '''
    Returns sorted list.
    '''

    #divide list into two parts
    start = []
    end   = []
    a = min(LIST)
    b = max(LIST)

    while len(LIST) > 1:
        start.append(a)
        end.append(b)
        try:
            LIST.remove(a)
            LIST.remove(b)
            a = min(LIST)
            b = max(LIST)
        except ValueError:
            continue
    end.reverse()
    return start + end

def visualization(LIST, SORTED_LIST):
    '''
    To visualise both unsorted and sorted data.
    '''
    plt.plot(LIST)   
    plt.xlabel('Random Data')
    plt.show()
    plt.plot(SORTED_LIST)
    plt.xlabel('Merge Sorted Data')
    plt.show()

if __name__ == "__main__":
    #Test
    LIST = [0, 8, 5, 2, 9, 4, 7, 3, 6, 1]
    print('Unordered list {}'.format(LIST))
    print('Merge sorted list {}'.format(merge_sort(LIST)))
    '''
    generate a list of random length between 100 and 1000
    and add ramdom number to it
    '''
    LIST = [random.randint(0, 1000) for i in range(random.randint(100, 1000))]
    unsortedLIST = copy.deepcopy(LIST)
    visualization(unsortedLIST, merge_sort(unsortedLIST))
