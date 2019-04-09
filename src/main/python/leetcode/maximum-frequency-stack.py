class FreqStack():

    def __init__(self):
        self.countEachNumber = {}
        self.freqNumber = {}
        self.maxFreqCount = 0

    def push(self, x):
        count = self.countEachNumber.get(x, 0) + 1
        self.countEachNumber[x] = count
        if self.maxFreqCount < count :
            self.maxFreqCount = count

        sameFreqNumbers = self.freqNumber.get(count, [])
        sameFreqNumbers.append(x)
        self.freqNumber[count] = sameFreqNumbers

    def pop(self):
        if self.maxFreqCount == 0 :
            return None
        if self.maxFreqCount in self.freqNumber and len(self.freqNumber.get(self.maxFreqCount)) > 0:
            sameFreqNumbers = self.freqNumber.get(self.maxFreqCount)
            maxFreqNumber = sameFreqNumbers.pop()
            count = self.countEachNumber.get(maxFreqNumber, 0)
            self.countEachNumber[maxFreqNumber] = count - 1
            return maxFreqNumber
        else :
            self.maxFreqCount -= 1
            return self.pop()

stack = FreqStack()

list = [5,7,5,7,4,5]
for item in list :
    stack.push(item)

freq = stack.pop()
while freq != None :
    print(freq)
    freq = stack.pop()