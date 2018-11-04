#!/usr/bin/python3

"""
Given the names and grades for each student in a Physics class of students, store them in
a nested list and print the name(s) of any student(s) having the second lowest grade.
"""

if __name__ == '__main__':

    nl = []
    ns = input("Plese enter number of students\n")
    for n in range(int(ns)):
        sn = input("Please input student name\n")
        sg = float(input("Please input student grade\n"))
        snl = [sn]
        snl.append(sg)
        nl.append(snl)

    nl.sort(key=lambda student: student[1])

    i = 1
    if nl[0][1] == nl[1][1]:
        listForPrint = [nl[0][0]]
        while (nl[i-1][1] == nl[i][1]):
            listForPrint.append(nl[i][0])
            i += 1
        if i == int(ns) - 1:
            listForPrint = [nl[i][0]]
        else:
            listForPrint = [nl[i][0]]
            while (nl[i][1] == nl[i+1][1]):
                listForPrint.append(nl[i+1][0])
                i += 1
            listForPrint.sort()

    else:
        listForPrint = [nl[i][0]]
        while (nl[i][1] == nl[i+1][1]):
            listForPrint.append(nl[i+1][0])
            i += 1
            listForPrint.sort()
            if i == int(ns)-1:
                break
    if len(listForPrint) > 1:
        for names in listForPrint:
            print(names)
    else:
        print(listForPrint[0])



