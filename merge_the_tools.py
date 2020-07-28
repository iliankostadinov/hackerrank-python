#!/usr/bin/env python3

from collections import OrderedDict


def merge_the_tools(string, step):
    l = []
    if step != 0:
        for i in range(0, len(string), step):
            word = string[i:i+step]
            i += step
            l.append(word)

        for w in l:
                print(''.join(OrderedDict.fromkeys(w).keys()))
    else:
        pass



string, k = input(), int(input())
merge_the_tools(string, k)
