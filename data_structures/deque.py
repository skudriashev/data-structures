class Deque:

    def __init__(self):
        self._items = []

    def add_front(self, item):
        self._items.insert(0, item)

    def add_back(self, item):
        self._items.append(item)

    def remove_front(self):
        if self._items:
            return self._items.pop(0)

    def remove_back(self):
        if self._items:
            return self._items.pop()

    def size(self):
        return len(self._items)

    def is_empty(self):
        return self.size() == 0
