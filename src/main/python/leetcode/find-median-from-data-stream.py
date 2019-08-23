import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smallerNums = []
        self.biggerNums = []
        self.sizeOfSmallerNums = 0
        self.sizeOfBiggerNums = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        if self.sizeOfSmallerNums == 0 or num < self.smallerNums[0] * -1 :
            heapq.heappush(self.smallerNums, num * -1)
            self.sizeOfSmallerNums = self.sizeOfSmallerNums + 1
        else :
            heapq.heappush(self.biggerNums, num)
            self.sizeOfBiggerNums = self.sizeOfBiggerNums + 1

        self.keepBalanceOfHeap()

    def keepBalanceOfHeap(self) :
        if self.sizeOfSmallerNums != self.sizeOfBiggerNums and abs(self.sizeOfSmallerNums - self.sizeOfBiggerNums) > 1 :

            if self.sizeOfBiggerNums > self.sizeOfSmallerNums :
                num = heapq.heappop(self.biggerNums)

                if num != None :
                    heapq.heappush(self.smallerNums, num * -1)
                    self.sizeOfBiggerNums = self.sizeOfBiggerNums - 1
                    self.sizeOfSmallerNums = self.sizeOfSmallerNums + 1
            else :
                num = heapq.heappop(self.smallerNums)

                if num != None :
                    heapq.heappush(self.biggerNums, num * -1)
                    self.sizeOfBiggerNums = self.sizeOfBiggerNums + 1
                    self.sizeOfSmallerNums = self.sizeOfSmallerNums - 1

    def findMedian(self):
        """
        :rtype: float
        """
        #print "##########"
        #print self.smallerNums
        #print self.biggerNums
        meidan = None
        if self.sizeOfSmallerNums > self.sizeOfBiggerNums :
            median = self.smallerNums[0] * -1
        elif self.sizeOfBiggerNums > self.sizeOfSmallerNums :
            median = self.biggerNums[0]
        else :
            median = ((self.smallerNums[0] * -1) + self.biggerNums[0]) / 2.0

        return median