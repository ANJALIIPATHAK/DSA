class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []
        for i in range(0, len(matrix)):
            if(matrix[i][0] > target):
                break
            row = matrix[i]

        if(not row):
            return False

        left = 0
        right = len(row) - 1

        while(left <= right):
            mid = (left + right)//2
            if(row[mid] > target):
                right = mid - 1
            elif(row[mid] < target):
                left = mid + 1
            elif(row[mid] == target):
                return True
        return False