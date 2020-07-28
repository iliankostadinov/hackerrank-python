#!/usr/bin/env python3

import os
import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    pattern = '%a %d %b %Y %H:%M:%S %z'
    date1 = int(datetime.datetime.strptime(t1, pattern).timestamp())
    date2 = int(datetime.datetime.strptime(t2, pattern).timestamp())

    print(abs(date1 - date2))
    return abs(date1 - date2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
