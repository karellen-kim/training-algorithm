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

__Title__("8.1 어떤 아이가 N개의 계단을 오른다. 1,2,3계단을 한번에 오를수 있을때 계단을 오르는 방법은 몇 가지인가")

__Title__("8.2 MxN 격자판을 오른쪽 또는 아래로 이동가능한 로봇. 어떤 cell은 금지구역일때, 왼쪽 상단에서 오른쪽 하단으로 이동하는 알고리즘")

__Title__("8.3 정렬된 배열에서 A[i] = i인 배열을 찾는 함수. (중복없음)")

__Title__("8.4 어떤 집합의 부분집합을 모두 반환하는 함수")

__Title__("8.5 양의 정수 2개를 연산자 없이 곱하는 재귀함수. (+, -, 비트 사용 가능)")

__Title__("8.6 세개의 기둥의 하노이 타워. 왼쪽 끝의 원반을 오른쪽 끝으로 이동.")

__Title__("8.7 문자열의 모든 순열을 계산하는 함수 (중복없음)")

__Title__("8.8 문자열의 모든 순열을 계산하는 함수. 문자열 중복있으나 나열된 순열은 중복되면 안된다.")

__Title__("8.9 n쌍의 괄호로 만들수 있는 모든 조합")

__Title__("8.10 그림판의 영역칠하기(fill) 기능 구현. 특정 지점을 클릭했을때 주변 모든 값이 같은 값이 되어야 한다.")

__Title__("8.11 25센트, 10센트, 5센트, 1센트가 있을 때 n센트를 표현하는 모든 방법의 수")

__Title__("8.12 8x8 체스판 위에 여덟개의 퀸이 서로 잡히지 않도록 배열하는 모든 방법의 수")
