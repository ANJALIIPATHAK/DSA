class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if (not grid):
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        numIslands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            while(q):
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if(r in range(0, rows) and c in range(0, cols) and grid[r][c]== "1" and (r,c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))


        for r in range(0, rows):
            for c in range(0, cols):
                if(grid[r][c] == "1" and (r,c) not in visited):
                    bfs(r, c)
                    numIslands += 1

        return numIslands