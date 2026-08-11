class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0 : 0} # Maps position to number of gaps at that position

        for row in wall:
            position = 0
            for brick in row[ : -1]:
                position += brick
                countGap[position] = 1 + countGap.get(position, 0)

        return len(wall) - max(countGap.values())
