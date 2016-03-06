#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem description:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?


Author: Santiago Narváez Rivas.
Date: 6-Mar-2016
"""
N = 600851475143

def get_factors(n):
    """
    Returnes all factors from a number
    :param n: Number
    :return: A list with all the factors from n
    """
    r = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            # Si ya esta significa que encontramos todos los factores
            if i in r:
                break
            else:
                # Si i es un factor, entonces x = n // i también lo es (i * x = n)
                r.append(i)
                r.append(n // i)
    r.sort()
    return r

def is_prime(n):
    """
    Determines if a number is prime or not
    :param n: Number
    :return: true if number is prime, false otherwise
    """
    return len(get_factors(n)) == 2 # Only 2 factors, n and 1.


if __name__ == "__main__":
    for n in get_factors(N)[::-1]:
        if is_prime(n):
            print(n)
            break
