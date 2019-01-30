import math
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import itertools
import utils
from utils import __Title__, __print__

__Title__("8.0 모든 순열")
result = []
def getSubSet(array, subList = []) :
    if len(array) == 0 :
        return subList

    newSubSet = append(subList, array[0])
    result.append(newSubSet)

    getSubSet(array[1:], subList)
    getSubSet(array[1:], newSubSet)

def append(array, item) :
    newArray = array.copy()
    newArray.extend(item)
    return newArray

getSubSet(['a', 'b', 'c'], [])
print(result)