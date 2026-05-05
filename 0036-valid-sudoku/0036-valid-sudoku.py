class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)

        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rowSet[row] or board[row][col] in colSet[col] or board[row][col] in squareSet[(row//3, col//3)]:
                    return False
                rowSet[row].add(board[row][col])
                colSet[col].add(board[row][col])
                squareSet[(row//3, col//3)].add(board[row][col])
        return True

                