#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem description:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-
valued terms.

Author: Santiago Narváez Rivas.
Date: 3-Mar-2016
"""
L = 4000000

def fibonacci(limit):
    """
    :param limit: Max. element
    :return: fibonacci series until limit (not including limit)
    """
    f = [1, 2]
    while f[-1] < limit:
        f.append(f[-1]+f[-2])
    f.pop()
    return f

if __name__ == "__main__":
    sum = 0
    for e in fibonacci(L):
        if e % 2 == 0: sum += e

    print(sum)