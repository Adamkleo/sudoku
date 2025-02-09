class Stack:
    def __init__(self, max_size=float('inf')):
        self.items = []
        self.max_size = max_size

    def push(self, item) -> None:
        if len(self.items) >= self.max_size:
            raise OverflowError("Max size reached!")
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("Stack empty!")
        return self.items.pop()


    def is_empty(self):
        return len(self.items) == 0