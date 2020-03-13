class Solution:
	def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

		if not stations :
			if startFuel >= target :
				return 0
			else :
				return -1
		
		self.availalbe = startFuel
		self.target = target
		self.refuelCount = 0
		self.recommendStations = []
		self.recommendStations.append(stations[0])
		
		for station in stations[1:] :	
			if self.canGoThere(station[0]) == False :
				self.doRefuel(station[0])

			if self.canGoThere(station[0]) == False :
				return -1
			else :
				self.addRecommendStation(station)
		
		if self.canGoThere(target) == False :
			self.doRefuel(target)				

		if self.canGoThere(target) == False :
			return -1		
		else :
			return self.refuelCount
	
	def canGoThere(self, destination) :
		return self.availalbe >= destination
		
	def doRefuel(self, destination) :
		
		while self.recommendStations and self.availalbe < destination :
			rec = self.recommendStations[-1]
			if self.availalbe >= rec[0] :
				self.availalbe += rec[1]
				self.recommendStations.pop()
				self.refuelCount += 1
			else :
				break
			
	def addRecommendStation(self, station) :
		greaterThan = []
		
		while self.recommendStations :
			rec = self.recommendStations[-1]
			
			if station[1] < rec[1] :
				greaterThan.append(rec)
				self.recommendStations.pop()
			else :
				break
				
		self.recommendStations.append(station)
		
		while greaterThan :
			self.recommendStations.append(greaterThan.pop())

