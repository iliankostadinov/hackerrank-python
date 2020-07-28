#!/usr/bin/env python3

from collections import defaultdict

n, m = map(int, input().split())
d_m = defaultdict(list)
d_n = defaultdict(list)
for i in range(n):
    d_n[input()].append(i+1)
for i in range(m):
    d_m[input()].append(i+1)

for i in d_m.keys():
    print(i)
    if not d_n[i]:
        print("-1")
    else:
        print(*d_n[i])
