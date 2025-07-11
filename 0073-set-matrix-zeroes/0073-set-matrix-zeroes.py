class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowMarker = [0]*len(matrix)
        colMarker = [0]*len(matrix[0])

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                if(matrix[row][col] == 0):
                    rowMarker[row] = 1
                    colMarker[col] = 1

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                if(rowMarker[row] == 1 or colMarker[col] == 1):
                    matrix[row][col] = 0
