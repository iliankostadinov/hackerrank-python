#!/usr/bin/python
from __future__ import print_function

import sys

if __name__ == '__main__':
    n = int(input())

    for i in xrange(1,n+1):
        print(i, sep=' ', end='', file=sys.stdout)
