#!/usr/bin/env python3

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':

    def mat(n, m):
        n = int(n)
        m = int(m)

        # printing upper part
        element = ".|."
        for i in range(1, n, 2):
            dash = "-"
            line = element * i
            dash = dash * ((m - len(line))//2)
            line = dash + line + dash
            print(line)

        # print welcome
        dash = "-"
        welcome = "WELCOME"
        dash = dash * ((m - len(welcome))//2)
        welcome = dash + welcome + dash
        print(welcome)

        # print bottom part
        for i in range(n-2, 0, -2):
            dash = "-"
            line = element * i
            dash = dash * ((m - len(line))//2)
            line = dash + line + dash
            print(line)

    N, M = input().split()
    mat(N, M)


