# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 1. cycle 찾기
        results = findCycle(head)
        hasCycle = results[0]
        runner = results[1]

        # 2. cycle 크기 구하기
        if hasCycle :
            cycleLength = getCycleLength(runner)

            # 3. head 찾기
            return findCycleStartNode(head, cycleLength)
        else :
            return None

def findCycle(head) :
    slowRunner = head
    fastRunner = head

    # 1. cycle 찾기
    hasCycle = False
    while fastRunner != None and fastRunner.next != None :
        slowRunner = slowRunner.next
        fastRunner = fastRunner.next.next

        if slowRunner == fastRunner :
            return (True, slowRunner)

    return (False, slowRunner)

def getCycleLength(runner) :
    cycleLengthChecker = runner.next

    cycleLength = 1
    while cycleLengthChecker != runner :
        cycleLengthChecker = cycleLengthChecker.next
        cycleLength += 1

    return cycleLength

def findCycleStartNode(head, cycleLength) :
    fastRunner = head
    slowRunner = head

    for i in range(0, cycleLength) :
        fastRunner = fastRunner.next

    while fastRunner != slowRunner :
        slowRunner = slowRunner.next
        fastRunner = fastRunner.next

    return slowRunner
