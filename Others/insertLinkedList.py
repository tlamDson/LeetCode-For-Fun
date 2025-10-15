class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  # Track length

    # Insert val at index (0 = head, -1 = end)
    def insert(self, index, val):
        # Your code here (from previous)
        pass

    # Get val at index (return None if out of bounds)
    def get(self, index):
        if (index < 0 | index > list.size):
        
        pass

    # Add val to end
    def add(self, val):
        # Your code here
        pass

    # Pop (remove) at index, return val (default index=-1 for end)
    def pop(self, index=-1):
        # Your code here
        pass

    # Set val at index (return True if success, False if out of bounds)
    def set(self, index, val):
        # Your code here
        pass

    # NEW: Insert entire other_list after index (0=after head, -1=after end)
    def insertList(self, index, other_list):
        # Your code here: Splice other_list after node at index
        # Update self.size += other_list.size
        # If other_list is empty (head=None), do nothing
        pass

    # Helper: Print list
    def __str__(self):
        if not self.head:
            return "Empty"
        vals = []
        curr = self.head
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " -> ".join(vals)

# Test previous methods + new one
sll = SinglyLinkedList()
sll.add(1)
sll.add(3)
sll.add(5)  # Now: 1 -> 3 -> 5

sll2 = SinglyLinkedList()
sll2.add(2)
sll2.add(4)
sll2.add(6)  # Now: 2 -> 4 -> 6

sll.insertList(1, sll2)  # Insert sll2 after index 1 (after 3): 1 -> 3 -> 2 -> 4 -> 6 -> 5
print(sll)  # Expected: 1 -> 3 -> 2 -> 4 -> 6 -> 5

# Test empty other_list
sll3 = SinglyLinkedList()  # Empty
sll.insertList(0, sll3)  # Should do nothing
print(sll)  # Still: 1 -> 3 -> 2 -> 4 -> 6 -> 5