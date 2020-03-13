class Solution:
	def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
		
		if destination > start :
			startPos = start
			endPos = destination
		else :
			startPos = destination
			endPos = start
		
		minDistance = 0
		for idx in range(startPos, endPos) :
			minDistance += distance[idx]
		
		return min(sum(distance) - minDistance, minDistance)
