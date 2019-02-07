#!/usr/bin/env python3

def mysteryAlgorithm(lst):    
    for i in range(1,len(lst)):        
        while i > 0 and lst[i-1] > lst[i]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i -= 1
    return lst
print(mysteryAlgorithm([6, 4, 3, 8, 5]))