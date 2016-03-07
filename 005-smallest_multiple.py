#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Author: Santiago Narváez Rivas.
Date: 6-Mar-2016
"""

def divisible_by(n, numbers):
    """
    Determines if n is divisible by all the numbers
    :param n: number
    :param numbers: all the numbers
    :return: true if n is divisible by all the numbers
    """
    for d in numbers:
        if n % d != 0:
            return False

    return True


if __name__ == "__main__":
    # Solo debemos comprobar que es divisible entre 11 y 20 (p. ej., si es divisible por 20 => lo es por 2, 4, 5, 10)
    numbers = list(range(11, 21))

    max = 1
    for i in range(1, 21):
        max *= i

    for i in range(numbers[-1], max + 1, numbers[-1]):
        if divisible_by(i, numbers):
            print(i)
            break

