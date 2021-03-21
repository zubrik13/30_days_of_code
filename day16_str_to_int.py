import sys


def string_to_int(S):
    try:
        n = int(S)
        return print(n)
    except ValueError:
        print("Bad String")


# S = input().strip()
# S = 4
S = 'az'

string_to_int(S)
