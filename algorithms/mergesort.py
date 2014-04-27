#!/usr/bin/env python

"""mergesort.py: Program to implement merge sort"""

__author__ = 'Rohit Sinha'


def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    middle = len(alist) / 2
    left = alist[:middle]
    right = alist[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left, right))


def merge(left, right):
    result = []

    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    if left:
        result.extend(left[left_index:])

    if right:
        result.extend(right[right_index:])

    return result


if __name__ == '__main__':
    alist = [84, 69, 76, 86, 94, 91]
    alist = merge_sort(alist)
    print(alist)