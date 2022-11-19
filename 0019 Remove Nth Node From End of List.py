class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        # store data
        self.data = data
        # store reference (next item)
        self.next = None
        return



def removeNthFromEnd(self, head, n: int):
        left, right = head, head
        for i in range(n):
            right = right.next
        if right == None:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next       
        return head


def removeNthFromEnd2(self, head, n: int):
    count = 1
    Ans = ListNode(0)
    Ans_tail = Ans
    Sup = head

    while Sup.next != None:
        # increase counter by one
        count = count + 1
        # jump to the linked node
        Sup = Sup.next

    for i in range(count - n):
        Ans_tail.next = ListNode(head.val)
        Ans_tail = Ans_tail.next
        head = head.next
    Ans_tail.next = head.next
    return Ans.next