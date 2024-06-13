class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][1]:
                i, h = stack.pop()
                max_area = max(max_area, h * (idx-i))
                start = i
            stack.append((start, height))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights)-i))
        
        return max_area
            
