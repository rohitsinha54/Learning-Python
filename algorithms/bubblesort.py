#!/usr/bin/env python

"""bubblesort.py: Program to implement bubble sort"""

__author__ = 'Rohit Sinha'


def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

if __name__ == '__main__':
    alist = [84, 69, 76, 86, 94, 91]
    bubble_sort(alist)
    print(alist)
