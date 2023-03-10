# python3
#221RDB014 Mihails Ruhļa 13. grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i));
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) < 1:
                return i + 1
            cur = opening_brackets_stack.pop()
            if(not are_matching(cur.char, next)):
                return i + 1
            pass
    return "Success"


def main():
    text = input()
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
