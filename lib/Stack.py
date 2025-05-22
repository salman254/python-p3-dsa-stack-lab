class Stack:
    def __init__(self, items=None, limit=None):
        self.items = items if items else []
        self.limit = limit

    def push(self, value):
        if self.limit is not None and len(self.items) >= self.limit:
            return None
        self.items.append(value)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        return self.limit is not None and len(self.items) >= self.limit

    def search(self, value):
        try:
            return len(self.items) - 1 - self.items.index(value)
        except ValueError:
            return -1
