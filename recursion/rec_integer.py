#!/usr/bin/env python3

# Example: 3 Integer Printing (Recursion)
# Print integers relative to various bases

# i.e.  printInteger(61,2) → 111101
#       printInteger(61,10) → 61

def rec_printInteger(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
print(rec_printInteger(610000, 2))