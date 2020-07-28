#!/usr/bin/env python3

from itertools import product

k, m = input().split()

k = int(k)
m = int(m)

d = {}
for i in range(k):
    d["key{}".format(i)] = list(map(int, input().split()))

print(d)

for v in d.values():
    v.pop(0)

combinations = product(*d.values())

result = 0
for x in combinations:
    tmp = sum(map(lambda y: y*y, x))
    print(tmp % m)
    if tmp % m > result:
        result = tmp % m
print(result)
