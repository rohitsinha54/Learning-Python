#!/usr/bin/env python

"""quicksort.py: Program to implement quicksort"""

__author__ = 'Rohit Sinha'


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, start, end):
    if start < end:
        pivot = partition(alist, start, end)
        quick_sort_helper(alist, start, pivot - 1)
        quick_sort_helper(alist, pivot + 1, end)


def partition(alist, start, end):
    pivot_value = alist[start]

    left_pointer = start+1
    right_pointer = end

    done = False

    while not done:
        while left_pointer <= right_pointer and alist[left_pointer] <= pivot_value:
            left_pointer += 1

        while right_pointer >= left_pointer and alist[right_pointer] >= pivot_value:
            right_pointer -= 1

        if left_pointer > right_pointer:
            done = True

        else:
            alist[left_pointer], alist[right_pointer] = alist[right_pointer], alist[left_pointer]

    alist[right_pointer], alist[start] = alist[start], alist[right_pointer]

    return right_pointer

if __name__ == '__main__':
    alist = [84, 69, 76, 86, 94, 91]
    quick_sort(alist)
    print(alist)