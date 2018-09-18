#!/usr/bin/python


N = int(raw_input("Plase enter a number\n"))

if N < 1:
    print "You entered number out of range, please enter number between 1 and 100\n"
    N = int(raw_input("Plase enter a number\n"))
elif N > 100:
    print "You entered number out of range, please enter number between 1 and 100\n"
    N = int(raw_input("Plase enter a number\n"))

if N % 2 != 0:
    print "Weird"
elif N < 6:
    print "Not Weird"
elif N < 21:
    print "Weird"
elif N > 20:
    print "Not Weird"
