#!/usr/bin/python3

if __name__ == '__main__':
    
    arr = [1,3,5]
    print("Please enter nuber of commands you want to execute")
    N = int(input())
    for i in range(0,N):
        command = input()
        if command == 'print':
            print(arr)


