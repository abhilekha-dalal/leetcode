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
