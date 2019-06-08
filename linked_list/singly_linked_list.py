class Node:

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
        return self._head is None

    def add_front(self, data):
        node = Node(data, self._head)
        self._head = node
        self._size += 1

    def size(self):
        return self._size

    def search(self, data):
        current = self._head
        while current is not None:
            if current.data == data:
                return current

            current = current.next

    def remove(self, data):
        current = self._head
        previous = None
        while current is not None:
            if current.data == data:
                if previous is not None:
                    previous.next = current.next
                else:
                    self._head = None

                self._size -= 1

            previous = current
            current = current.next
