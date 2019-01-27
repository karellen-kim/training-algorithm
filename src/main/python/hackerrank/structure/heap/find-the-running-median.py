import math
import bisect

def runningMedian(a):
    result = []
    list = []
    for i in a :
        bisect.insort(list, i)

        idx = (len(list) - 1) / 2
        if len(list) % 2 == 1 :
            result.append(list[int(idx)])
        else :
            end = int(math.ceil(idx))
            start = int(math.floor(idx))
            n = float(list[start] + list[end]) / 2
            result.append(n)
    return result

print(runningMedian([1,2,3,4,5,6,7,8,9,10]))