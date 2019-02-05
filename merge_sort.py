#!/usr/bin/env/python3
'''
Python implementation of merge sort algorithm.
Worst Case Scenario : O(n)

'''

#these modules are required for testing only
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




