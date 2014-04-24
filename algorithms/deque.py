#!/usr/bin/env python

"""deque.py: Deque implementation"""

__author__ = 'rohitsinha'

class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items).strip('[]')

if __name__ == '__main__':
    d = Deque()
    print(d.isEmpty())
    d.addFront(5)
    d.addRear('Hello')
    print(d.removeFront())
    d.addFront(True)
    print(d.removeRear())
    print(d.size())
    print(d.removeFront())
    d.addRear('Bye')
    d.addFront('Bye')
    print(d)