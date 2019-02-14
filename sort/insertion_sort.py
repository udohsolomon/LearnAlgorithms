#!/usr/bin/env python3

def insertion_sort(lst):                                        #times
    for i in range(1,len(lst)):                                 #n - 1
        while i > 0 and lst[i-1] > lst[i]:                      #(n - 1)n
            lst[i], lst[i-1] = lst[i-1], lst[i]                 #(n - 1)n/2
            i -= 1                                              #1
    return lst
print(insertion_sort([6, 4, 3, 8, 5]))