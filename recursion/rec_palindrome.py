#!/usr/bin/env python3
# Example: 3 Palindrome (Recursion)

# Detect whether a sequence is a palindrome

def rec_palindrome(str):
    if len(str) <= 1:
        return True # base case
    if str[0] == str[len(str) - 1]:
        return rec_palindrome(str[1:-1]) # recursive call
    else:
        return False
print(rec_palindrome('mother'))
