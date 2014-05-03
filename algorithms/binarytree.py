#!/usr/bin/env python

"""binarytree.py: Implementation of binary tree"""

__author__ = 'Rohit Sinha'


class BinaryTree:
    def __init__(self, root_key):
        self.value = root_key
        self.left = None
        self.right = None

    def insert_left(self, new_key):
        if self.left is None:
            self.left = BinaryTree(new_key)
        else:
            new_node = BinaryTree(new_key)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, new_key):
        if self.right is None:
            self.right = BinaryTree(new_key)
        else:
            new_node = BinaryTree(new_key)
            new_node.right = self.right
            self.right = new_node

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_value(self):
        return self.value

    def set_value(self, new_val):
        self.value = new_val


if __name__ == '__main__':
    r = BinaryTree('h')
    print(r.get_value())
    print(r.get_left())
    r.insert_left('e')
    print(r.get_left())
    print(r.get_left().get_value())
    r.insert_right('y')
    print(r.get_right())
    print(r.get_right().get_value())
    r.get_right().set_value('i')
    print(r.get_right().get_value())