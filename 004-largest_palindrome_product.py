#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem description:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Author: Santiago Narváez Rivas.
Date: 6-Mar-2016
"""

def is_palindrome(n):
    """
    Determines whether n is a palindrome or not
    :param n: number
    :return: true if n is a palindrome, false otherwise
    """
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    biggest = 0
    for d1 in range(999, 99, -1):
        for d2 in range(999, 99, -1):
            m = d1 * d2
            if is_palindrome(m) and m > biggest:
                print("{0} * {1} = {2}".format(d1, d2, m))
                biggest = m
    print(biggest)