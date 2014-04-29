#!/usr/bin/env python

"""binarysearch.py: Program to implement binary search"""

__author__ = 'Rohit Sinha'


def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)/2
        if alist[mid] == item:
            return True
        else:
            if alist[mid] > item:
                return binary_search(alist[:mid], item)
            else:
                return binary_search(alist[mid+1:], item)

if __name__ == "__main__":
    list = [0, 4, 6, 45, 89, 23, 34]
    print(binary_search(list, 6))
    print(binary_search(list, 22))