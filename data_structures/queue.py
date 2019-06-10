class Queue:

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Enqueue item at the beginning of the queue.

        Time complexity is O(n).
        """
        self._items.insert(0, item)

    def dequeue(self):
        """Dequeue item from the end of the queue.

        Time complexity is O(1).
        """
        if self._items:
            return self._items.pop()

    def peek(self):
        """Return next value to be returned by dequeue.

        Time complexity is O(1).
        """
        if self._items:
            return self._items[-1]

    def size(self):
        """Get queue size.

        Time complexity is O(1).
        """
        return len(self._items)

    def is_empty(self):
        """Return if queue is empty.

        Time complexity is O(1).
        """
        return self.size() == 0
