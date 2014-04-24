#!/usr/bin/env python

"""listnode.py: Class representing nodes in lists"""

__author__ = 'Rohit Sinha'


class ListNode:
    def __init__(self, val):
        self.data = val
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, val):
        self.data = val

    def set_next(self, new_next):
        self.next = new_next