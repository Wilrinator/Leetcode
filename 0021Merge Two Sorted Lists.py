def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    Ans = ListNode(0)
    Ans_tail = Ans

    while l1 or l2:
        val1 = (l1.val if l1 else 1000)
        val2 = (l2.val if l2 else 1000)
        if val1 <= val2:
            Ans_tail.next = ListNode(val1)
            Ans_tail = Ans_tail.next
            l1 = (l1.next if l1 else None)
        elif val1 >= val2:
            Ans_tail.next = ListNode(val2)
            Ans_tail = Ans_tail.next
            l2 = (l2.next if l2 else None)
        elif val1 == 1000 and val2 == 1000:
            break
    return Ans.next

def mergeTwoLists2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Ans = ListNode(0)
        Ans_tail = Ans
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    Ans_tail.next = ListNode(l1.val)
                    Ans_tail = Ans_tail.next
                    l1 = l1.next
                elif l1.val >= l2.val:
                    Ans_tail.next = ListNode(l2.val)
                    Ans_tail = Ans_tail.next
                    l2 = l2.next
            elif l1:
                Ans_tail.next = ListNode(l1.val)
                Ans_tail = Ans_tail.next
                l1 = l1.next
            else:
                Ans_tail.next = ListNode(l2.val)
                Ans_tail = Ans_tail.next
                l2 = l2.next
        return Ans.next


def mergeTwoLists3(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1 and not l2:  # If both lists empty - return None
        return None
    if not l1 or not l2:  # If one of the lists empty - return the other list
        return l1 or l2
    if l1.val < l2.val:  # If first ll val is lower - return new Node with this value and recursively merge ll's without first element in first ll
        return ListNode(val=l1.val, next=self.mergeTwoLists(l1.next, l2))
    else:  # If second ll val lower or equal - same step as before, but without first element in second ll
        return ListNode(val=l2.val, next=self.mergeTwoLists(l1, l2.next))