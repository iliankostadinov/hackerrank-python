#!/usr/bin/env python3
"""Given a set and number of other sets. These number of sets have to perform
some specific mutation operations on set execute those operations and print
the sum of elements from set
"""


def set_mutations():
    """main work is done here"""
    set_len = int(input())
    set_a = set(map(int, input().split()))
    num_of_operation = int(input())
    for _ in range(num_of_operation):
        command, lenght = input().split()
        tmp_set = set(map(int, input().split()))
        getattr(set_a, command)(tmp_set)
    print(sum(set_a), set_len)


if __name__ == "__main__":
    set_mutations()
