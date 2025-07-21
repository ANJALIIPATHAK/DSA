class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        pair = sorted(pair) # Sorted based on position

        for p, s in pair[::-1]:
            t = (target - p)/s
            stack.append(t)
            if(len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)

