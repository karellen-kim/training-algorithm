class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        mergedList = ListNode(0)
        cur = mergedList

        while l1 != None and l2 != None :

            if l1.val < l2.val :
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else :
                cur.next = ListNode(l2.val)
                l2 = l2.next

            cur = cur.next

        if l1 != None :
            cur.next = l1
        elif l2 != None :
            cur.next = l2

        return mergedList.next
