#!/usr/bin/python

if __name__ == '__main__':

    n = int(raw_input())

    if n < 1:
        print "You should enter number in range 1 to 20"
    elif n > 20:
        print "You should enter number in range 1 to 20"

    for i in  range(0,n):
        c = i*i
        print c
