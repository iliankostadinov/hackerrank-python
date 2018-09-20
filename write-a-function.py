#!/usr/bin/python

def is_leap(year):
    leap = False


    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

if __name__ == '__main__':

    year = int(raw_input())

    if year < 1900:
        print "You should enter year between 1900 and 10 on power 5"
        year = int(raw_input())
    elif year > 10**5:
        print "You should enter year between 1900 and 10 on power 5"
        year = int(raw_input())

    print is_leap(year)
