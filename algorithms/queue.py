#!/usr/bin/env python

"""queue.py: Queue implementation"""

__author__ = 'rohitsinha'

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items).strip('[]')

if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    q.enqueue(5)
    q.enqueue('Hello')
    print(q.dequeue())
    q.enqueue(True)
    print(q.dequeue())
    print(q.size())
    print(q.dequeue())
    q.enqueue('Bye')
    q.enqueue('Bye')
    print(q)