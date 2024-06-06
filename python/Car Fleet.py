class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack =[]
        pairs = [(p,s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        for pos, spe in pairs:
            arrival_time = (target - pos)/spe
            stack.append(arrival_time)
            if len(stack)>=2 and stack[-1]<= stack[-2]:
                stack.pop()
        return len(stack)
