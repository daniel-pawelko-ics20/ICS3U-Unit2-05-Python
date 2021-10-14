#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This program takes advantage of global and local variables

first = 10


def local_variable():
    # this shows what happens with local variables

    first = 21
    second = 12
    third = first + second
    print(f"Local first Variable: {first}")
    print(f"second Variable: {second}")
    print(f"{first} + {second} = {third}(third)")


def global_varialbe():
    # this shows what heppens with global variables
    global first
    first = first + 1
    second = 12
    third = first + second
    print(f"\nglobal first Variable: {first}")
    print(f"second Variable: {second}")
    print(f"{first} + {second} = {third}(third)")


def main():
    # this function shows how local and global variables work

    local_variable()
    global_varialbe()


if __name__ == "__main__":
    main()
