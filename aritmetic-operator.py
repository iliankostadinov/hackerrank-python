#!/usr/bin/python

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

    if a < 1:
        print "You enter number out of scope, plese enter number bigger then 1"
    elif a > 10**10:
        print "You enterd too big number please enter smaller one"

    if b < 1:
        print "You enter number out of scope, plese enter number bigger then 1"
    elif b > 10**10:
        print "You enterd too big number please enter smaller one"

    c = a + b
    d = a - b
    e = a * b

    print c
    print d
    print e
