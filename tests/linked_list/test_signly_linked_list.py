from unittest import TestCase

from linked_list.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(TestCase):

    def setUp(self):
        super().setUp()
        self.linked_list = SinglyLinkedList()

    def test_repr(self):
        self.assertEqual(repr(self.linked_list), "SinglyLinkedList(head=None, size=0)")

    def test_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())

    def test_add_front(self):
        self.linked_list.add_front(1)

        self.assertFalse(self.linked_list.is_empty())

    def test_size(self):
        self.assertEqual(self.linked_list.size(), 0)

        self.linked_list.add_front(1)
        self.linked_list.add_front(2)

        self.assertEqual(self.linked_list.size(), 2)

    def test_search(self):
        self.linked_list.add_front(1)
        self.linked_list.add_front(2)

        self.assertEqual(self.linked_list.search(1).data, 1)
        self.assertEqual(self.linked_list.search(2).data, 2)
        self.assertIsNone(self.linked_list.search(3))

    def test_remove(self):
        self.linked_list.add_front(1)
        self.linked_list.add_front(2)
        self.linked_list.add_front(3)

        self.linked_list.remove(2)

        self.assertEqual(self.linked_list.size(), 2)
        self.assertIsNone(self.linked_list.search(2))
        self.assertEqual(self.linked_list.search(1).data, 1)
        self.assertEqual(self.linked_list.search(3).data, 3)

    def test_remove_head(self):
        self.linked_list.add_front(1)
        self.linked_list.add_front(2)
        self.linked_list.add_front(3)

        self.linked_list.remove(3)

        self.assertEqual(self.linked_list.size(), 2)
        self.assertIsNone(self.linked_list.search(3))
        self.assertEqual(self.linked_list.search(1).data, 1)
        self.assertEqual(self.linked_list.search(2).data, 2)

    def test_remove_tail(self):
        self.linked_list.add_front(1)
        self.linked_list.add_front(2)
        self.linked_list.add_front(3)

        self.linked_list.remove(1)

        self.assertEqual(self.linked_list.size(), 2)
        self.assertIsNone(self.linked_list.search(3))
        self.assertEqual(self.linked_list.search(2).data, 2)
        self.assertEqual(self.linked_list.search(3).data, 3)

    def test_remove_head_only(self):
        self.linked_list.add_front(1)

        self.linked_list.remove(1)

        self.assertEqual(self.linked_list.size(), 0)
