#!/usr/bin/env python3
# Example: 5 Sum of a list (Recursion)

def rec_sum(lst):
    if len(lst) == 1:
        return lst[0] # base case
    else:
        return lst[0] + rec_sum(lst[1:]) # recursive call
print(rec_sum([2, 4, 7, 9, 4, 5]))
    