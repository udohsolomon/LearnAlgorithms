#!/usr/bin/env python3

# Example: 3 Integer Printing (Recursion)
# Print integers relative to various bases

# i.e.  printInteger(61,2) → 111101
#       printInteger(61,10) → 61

def rec_printInteger(n, b):
    str = '0123456789ABCDEF'
    if n < b:
        return str[n] # base case
    else:
        return rec_printInteger(n // b, b) + str[n % b] # recursive call
print(rec_printInteger(62, 2))