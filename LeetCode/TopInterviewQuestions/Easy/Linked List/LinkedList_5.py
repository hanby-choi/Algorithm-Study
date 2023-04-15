# Palindrome Linked List
class Solution(object):
    def isPalindrome(self, head):
        cnt = 1
        tmp = head
        while tmp.next:
            cnt += 1
            tmp = tmp.next
        if cnt == 1:
            return True
        stack = []
        pnt = head
        mid = int(cnt/2)
        for i in range(mid):
            stack.append(pnt.val)
            pnt = pnt.next
        if cnt % 2 == 1:
            mid += 1
            pnt = pnt.next
        for i in range(mid, cnt):
            if stack[-1] != pnt.val:
                return False
            stack.pop()
            pnt = pnt.next
        return True
    def isPalindrome2(self, head):
        num = []
        while head:
            num.append(head.val)
            head = head.next
        length = len(num)
        mid = int(length/2)
        for i in range(mid):
            if num[i] != num[length-i-1]:
                return False
        return True
    def isPalindrome3(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev