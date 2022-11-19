def deleteMiddle(self, head):
        prev, slow, fast = head, head, head        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next        
        if slow == head:
            return head.next        
        prev.next = slow.next
        return head



def deleteMiddle2(self, head):
        count = 0
        Ans = ListNode(0)
        Ans_tail = Ans
        Sup = head  
        
        while Sup:
            count += 1 
            Sup = Sup.next
            
        for i in range(count//2):
            Ans_tail.next = ListNode(head.val)    
            Ans_tail = Ans_tail.next  
            head= head.next
        Ans_tail.next = head.next
        return Ans.next