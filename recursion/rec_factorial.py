#!/usr/bin/env python3
# Example: 1 Factorial (Recursion)

# i.e.  n! = n⋅(n−1)⋅(n−2) ⋯ 3⋅2⋅1

def rec_factorial(n):
    # print('n =', n)
    if n == 1:
        return 1 # base case of factorial
    else:
        return n*rec_factorial(n-1) # recursive call

print(rec_factorial(1000))