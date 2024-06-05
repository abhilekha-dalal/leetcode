class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack  = []

        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackidx, stacktemp = stack.pop()
                res[stackidx] = ind - stackidx
            stack.append([ind, temp])
        return res
