from unittest import TestCase

from data_structures.stack import Stack


class TestStack(TestCase):

    def setUp(self):
        super().setUp()
        self.stack = Stack()

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty(self):
        self.assertIsNone(self.stack.pop())

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.peek(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)

    def test_size(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.size(), 2)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

        self.stack.push(1)

        self.assertFalse(self.stack.is_empty())

        self.stack.pop()
