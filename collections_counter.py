#!/usr/bin/env python3
"""Solution of how much money Raghu earned"""

from collections import Counter


def inp_to_str():
    """Convert input from space separated
       values to list from them.
    """
    input_str = input("Please enter values separeted by space\n")
    return list(input_str.split())


def list_to_int(str_list):
    """Convert list from strings to int"""
    return [int(x) for x in str_list]


def inp_to_int():
    """Convert input from space separated
       values to intiger list from them.
    """
    return list_to_int(inp_to_str())


def main():
    """main function"""
    # NUM_OF_SHOES = int(input("Please enter number of shoes: "))
    shoes_counter = Counter(inp_to_int())
    num_of_custoum = int(input("Please enter number of customers: "))
    print("Please enter space separated \
          values of the desired by the customers:")
    total_sum = 0
    for _ in range(num_of_custoum):
        tmp_list = inp_to_int()
        if shoes_counter[tmp_list[0]] > 0:
            total_sum += tmp_list[1]
            shoes_counter.update({tmp_list[0]: -1})

    print(total_sum)


if __name__ == "__main__":
    main()
