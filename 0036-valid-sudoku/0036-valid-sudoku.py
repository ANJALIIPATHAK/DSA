class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowSet = set()
            for num in row:
                if num != "." and num in rowSet:
                    return False
                rowSet.add(num)
        
        for col in range(0, 9):
            colSet = set()
            for row in range(0, len(board)):
                if board[row][col] != "." and board[row][col] in colSet:
                    return False
                colSet.add(board[row][col])

        for square in range(0, 9):
            squareSet = set()
            for i in range(0, 3):
                for j in range(0, 3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] != "." and board[row][col] in squareSet:
                        return False
                    squareSet.add(board[row][col])
        return True
