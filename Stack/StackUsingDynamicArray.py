class Stack:
    def __init__(self):
        self._data = []

    def size(self):
        return len(self._data)

    def push(self, value):
        self._data.append(value)  # we can still use append, or implement manually

    def pop(self):
        if self.size() == 0:
            raise IndexError("pop from empty stack")
        # manually remove and return the last element
        last_index = len(self._data) - 1
        value = self._data[last_index]
        self._data = self._data[:last_index]  # remove last element
        return value

    def top(self):
        if self.size() == 0:
            raise IndexError("top from empty stack")
        return self._data[-1]
