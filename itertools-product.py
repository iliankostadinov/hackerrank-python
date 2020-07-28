#!/usr/bin/env python3

from itertools import product


a = list(map(int,input()))
b = input()

print(a)
a = a.split()
a = list(a)

b = b.split()
b = list(b)

a_l = list(map(int, a))
b_l = list(map(int, b))

p = product(a_l, b_l)
for i in p:
    print(i, end= ' ')
