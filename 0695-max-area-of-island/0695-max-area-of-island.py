class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS  = len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS  or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r-1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))
        return maxArea
