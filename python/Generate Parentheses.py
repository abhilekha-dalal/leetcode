class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #we can add open paranthesis if open < n
        # we can add close paranthesis if close < open
        # stop iff open ==close==n
        stack =[]
        res = []

        def dfs(openN, closeN):
            #usually base case is the state to add result in backtracking
            if openN == closeN ==n:
                res.append("". join(stack))
            # add ( and call dfs by updating state change, dfs keeps on calling deep until a roadblock, then it starts popping back
            if openN < n:
                stack.append("(")
                dfs(openN+1, closeN)
                stack.pop()
          # add ) and call dfs by updating state change, dfs keeps on calling deep until a roadblock, then it starts popping back  
          if closeN < openN:
                stack.append(")")
                dfs(openN, closeN+1)
                stack.pop()
        dfs(0,0)
        return res
