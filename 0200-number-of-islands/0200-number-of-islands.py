class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row,col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while(q):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if(r in range(ROWS) and
                    c in range(COLS) and 
                    grid[r][c] == "1" and 
                    (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r,c))

        visited = set()
        numIslands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    numIslands += 1

        return numIslands
                