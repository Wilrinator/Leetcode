class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
 
class LinkedList: 
    def __init__(self):
        self.head = None


def reverseList(self, head):
        prev = None
        current = head
        while current:
            Next = current.next
            current.next = prev
            prev = current
            current = Next
        head = prev
        return head