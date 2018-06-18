# https://stonesoupprogramming.com/2017/05/21/circular-linked-list-python/

from enum import Enum


class NodeConstants(Enum):
    FRONT_NODE = 1


class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node

    def __str__(self):
        if self.element:
            return self.element.__str__()
        else:
            return 'Empty Node'

    def __repr__(self):
        return self.__str__()


class CircularLinkedList:
    def __init__(self):
        self.head = Node(element=NodeConstants.FRONT_NODE)

        self.head.next_node = self.head

    def size(self):
        count = 0
        current = self.head.next_node

        while current != self.head:
            count += 1
            current = current.next_node

        return count

    def insert_front(self, data):
        node = Node(element=data, next_node=self.head.next_node)
        self.head.next_node = node

    def insert_last(self, data):
        current_node = self.head.next_node

        while current_node.next_node != self.head:
            current_node = current_node.next_node

        node = Node(element=data, next_node=current_node.next_node)
        current_node.next_node = node

    def insert(self, data, position):
        if position == 0:
            self.insert_front(data)
        elif position == self.size():
            self.insert_last(data)
        else:
            if 0 < position < self.size():
                current_node = self.head.next_node
                current_pos = 0

                while current_pos < position - 1:
                    current_pos += 1
                    current_node = current_node.next_node

                node = Node(data, current_node.next_node)
                current_node.next_node = node
            else:
                raise IndexError

    def remove_first(self):
        self.head.next_node = self.head.next_node.next_node

    def remove_last(self):
        current_node = self.head.next_node

        while current_node.next_node.next_node != self.head:
            current_node = current_node.next_node

        current_node.next_node = self.head

    def remove(self, position):
        if position == 0:
            self.remove_first()
        elif position == self.size():
            self.remove_last()
        else:
            if 0 < position < self.size():
                current_node = self.head.next_node
                current_pos = 0

                while current_pos < position - 1:
                    current_node = current_node.next_node
                    current_pos += 1

                current_node.next_node = current_node.next_node.next_node
            else:
                raise IndexError

    def fetch(self, position):
        if 0 <= position < self.size():
            current_node = self.head.next_node
            current_pos = 0

            while current_pos < position:
                current_node = current_node.next_node
                current_pos += 1

            return current_node.element
        else:
            raise IndexError


import unittest
from random import randint


class TestCircularLinkedList(unittest.TestCase):
    names = ['Bob Belcher',
             'Linda Belcher',
             'Tina Belcher',
             'Gene Belcher',
             'Louise Belcher']

    def test_init(self):
        dll = CircularLinkedList()
        self.assertIsNotNone(dll.head)
        self.assertEqual(dll.size(), 0)

    def test_insert_front(self):
        dll = CircularLinkedList()
        for name in TestCircularLinkedList.names:
            dll.insert_front(name)

        self.assertEqual(dll.fetch(0), TestCircularLinkedList.names[4])
        self.assertEqual(dll.fetch(1), TestCircularLinkedList.names[3])
        self.assertEqual(dll.fetch(2), TestCircularLinkedList.names[2])
        self.assertEqual(dll.fetch(3), TestCircularLinkedList.names[1])
        self.assertEqual(dll.fetch(4), TestCircularLinkedList.names[0])

    def test_insert_last(self):
        dll = CircularLinkedList()
        for name in TestCircularLinkedList.names:
            dll.insert_last(name)

        for i in range(len(TestCircularLinkedList.names) - 1):
            self.assertEqual(dll.fetch(i), TestCircularLinkedList.names[i])

    def test_insert(self):
        dll = CircularLinkedList()
        for name in TestCircularLinkedList.names:
            dll.insert_last(name)

        pos = randint(0, len(TestCircularLinkedList.names) - 1)

        dll.insert('Teddy', pos)
        self.assertEqual(dll.fetch(pos), 'Teddy')

    def test_remove_first(self):
        dll = CircularLinkedList()
        for name in TestCircularLinkedList.names:
            dll.insert_last(name)

        for i in range(dll.size(), 0, -1):
            self.assertEqual(dll.size(), i)
            dll.remove_first()

    def test_remove_last(self):
        dll = CircularLinkedList()
        for name in TestCircularLinkedList.names:
            dll.insert_last(name)

        for i in range(dll.size(), 0, -1):
            self.assertEqual(dll.size(), i)
            dll.remove_last()

    def test_remove(self):
        dll = CircularLinkedList()
        for name in TestCircularLinkedList.names:
            dll.insert_last(name)

        dll.remove(1)

        self.assertEqual(dll.fetch(0), 'Bob Belcher')
        self.assertEqual(dll.fetch(1), 'Tina Belcher')
        self.assertEqual(dll.fetch(2), 'Gene Belcher')
        self.assertEqual(dll.fetch(3), 'Louise Belcher')


if __name__ == '__main__':
    unittest.main()
