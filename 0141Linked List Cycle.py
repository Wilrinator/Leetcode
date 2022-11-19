def hasCycle2(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        
        return False



def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        while head is not None:
            if head.val == 'visited':
                return True
            head.val = 'visited'
            if head.next is None:
                return False
            head = head.next
     
        return False