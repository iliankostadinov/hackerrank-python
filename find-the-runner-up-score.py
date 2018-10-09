#!/usr/bin/python3

if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().split()))

    swap = 0
    for elements in (arr):
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                swap = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = swap
    second = arr[0]
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            second = arr[i+1]
            break

    print(second)
