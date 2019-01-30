import math
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils
from utils import __Title__, __print__
from collections import deque

utils.__Title__("4.1 방향 그래프가 주어졌을때 두 노드 사이에 경로가 존재하는지 확인")
class Node :
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
        self.visited = False

def hasTrace(start, end) :
    d = deque()
    d.append(start)

    while d :
        current = d.pop()
        if current.value == end.value :
            return True
        for c in current.children :
            if c.visited == False :
                d.append(c)
                c.visited = True
    return False

def node(value, children = []) :
    return Node(value, children)

root = node(1, [node(2), node(3, [node(6), node(7), node(8)]), node(4, [node(9), node(10)]), node(5)])
__print__(hasTrace(root, root.children[1].children[1]))
__print__(hasTrace(root.children[1], root.children[1].children[1]))

utils.__Title__("4.2 최소 트리 : 오름차순 정렬된 중복없는 배열. 이 배열 값으로 만드는 높이가 최소인 트리")
class BinaryTreeNode :
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = Node

def createBTNode(value) :
    node = BinaryTreeNode(value)
    return node

def getDepth(node, depth = 0) :
    if node == None :
        return depth
    d1 = getDepth(node.left, depth + 1)
    d2 = getDepth(node.right, depth + 1)

    return max(d1, d2)

def printTree(node) :
    indent = getDepth(root)
    q = deque()
    q.append([node])

    while q :
        nodes = q.pop()
        space = ['  ' for i in range(indent)]
        nodeValues = [str(node.value) for node in nodes]
        print("%s%s" % ("".join(space), '  '.join(nodeValues)))

        child = []
        for node in nodes :
            if node.left != None :
                child.append(node.left)
            if node.right != None :
                child.append(node.right)
        if len(child) != 0 :
            q.append(child)
        indent = indent - 1

def createBST(list) :
    # find Mid and create node
    # createBST with reft list side
    # createBST with right list side
    # append two child to current node
    if len(list) == 0 :
        return None

    mid = len(list) // 2
    currentNode = createBTNode(list[mid])

    leftNode = createBST(list[:mid])
    rightNode = createBST(list[mid+1:])

    currentNode.left = leftNode
    currentNode.right = rightNode
    return currentNode

list = [1,2,3,4,5,6,7,8]
root = createBST(list)
printTree(root)

utils.__Title__("4.3 이진 트리에서 같은 깊이에 있는 노드를 연결 리스트로 연결. (깊이가 N이면 N개의 연결리스트)")

utils.__Title__("4.4 이진 트리가 균형이 잡혀 있는지 확인하는 함수 (균형 : 높이 차가 최대 1)")

utils.__Title__("4.5 BST 검증 : 주어진 이진 트리가 이진 탐색 트리인지 확인하는 함수")

utils.__Title__("4.6 이진 탐색 트리에서 주어진 노드의 다음 노드(in-order) 찾는 함수. (참고: 각 노드는 부모 노드를 알수있다)")

utils.__Title__("4.7 프로젝트 리스트와 프로젝트 간의 종속 관계가 있을 때 프로젝트 수행 순서를 찾는 알고리즘")

utils.__Title__("4.8 이진 트리에서 노드 2개가 주어졌을 때 두 노드의 조상 노드를 찾는 함수 (노드 저장을 위한 추가 버퍼 없음)")

utils.__Title__("4.9 이진 탐색 트리를 만들어 낼 수 있는 가능한 배열의 목록")
#     2
#   ↙  ↘
# 1     3
# => {2,1,3}, {2,3,1}
utils.__Title__("4.10 2개의 이진 트리가 T1, T2가 있을 때 T2가 T1의 하위 트리인지 확인하는 함수")

utils.__Title__("4.11 이진 트리 클래스 : 삽입, 검색, 삭제, 모든 노드를 같은 확률로 반환하면 getRandomNode를 구현하라")

utils.__Title__("4.12 정수값을 가진 이진 트리에서 특정 값이 되는 경로들의 합. (노드 중간부터여도 상관없음)")

