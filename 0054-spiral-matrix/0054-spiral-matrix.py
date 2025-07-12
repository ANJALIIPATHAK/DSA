class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        numOfRows = len(matrix)
        numOfCols = len(matrix[0])
        left = 0
        right = numOfCols-1
        top = 0
        bottom = numOfRows-1
        res = []

        while(top <= bottom and left <= right):

            # Traverse Top Row (left -> right)
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Traverse Right Column (top -> bottom)
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Traverse Bottom Row (right -> left)
            if(top <= bottom):
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # Traverse Left Column (bottom -> top)
            if(left <= right):
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res