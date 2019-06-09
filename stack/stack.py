class Stack:

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add item to the top of the stack.

        Time complexity is O(1).
        """
        self._items.append(item)

    def pop(self):
        """Get item from the top of the stack.

        Time complexity is O(1).
        """
        if self._items:
            return self._items.pop()

    def peek(self):
        if self._items:
            return self._items[-1]

    def size(self):
        """Get stack size.

        Time complexity is O(1).
        """
        return len(self._items)

    def is_empty(self):
        """Return if stack is empty.

        Time complexity is O(1).
        """
        return len(self._items) == 0
