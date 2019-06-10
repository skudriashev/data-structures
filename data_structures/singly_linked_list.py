class Node:
    __slots__ = ('data', 'next')

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return "{}(data={}, next={})".format(self.__class__.__name__, self.data, self.next)


class SinglyLinkedList:

    def __init__(self):
        self._head = None
        self._size = 0

    def __repr__(self):
        return "{}(head={}, size={})".format(self.__class__.__name__, self._head, self._size)

    def is_empty(self):
        """Return if linked list is is empty."""
        return self._head is None

    def add_front(self, data):
        """Add new data node in front."""
        self._head = Node(data, self._head)
        self._size += 1

    def size(self):
        """Get linked list size."""
        return self._size

    def search(self, data):
        """Search for a node with a given data."""
        current = self._head
        while current is not None:
            if current.data == data:
                return current

            current = current.next

    def remove(self, data):
        """Remove node with a given data."""
        current = self._head
        previous = None
        while current is not None:
            if current.data == data:
                if previous is None:
                    self._head = current.next
                    self._size -= 1
                    break
                else:
                    previous.next = current.next

                self._size -= 1

            previous = current
            current = current.next
