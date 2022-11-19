def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            ahead = curr.next  
            if ahead.val == curr.val:
                curr.next = curr.next.next 
            else:
                curr=curr.next
        return head