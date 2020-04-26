class MinStack:

	def __init__(self):
		self.list = []
		
	def push(self, x: int) -> None:
		minValue = x
		if self.list :
			minValue = self.getMin()
			
		self.list.append((x, min(minValue, x)))
		
	def pop(self) -> None:
		self.list.pop()
		
	def top(self) -> int:
		if self.list :
			return self.list[-1][0]
		
	def getMin(self) -> int:
		if self.list :
			return self.list[-1][1]
			
