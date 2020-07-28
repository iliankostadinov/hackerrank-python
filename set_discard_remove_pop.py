#!/usr/bin/env python3
"""Print sum of set after executed commands"""


def main():
    """Main function"""

    # num_of_elements = int(input())
    set_of_elements = set(map(int, input().split()))

    for _ in range(int(input())):
        input_command = input()

        if input_command == "pop":
            set_of_elements.pop()
        else:
            command, num = input_command.split()
            num = int(num)
            if command == "remove":
                set_of_elements.remove(num)
            else:
                set_of_elements.discard(num)

    print(sum(set_of_elements))


if __name__ == "__main__":
    main()
