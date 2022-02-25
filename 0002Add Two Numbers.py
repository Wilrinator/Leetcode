# Questions Source: https://leetcode.com/problems/add-two-numbers/

## You are given two non-empty linked lists representing two non-negative integers. 
## The digits are stored in reverse order, and each of their nodes contains a single digit. 
## Add the two numbers and return the sum as a linked list.
## You may assume the two numbers do not contain any leading zero, except the number 0 itself.



### Before I did Leetcode questions, I didnt know anything about LinkedList, so I have to copy everything from others. ###

def addTwoNumbers(l1, l2):
    """   type l1: ListNode, type l2: ListNode, rtype: ListNode    """
    result = ListNode(0)
    result_tail = result
    carry = 0

    while l1 or l2 or carry:  # An interesting way to use while loop
        val1  = (l1.val if l1 else 0)
        val2  = (l2.val if l2 else 0)
        carry, out = divmod(val1 +val2 + carry, 10) # divmod function can produce quotient and remainder

        result_tail.next = ListNode(out)
        result_tail = result_tail.next

        l1 = (l1.next if l1 else None)  # Also an interesting way to use if condition
        l2 = (l2.next if l2 else None)

    return result.next