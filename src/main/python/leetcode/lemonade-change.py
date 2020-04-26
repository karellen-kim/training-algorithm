class Solution:
	def lemonadeChange(self, bills: List[int]) -> bool:
		moneyToIndex = { 5 : 2, 10 : 1, 20 : 0}
		indexToMoney = {v: k for k, v in moneyToIndex.items()}
		
		changes = [0, 0, 0] # [twenty, ten, five]
		
		for bill in bills :
			shouldReturn = bill - 5
			
			#print("bill={}, changes={}, shouldReturn={}".format(bill, changes, shouldReturn))
			
			for idx in range(len(changes)) :
				change = indexToMoney[idx]
				if shouldReturn == 0 :
					break
					
				while changes[idx] != 0 and shouldReturn >= change :
					shouldReturn -= change
					changes[idx] -= 1
			
			if shouldReturn != 0 :
				return False
			else :
				changes[moneyToIndex[bill]] += 1
				
				
		return True
