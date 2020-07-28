#!/usr/bin/env python3

size_of_grp = 5

inp_list = "1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2".split()
set_l = set(inp_list)
cap_room = ""
for element in set_l:
    inp_list.remove(element)
    if not element in inp_list:
        cap_room = element
        break
print(int(cap_room))

