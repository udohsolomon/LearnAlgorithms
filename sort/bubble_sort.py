#!/usr/bin/env python3

def bubble_sort(lst):
    length = len(lst)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if lst[j] > lst[j+1]:
                swapped = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if not swapped: break  # Stop iteration if the list is sorted.
    return lst

print(bubble_sort([6, 5, 3, 1, 8, 7, 2, 4]))