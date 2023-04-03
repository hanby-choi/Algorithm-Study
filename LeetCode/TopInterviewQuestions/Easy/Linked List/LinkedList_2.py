# Remove Nth Node From End of List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        crnt_node = head
        sz = 1
        while crnt_node.next:
            crnt_node = crnt_node.next
            sz += 1
        if n == 1 and sz == 1: # remove linked list
            head.val = ''
            return  head
        if sz-n == 0: # remove head node
            return head.next
        prev_node = head
        index = 1
        while index < (sz-n):
            prev_node = prev_node.next
            index += 1
        if n == 1: # remove tail node
            prev_node.next = None
        else:
            prev_node.next = prev_node.next.next
        return head
    def removeNthFromEnd2(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first_pnt = second_pnt = dummy
        for i in range(n):
            first_pnt = first_pnt.next
        while first_pnt.next:
            first_pnt = first_pnt.next
            second_pnt = second_pnt.next
        second_pnt.next = second_pnt.next.next
        return dummy.next