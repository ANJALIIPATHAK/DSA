class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                if(matrix[row][col] == 0):
                    matrix[row][0] = 0
                    if(col != 0):
                        matrix[0][col] = 0
                    else:
                        col0 = 0

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                if(matrix[row][col] != 0):
                    if(matrix[0][col] == 0 or matrix[row][0] == 0):
                        matrix[row][col] = 0

        if(matrix[0][0] == 0):
            for col in range(0, len(matrix[0])):
                matrix[0][col] = 0

        if(col0 == 0):
            for row in range(0, len(matrix)):
                matrix[row][0] = 0
