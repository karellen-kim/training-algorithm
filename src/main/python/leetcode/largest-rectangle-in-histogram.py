class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		
		stack = []
		curPos = 0
		maxArea = 0
		while curPos <= len(heights) :
			
			if curPos == len(heights) :
				curHeight = 0
			else :
				curHeight = heights[curPos]
			
			if len(stack) == 0 or curHeight >= heights[stack[-1]] :
				stack.append(curPos)
				curPos += 1
			else :
				print("stack={}".format(stack))
				lastPos = stack.pop()
				lastHeight = heights[lastPos]
				
				left = 0
				if len(stack) != 0 :
					left = stack[-1] + 1
				
				width = curPos - left
				height = lastHeight
				
				maxArea = max(maxArea, width * height)
				print("lastHeight={}, curHeight={}, left={}, right={}, area={}".format(lastHeight, curHeight, left, curPos, width*height))
			
		return maxArea
