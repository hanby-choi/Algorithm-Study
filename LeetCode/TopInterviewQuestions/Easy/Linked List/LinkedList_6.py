# Linked List Cycle
class Solution(object):
    def hasCycle(self, head):
        visit = set()
        while head:
            if head in visit:
                return True
            else:
                visit.add(head)
            head = head.next
        return False
    def hasCycle2(self, head):
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False