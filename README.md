# Leetcode

## Two pointers
| Problem no # | Problem Title | Solution | Difficulty | Hints |
|----------|:--------:|---------:|---------:|---------:|
| 167 | [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [python](https://github.com/abhilekha-dalal/leetcode/blob/main/python/Two%20Sum.py) | medium | L=0; R=end; keep looking at L+R until reach T
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | [python](https://github.com/abhilekha-dalal/leetcode/blob/main/python/3sum.py) | medium | keep 1 fixed, for 2 and 3 - Two Sum
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [python](https://github.com/abhilekha-dalal/leetcode/blob/main/python/Max%20Water%20Container.py) | medium | L=0; R=end; <br>amount = min(heights at L, R) * width; move min(L, R)
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/) | [python](https://github.com/abhilekha-dalal/leetcode/blob/main/python/Trapping%20Rain%20Water.py) | hard | L=0; R=end;maxL, maxR = height[L], height[R]; <br> maxL = max(maxL, height[L]) res+= maxL-height[L]<br>(same for right)
## Stack
| Problem no # | Problem Title | Solution | Difficulty | Hints |
|----------|:--------:|---------:|---------:|---------:|
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/) | [python](https://github.com/abhilekha-dalal/leetcode/blob/main/python/Valid%20Parentheses.py) | easy | stack.append(opening bracket) <br> if closing == stack[-1] then pop, len(stack) ==0
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/) | [python](https://github.com/abhilekha-dalal/leetcode/blob/main/python/Generate%20Parentheses.py) | medium | open == close == n: append to result<br> if open < n: stack.append("(") call dfs then pop <br> if close < open: stack.append(")") call dfs then pop
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/description/) | [python](https://github.com/abhilekha-dalal/leetcode/blob/main/python/Min%20Stack.py) | medium | keep stack and minStack <br> min = min(minstack[-1], val
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/) | [python](https://github.com/abhilekha-dalal/leetcode/blob/main/python/Evaluate%20Reverse%20Polish%20Notation.py) | medium | append int to stack, pop on operation sign <br> append res to stack
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/) | [python](https://github.com/abhilekha-dalal/leetcode/blob/main/python/Daily%20Temperatures.py) | medium | use stack to append (idx, temp); <br> keep checking for temp > stack[-1][1]<br> if yes pop and calculate index diff to append to res.
| 853 | [Car Fleet](https://leetcode.com/problems/car-fleet/description/) | [python](https://github.com/abhilekha-dalal/leetcode/blob/main/python/Car%20Fleet.py) | medium | reverse sorting on position imp:-<br> car starting at large position will reach earlier<br>(rest depending upon speed)<br> calculate arrival time for that<br> if time<=last car time: pop that


