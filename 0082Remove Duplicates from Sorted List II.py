def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Ans = ListNode(0)
        Ans_tail = Ans
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next 
                Ans_tail.next = head.next                
            else:
                Ans_tail.next = head    
                Ans_tail = Ans_tail.next  
            head= head.next 
        return Ans.next