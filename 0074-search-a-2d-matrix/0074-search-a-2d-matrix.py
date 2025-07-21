class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        topRow = 0
        bottomRow = rows - 1
        while(topRow <= bottomRow):
            midRow = (topRow + bottomRow)//2
            if(target > matrix[midRow][-1]):
                topRow = midRow + 1
            elif(target < matrix[midRow][0]):
                bottomRow = midRow - 1
            else:
                break

        left = 0
        right = len(matrix[midRow])-1
        finalRow = matrix[midRow]
        while(left <= right):
            mid = (left + right)//2
            if(finalRow[mid] > target):
                right = mid - 1
            elif(finalRow[mid] < target):
                left = mid + 1
            elif(finalRow[mid] == target):
                return True
        return False

