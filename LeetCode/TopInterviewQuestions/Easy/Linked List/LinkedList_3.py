# Reverse Linked List
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        find_head = False
        new_head = ''
        while head.next:
            prev_node = head
            while prev_node.next.next:
                prev_node = prev_node.next
            prev_node.next.next = prev_node
            if not find_head:
                new_head = prev_node.next
                find_head = True
            prev_node.next = None
        return new_head
    def reverseList2(self, head):
        node, prev = head, None
        while node: # node.next를 prev 리스트로 연결
            next_node, node.next = node.next, prev
            prev, node = node, next_node
        return prev
    def reverseList3(self, head):
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev