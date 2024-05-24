class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        max_amount = 0

        while L < R:
            max_height = min(heights[L], heights[R])
            width = R - L
            amount = max_height * width

            max_amount = max(max_amount, amount)
            if heights[L] <= heights[R]: L+=1
            else: R-=1
        
        return max_amount

solution = Solution()  # Instantiate Solution class
result = solution.maxArea([1,7,2,5,4,7,3,6])
print(result)
