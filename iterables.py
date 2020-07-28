#!/usr/bin/env python3

from itertools import combinations

n = int(input())
s = input().split()
k = int(input())

total = 0
match = 0

for _ in combinations(s, k):
    total += 1
    if 'a' in _:
        match += 1

print(match/total)
