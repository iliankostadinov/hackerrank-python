#!/usr/bin/env python3

from collections import namedtuple

n = int(input())
d = {}
Student = namedtuple('Student', 'ID MARKS NAME CLASS')
score = 0
v1, v2, v3, v4 = input().split()
for std in range(n):
    MARKS, ID, NAME, CLASS = input().split()
    d["std{}".format(std)] = Student(ID=ID, MARKS=MARKS, NAME=NAME, CLASS=CLASS)

if v1 == "MARKS":
    for tup in d.values():
        score += int(tup.MARKS)
if v2 == "MARKS":
    for tup in d.values():
        score += int(tup.ID)
if v3 == "MARKS":
    for tup in d.values():
        score += int(tup.NAME)
if v4 == "MARKS":
    for tup in d.values():
        score += int(tup.CLASS)

result = score/n
print('%.2f' % result)
