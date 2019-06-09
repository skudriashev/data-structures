from unittest import TestCase

from my_queue.my_queue import Queue


class TestQueue(TestCase):

    def setUp(self):
        super().setUp()
        self.queue = Queue()

    def test_enqueue_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)

    def test_peek(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(self.queue.size(), 2)

    def test_size(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.size(), 2)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())

        self.queue.enqueue(1)

        self.assertFalse(self.queue.is_empty())

        self.queue.dequeue()

        self.assertTrue(self.queue.is_empty())
