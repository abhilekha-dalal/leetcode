class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        max_amount = 0

        while L<R:
            height = min(heights[L], heights[R])
            amount = height * (R-L)
            max_amount = max(max_amount, amount)

            if heights[L] < heights[R]:
                L+=1
            else:
                R-=1
        return max_amount

solution = Solution()  
result = solution.trap([0,2,0,3,1,0,1,3,2,1])  
print(result)
