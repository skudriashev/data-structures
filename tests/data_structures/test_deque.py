from unittest import TestCase

from data_structures.deque import Deque


class TestDeque(TestCase):

    def setUp(self):
        super().setUp()
        self.deque = Deque()

    def test_add_remove_front(self):
        self.deque.add_front(1)
        self.deque.add_front(2)

        self.assertEqual(self.deque.size(), 2)

        self.assertEqual(self.deque.remove_front(), 2)
        self.assertEqual(self.deque.remove_front(), 1)
        self.assertEqual(self.deque.size(), 0)

    def test_add_remove_back(self):
        self.deque.add_back(1)
        self.deque.add_back(2)

        self.assertEqual(self.deque.size(), 2)

        self.assertEqual(self.deque.remove_back(), 2)
        self.assertEqual(self.deque.remove_back(), 1)
        self.assertEqual(self.deque.size(), 0)

    def test_add_front_remove_back(self):
        self.deque.add_front(1)
        self.deque.add_front(2)

        self.assertEqual(self.deque.remove_back(), 1)
        self.assertEqual(self.deque.remove_back(), 2)

    def test_add_back_remove_front(self):
        self.deque.add_back(1)
        self.deque.add_back(2)

        self.assertEqual(self.deque.remove_front(), 1)
        self.assertEqual(self.deque.remove_front(), 2)

    def test_is_empty(self):
        self.assertTrue(self.deque.is_empty())

        self.deque.add_front(1)
        self.assertFalse(self.deque.is_empty())

        self.deque.remove_front()
        self.assertTrue(self.deque.is_empty())

        self.deque.add_back(1)
        self.assertFalse(self.deque.is_empty())

        self.deque.remove_back()
        self.assertTrue(self.deque.is_empty())
