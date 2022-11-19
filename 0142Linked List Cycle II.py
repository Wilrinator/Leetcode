def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        while head is not None:
            if head.val == 'visited':
                return head
            head.val = 'visited'
            if head.next is None:
                return 
            head = head.next     
        return 
