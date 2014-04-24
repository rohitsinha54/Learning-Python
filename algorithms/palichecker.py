#!/usr/bin/env python

"""palichecker.py: Program to check if a given string is palindrome or not"""

from deque import Deque

__author__ = 'Rohit Sinha'


def pali_checker(string):
    dq = Deque()

    for s in string:
        dq.addRear(s)

    eq_flag = True

    while dq.size() > 1 and eq_flag:
        left = dq.removeFront()
        right = dq.removeRear()

        if left != right:
            eq_flag = False

    return eq_flag


if __name__ == '__main__':
    print(pali_checker('rohit'))
    print(pali_checker('aaaabbbbaaa'))
    print(pali_checker('123321'))
    print(pali_checker('1234321'))