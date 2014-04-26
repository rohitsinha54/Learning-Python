#!/usr/bin/env python

"""insertionsort.py: Program to implement insertion sort"""

__author__ = 'Rohit Sinha'


def insertion_sort(alist):
    for selected in range(1, len(alist)):
        selected_value = alist[selected]
        pos = selected
        while pos > 0 and alist[pos - 1] > selected_value:
            alist[pos] = alist[pos - 1]
            pos -= 1

        alist[pos] = selected_value

if __name__ == '__main__':
    alist = [84, 69, 76, 86, 94, 91]
    insertion_sort(alist)
    print(alist)