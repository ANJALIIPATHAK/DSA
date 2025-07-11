class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def markRow(row):
            for col in range(0, len(matrix[row])):
                if(matrix[row][col] != 0):
                    matrix[row][col] = '*'

        def markCol(col):
            for row in range(0, len(matrix)):
                if(matrix[row][col] != 0):
                    matrix[row][col] = '*'

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                if(matrix[row][col] == 0):
                    markRow(row)
                    markCol(col)

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                if(matrix[row][col] == '*'):
                    matrix[row][col] = 0
