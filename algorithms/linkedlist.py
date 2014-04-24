#!/usr/bin/env python

"""linkedlist.py: Class representing linkedlist"""

from listnode import ListNode

__author__ = 'Rohit Sinha'


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = ListNode(item)

        if self.head is None:
            self.head = temp
        else:
            cur = self.head
            # traverse to the last node and append there
            while cur.get_next() is not None:
                cur = cur.get_next()
            cur.set_next(temp)

    def size(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.get_next()

        return count

    def search(self, key):
        cur = self.head
        found = False
        while cur is not None and not found:
            if cur.get_data() == key:
                found = True
            else:
                cur = cur.get_next()
        return found

    def remove(self, item):
        cur = self.head
        prev = None
        found = False
        # if the element is present then delete it
        while cur is not None and not found:
            if cur.get_data() == item:
                found = True
            else:
                prev = cur
                cur = cur.get_next()

        if prev is None:
            self.head = cur.get_next()
        elif cur is not None:
            prev.set_next(cur.get_next())


if __name__ == '__main__':
    list = LinkedList()
    print(list.is_empty())
    list.add(1)
    list.add(2)
    list.add(3)
    list.add(4)
    print(list.size())
    print(list.search(2))
    print(list.search(5))
    list.remove(2)
    print(list.search(2))
    list.remove(5)