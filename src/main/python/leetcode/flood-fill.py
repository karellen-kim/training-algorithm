from typing import List
import queue


class Point :
	def __init__(self, r, c) :
		self.r = r
		self.c = c
		
	def __str__(self) :
		return "row={r}, col={c}".format(r=self.r, c=self.c)

class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
		
		self.lenRow = len(image)
		self.lenCol = len(image[0])
		
		color = image[sr][sc]
		q = queue.Queue()
		q.put(Point(sr, sc))
		visited = [[ 0 for i in range(self.lenCol) ] for j in range(self.lenRow)]
		
		while q.empty() == False :
			cur = q.get()
			
			if image[cur.r][cur.c] == color :
				image[cur.r][cur.c] = newColor
				
				for neighbor in self.getNeighbors(cur) : 
					if visited[neighbor.r][neighbor.c] == 0 :
						visited[neighbor.r][neighbor.c] = 1
						q.put(neighbor)
					
		return image
		
	def getNeighbors(self, cur, ) :
		r = cur.r
		c = cur.c
		list = []
		
		if r > 0 :
			list.append(Point(cur.r - 1, cur.c))
		if r < self.lenRow - 1 :
			list.append(Point(cur.r + 1, cur.c))
		if c > 0 :
			list.append(Point(cur.r, cur.c - 1))
		if c < self.lenCol - 1 :
			list.append(Point(cur.r, cur.c + 1))
			
		return list	
