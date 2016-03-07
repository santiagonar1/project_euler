#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem description:
The sum of the squares of the first ten natural numbers is, 1 ^ 2 + 2 ^ 2 + ... + 10 ^ 2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10) ^ 2 = 55 ^ 2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Author: Santiago Narváez Rivas.
Date: 7-Mar-2016
"""
import math

def sumatory(k):
    """
    Calculates the sumatory 1 + 2 + ... + k
    :param k:
    :return: The sumatory 1 + 2 + ... + k
    """
    return (k * (k + 1)) / 2


def sum_of_squares(k):
    """
    Calculates the sumatory 1 ^ 2 + 2 ^ 2 + ... + k ^ 2
    :param k:
    :return: The sumatory 1 ^ 2 + 2 ^ 2 + ... + k ^ 2
    """
    return (k * (k + 1) * (2 * k + 1)) / 6


if __name__ == "__main__":
    k = 100
    r = sum_of_squares(k) - math.pow(sumatory(k), 2)
    print(r)