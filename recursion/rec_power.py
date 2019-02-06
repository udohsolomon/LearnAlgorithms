#!/usr/bin/env python3
# Example: 4 Power (Recursion)

# i.e.  n^10 = n*(n^9)

def rec_power(n, y):
    if y == 0:
        return 1 # base case
    if y >= 1:
        return n*rec_power(n, y-1) # recursive call
print(rec_power(2, 10))
