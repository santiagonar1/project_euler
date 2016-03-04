#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

Author: Santiago Narváez Rivas.
Date: 3-Mar-2016
"""

N1 = 3
N2 = 5
L = 1000


def get_multiples(n, limit):
    """
    :param n: Multiples from
    :param limit: Multiples until
    :return: All the n multiples below limit
    """
    multiples = []
    i = 1
    while n * i < limit:
        multiples.append(n*i)
        i += 1
    return multiples


if __name__ == "__main__":
    mult3 = get_multiples(N1, L)
    mult5 = get_multiples(N2, L)
    # Se concatenan los elementos de 3 que no estan en 5, con los elementos de 5
    mult = list(set(mult3) - set(mult5)) + mult5
    print(sum(mult))