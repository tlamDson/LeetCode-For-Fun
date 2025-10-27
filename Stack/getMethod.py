def get(self, index):
    if self.is_empty():
        raise ValueError("Cannot get index from an empty stack")
    if index < 0 or index >= self.size():
        raise IndexError("Index out of bounds")

    current = self.top  
    count = 0
    while count < index:
        current = current.next
        count += 1
    return current.data
