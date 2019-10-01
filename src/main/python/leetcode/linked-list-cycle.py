# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slowRunner = head
        fastRunner = head
        while fastRunner != None and fastRunner.next != None:
            slowRunner = slowRunner.next
            fastRunner = fastRunner.next.next

            if slowRunner == fastRunner :
                return True

        return False
