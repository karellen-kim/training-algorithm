class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        index = 0
        medianNode = head
        curNode = head
        while curNode.next != None :
            if index % 2 == 0 :
                medianNode = medianNode.next

            curNode = curNode.next
            index = index + 1

        return medianNode