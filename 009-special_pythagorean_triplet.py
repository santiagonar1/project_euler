#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem description:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a ^ 2 + b ^ 2 = c ^ 2

For example, 3 ^ 2 + 4 ^ 2 = 9 + 16 = 25 = 5 ^ 2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


Author: Santiago Narváez Rivas.
Date: 11-Mar-2016
"""

PERIMETER = 1000
# 16 primeras ternas pitagóricas primitivas / First 16th primitive Pythagorean triples
PPT = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
       (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53),
       (11, 60, 61), (16, 63, 65), (33, 56, 65), (48, 55, 73),
       (13, 84, 85), (36, 77, 85), (39, 80, 89), (65, 72, 97)]


if __name__ == "__main__":
    for t in PPT:
        if PERIMETER % sum(t) == 0:
            # Los multiplos de una terna pitagorica primitiva también son ternas pitagóricas, luego basta encontrar
            # una terna primitiva cuya suma sea divisor del PERIMETRO. Ver:
            # https://es.wikipedia.org/wiki/Terna_pitag%C3%B3rica
            r = [n * (PERIMETER // sum(t)) for n in t]
            mult = r[0] * r[1] * r[2]
            print("({r[0]}, {r[1]}, {r[2]}) ==> {mult}".format(r=r, mult=mult))
            break
