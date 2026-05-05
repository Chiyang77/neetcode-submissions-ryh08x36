class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        w_total = len(heights)
        maxarea = 0
        stack =[]
        stack.append([0,heights[0]])

        for i in range(1, len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                popidx, popheight = stack.pop()
                maxarea = max(popheight*(i-popidx),maxarea)
                start = popidx
            stack.append([start, heights[i]])
        
        for _ in range(len(stack)):
            popidx, popheight = stack.pop()
            maxarea = max(popheight*(w_total-popidx),maxarea)
        
        return maxarea