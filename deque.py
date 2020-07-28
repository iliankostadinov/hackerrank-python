#!/usr/bin/env python3

from collections import deque


def pilingUp(q):
    if len(d) > 1:
        value = "Yes"
        currentEl = 0
        if d[0] > d[-1]:
            currentEl = d[0]
            d.popleft()
        else:
            currentEl = d[-1]
            d.pop()
        for _ in range(len(d) - 1):
            if d[0] > d[-1] and d[0] <= currentEl:
                d.popleft()
            else:
                if d[-1] <= currentEl:
                    d.pop()
                else:
                    value = "No"
                    break
    else:
        value = "Yes"
    return value


if __name__ == "__main__":
    # number of testcases
    t = int(input())
    results = []
    for _ in range(t):
        d = deque()
        # number of cubes
        n = int(input())
        # side lenght of each cube
        row_of_cubes = map(int, input().split())
        # put elements in deque
        for e in row_of_cubes:
            d.append(e)
        results.append(pilingUp(d))
    for i in results:
        print(i)

