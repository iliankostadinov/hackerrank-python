#!/usr/bin/env python3
"""Print rangoli of size NUM"""


def print_rangoli(size):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z']

    alphabet_slice = alphabet[:size]
    elements = alphabet_slice.copy()
    alphabet_slice.pop(0)

    for i in alphabet_slice:
        elements.insert(0, i)

    other = 4*size - 3
    matrix = [['-' for i in range(other)] for k in range(size)]

    for i in range(size):
        n = i*2
        for k in range(len(elements)):
            matrix[i][n] = elements[k]
            n += 2
        if i < size-1:
            elements.pop((len(elements)//2) - 1)
            elements.pop((len(elements)//2) - 1)

    # for i in range(size):
    #     for k in range(4*size-3):
    #         print(matrix[i][k], end='')
    matrix.reverse()
    print('\n'.join(map(''.join, matrix)))
    matrix.pop()
    matrix.reverse()
    print('\n'.join(map(''.join, matrix)))


if __name__ == "__main__":
    NUM = int(input("Enter number: "))
    print_rangoli(NUM)
