class Node:
    def __init__(self,val):
        self.val=val
        self.next = None 
class Solution(object):
    def mergeTwoLists(self,l1,l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        #Attach the remaining node
        tail.next = l1 or l2
        return dummy.next
    
def print_list(head):
    while head:
        print(head.val,end=" -> ")
        head = head.next
    print('None')

# First sorted list: 1 -> 3 -> 5
l1 = Node(1)
l1.next = Node(6)
l1.next.next = Node(5)

# Second sorted list: 2 -> 4 -> 6
l2 = Node(2)
l2.next = Node(7)
l2.next.next = Node(6)

print("List 1:")
print_list(l1)
print("List 2:")
print_list(l2)

sol = Solution()
merged = sol.mergeTwoLists(l1, l2)

print("Merged list:")
print_list(merged)

        

