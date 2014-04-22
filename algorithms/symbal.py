#!/usr/bin/env python

"""symbal.py: Check for braces to be balanced"""

from stack import Stack

__author__ = 'Rohit Sinha'


def match_braces(opener, closer):
    return "({[".index(opener) == ")}]".index(closer)


def brace_checker(brace_string):
    stack = Stack()
    isbal = True
    index = 0
    while index < len(brace_string) and isbal:
        if brace_string[index] in "({[":
            stack.push(brace_string[index])
        else:
            if stack.isEmpty():
                isbal = False
            else:
                opener = stack.pop()
                if not match_braces(opener, brace_string[index]):
                    isbal = False
        index += 1
    if stack.isEmpty() and isbal:
        return True
    else:
        return False

# check the above code
if __name__ == '__main__':
    print(brace_checker("([({})])"))
    print(brace_checker("[({)]"))