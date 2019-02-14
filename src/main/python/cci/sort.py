import math
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils
from utils import __Title__, __print__
import bisect

__Title__("10.1 정렬된 두 배열 정렬된 상태로 병합")
def merge(listA, listB) :
    insertIdx = len(listA) + len(listB) - 1
    aIdx = len(listA) - 1
    bIdx = len(listB) - 1

    listA.extend(0 for i in range(0,len(listB)))
    while bIdx >= 0 :
        if aIdx >= 0 and listA[aIdx] > listB[bIdx] :
            listA[insertIdx] = listA[aIdx]
            aIdx = aIdx - 1
        else :
            listA[insertIdx] = listB[bIdx]
            bIdx = bIdx - 1
        insertIdx = insertIdx - 1
    return listA

listA = [2,4,6,8,10]
listB = [1,3,5,7,9,11]
__print__(listA)
__print__(listB)
__print__(merge(listA, listB))


__Title__("10.9 각 행과 열이 오름차순인 MxN 행렬에서 특정 원소를 찾는 함수")
def findFromMatrix_v1(matrix, value) :
    for rowIdx in range(0, len(matrix)) :
        for colIdx in range(0, len(matrix[0])) :
            if matrix[rowIdx][colIdx] == value :
                return (rowIdx, colIdx)
    return None

def findFromMatrix_v2(matrix, value) :
    for rowIdx in range(0, len(matrix)) :
        idx = bisect.bisect(matrix[rowIdx], value)
        if matrix[rowIdx][idx - 1] == value :
            return (rowIdx, idx - 1)
    return None

def findFromMatrix_v3(matrix, value) :
    return None

matrix = [
    [15,20,40,85],
    [20,35,80,95],
    [30,55,95,105],
    [49,80,100,200],
]

__print__(findFromMatrix_v1(matrix, 55)) # O(MN)
__print__(findFromMatrix_v2(matrix, 55)) # O(MlogN)


__Title__("10.2 철자만 바꾼 문자열(anagram)이 서로 인접하도록 문자열 배열을 정렬")

__Title__("10.3 n개 정수의 정렬된 배열을 회전시켜 얻은 배열에서 특정 값 찾기")

__Title__("""10.4 size method가 없는 Array 비슷한 자료 구조 Listy가 있다. 
O(1)에 검색 가능한 elementAt(i)는 존재한다면, 원소 x의 인덱스를 반환하는 알고리즘 구현""")

__Title__("10.5 빈 문자열이 섞여 있는 정렬된 문자열에서 특정 문자열을 찾는 함수")
# ["at", "", "", "", "ball", "", "car", "dad", ""]

__Title__("10.6 한줄에 문자열 하나가 쓰여있는 20GB 파일을 정렬하기")

__Title__("10.7 양수 40억개로 이루어진 입력 파일에 없는 정수를 생성하는 알고리즘. (메모리는 1GB만 사용가능)")

__Title__("10.8 1~n(<= 32,000)까지의 중복된 숫자로 이루어진 배열. 사용가능한 메모리가 4KB일때 중복된 원소 모두 출력.")

__Title__("10.9 행과 열이 오름차순인 MxN 행렬. 특정 원소를 찾는 함수")

__Title__("10.10 정수 스트림에서 주기적으로 어떤 수의 랭킹을 확인하고 싶다. 수 하나를 읽을 때마다 호출되는 track(int x)을 구현")
# 입력 스트림 : 5,1,4,4,5,9,7,13,3

__Title__("10.11 인접한 숫자가 커졌다가 작아졌다가를 반복하도록 정렬하는 알고리즘")
# 5,3,1,2,3 => 5,1,3,2,3