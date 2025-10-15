# Define the Node class first
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the Solution class
class Solution:
    def getLength(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def getMiddle(head):
        length = Solution.getLength(head)
        midIndex = length // 2
        while midIndex > 0:
            head = head.next
            midIndex -= 1
        return head.data

# Create the linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(50)
head.next.next.next.next = Node(50)

# Get the middle element
middle = Solution.getMiddle(head)
print("Middle element:", middle)
