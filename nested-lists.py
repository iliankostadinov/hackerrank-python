#!/usr/bin/python3

if __name__ == '__main__':

    nl = []
    ns = input("Plese enter number of students\n")
    for n in range(int(ns)):
        sn = input("Please input student name\n")
        sg = input("Please input student grade\n")
        snl = [sn]
        snl.append(sg)
        nl.append(snl)
