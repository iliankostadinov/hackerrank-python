#!/usr/bin/python


N = int(raw_input("Plase enter a number\n"))

if N < 1 and N > 100:
    print("You entered number out of range, please enter number between 1 and 100\n")
    N = int(raw_input("Plase enter a number\n"))

