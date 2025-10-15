class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class Solution(object):
    def getMiddle(head):
        slowptr = head
        fastptr = head 

        while fastptr is not None and fastptr.next is not None:

            #move the fast pointer by 2 nodes
            fastptr = fastptr.next.next

            #move the slow pointer by one node
            slowptr = slowptr.next
        return slowptr.data


# Create the linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

print(Solution.getMiddle(head))