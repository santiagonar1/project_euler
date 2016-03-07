#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Author: Santiago Narváez Rivas.
Date: 6-Mar-2016
"""

import math

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

def first_method():
    numbers = list(range(11, 21))

    max = 1
    for i in range(1, 21):
        max *= i

    for i in range(numbers[-1], max + 1, numbers[-1]):
        if divisible_by(i, numbers):
            return i

def second_method(primes, k):
    """
    Es un método optimizado. Se basa en descomponer la respuesta N en la multiplicación de los primos que componen
    la secuencia: N = primes[i] ^ a[i], para todo primes[i] <= k.
    :param primes: List of primes <= k
    :param k: max. value
    :return:
    """
    N = 1
    i = 0
    limit = math.sqrt(k)
    check = True
    a = [1 for n in range(0, len(primes))]
    for p in primes:
        if check:
            if p <= limit:
                # a[i] debe ser una potencia tal que primes[i] ^ a[i] <= k. Estableciendo la igualdad tenemos que
                # primes[i] ^ a[i] = k ==> a[i]*log(primes[i]) = log(k)
                a[i] = math.floor(math.log(k) / math.log(p))
            else:
                check = False
        N *= math.pow(p, a[i])
        i += 1
    return N



if __name__ == "__main__":
    # Solo debemos comprobar que es divisible entre 11 y 20 (p. ej., si es divisible por 20 => lo es por 2, 4, 5, 10)
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    print(second_method(primes, 20)) # método optimizado
    print(first_method())
