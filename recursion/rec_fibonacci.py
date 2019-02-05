#!/usr/bin/env python3

# Example: 2 Fibonacci Numbers (Recursion)

def rec_fibonacci(n):
    # print('n =', n)
    if n == 0 or n == 1:
        return n
    else:
        return rec_fibonacci(n-1) + rec_fibonacci(n - 2)

print(rec_fibonacci(100))
