class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        newMatrix = [[] for i in range(0, len(matrix))]
        for row in range(len(matrix)-1, -1, -1):
            newRow = 0
            for col in range(0, len(matrix[0])):
                newMatrix[newRow].append(matrix[row][col])
                newRow += 1

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                matrix[row][col] = newMatrix[row][col]