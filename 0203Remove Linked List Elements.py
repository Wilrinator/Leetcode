def removeElements(self, head, val: int):
        Ans = ListNode(0)
        Ans_tail = Ans
        
        while head:
            if head.val == val:
                Ans_tail.next = head.next
                head= head.next 
            else:
                Ans_tail.next = head    
                Ans_tail = Ans_tail.next  
                head= head.next 
        return Ans.next