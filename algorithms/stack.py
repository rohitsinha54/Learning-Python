#!/usr/bin/env python

"""stack.py: Stack implementation"""

__author__ = 'Rohit Sinha'


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items).strip('[]')


if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(5)
    s.push('Hello')
    print(s.peek())
    s.push(True)
    print(s.peek())
    print(s.size())
    print(s.pop())
    print(s)
