import heapq

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):

        list = []
        for node in lists :
            while node != None :
                heapq.heappush(list, node.val)
                node = node.next

        root = ListNode(0)
        smallestNode = root
        while len(list) != 0 :
            smallestValue = heapq.heappop(list)
            smallestNode.next = ListNode(smallestValue)

            smallestNode = smallestNode.next

        return root.next
