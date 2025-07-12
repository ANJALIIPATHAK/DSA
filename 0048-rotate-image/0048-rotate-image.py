class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        newMatrix = [[0] * len(matrix[0]) for i in range(0, len(matrix))]
        
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                newMatrix[col][len(matrix)-1 - row] = matrix[row][col]

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                matrix[row][col] = newMatrix[row][col]
        