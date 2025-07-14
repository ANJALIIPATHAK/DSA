class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def generateRow(row):
            ansRow = [1]
            ans = 1
            for col in range(1, row):
                ans = ans * (row - col)
                ans = ans // col
                ansRow.append(ans)
            return ansRow
        
        pascalTriangle = []
        for row in range(1, numRows + 1):
            tempRow = generateRow(row)
            pascalTriangle.append(tempRow)

        return pascalTriangle