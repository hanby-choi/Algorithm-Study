# Merge Two Sorted List
class Solution(object):
    def mergeTwoLists(self, list1, list2):        
        start = ListNode()
        dummy = start
        while list1 and list2:
            if list1.val < list2.val:
                start.next = list1
                list1 = list1.next
            else:
                start.next = list2
                list2 = list2.next
            start = start.next   
        self.dealLast(start, list1)
        self.dealLast(start, list2)
        return dummy.next    
        
    def dealLast(self, start, list_):
        while list_:
            start.next = list_
            list_ = list_.next
            start = start.next

    def mergeTwoLists2(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2        
        return dummy.next   

    def mergeTwoLists3(self, list1, list2):        
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
"""     if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1 == None and list2 == None:
            return None"""